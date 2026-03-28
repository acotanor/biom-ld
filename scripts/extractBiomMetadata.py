import biom
from pathlib import Path
import argparse
import sys
import os
import numpy as np

def listar_biom(ruta_base: str) -> List[str]:
    """
    Función que lista todos los archivos .biom de las subcarpetas de un directorio.
    Parametros:
        - ruta_base: El directorio donde buscar los archivos .biom.
    Returns:
        - rutas_biom: Lista con todos las rutas de todos los archivos.
    """
    rutas_biom = []
    for raiz, carpetas, archivos in os.walk(ruta_base):
        for archivo in archivos:
            if archivo.lower().endswith('.biom'):
                ruta_completa = os.path.join(raiz,archivo)
                rutas_biom.append(ruta_completa)
    return rutas_biom

def extraer_metadatos(ruta_biom: str, rich: bool) -> Dict():
    """
    Función que extrae los metadatos de un archivo .biom.
    Parametros:
        - ruta_biom: La ruta del archivo.
        - rich: Si se tratan o no los metadatos taxonómicos.
    Returns:
        - metadata: Un diccionario con los metadatos del archivo.
    """
    try:
        table = biom.load_table(ruta_biom)

    except Exception as e:
        print(f"""Error al cargar el archivo {ruta_biom}:
            - {e}""")
        sys.exit(1)
    
    metadata = {
        "id": table.table_id,
        "table-type":table.type,
        "url":biom.util.get_biom_format_url_string(),
        "version":table.format_version,
        "generated-by":table.generated_by,
        "creation-date":table.create_date,
        "shape":table.shape,
        "nnz":table.nnz,
        "density":f"{table.get_table_density():.2%}"
    }
    
    # Metadatos de las muestras.
    metadata["Samples"]=[]
    for sample_id in table.ids(axis='sample'):
        metadata["Samples"].append({sample_id.item():table.metadata(id=sample_id, axis='sample')})

    # Metadatos de las observaciones.
    metadata["Observations"]=[]
    if rich:
        for observation_id in table.ids(axis='observation'):
            metadata["Observations"].append({observation_id:';'.join([t for t in table.metadata(id=observation_id, axis='observation').get('taxonomy') if t])})
    else:
        for observation_id in table.ids(axis='observation'):
            metadata["Observations"].append({observation_id:table.metadata(id=observation_id, axis='observation')})

    return metadata

def generar_informe(metadatos: Dict(), output: str, verbose: bool):
    output_path = Path(output)
    sobrescribir = True

    if output_path.exists() and output_path.stat().st_size > 0:
        r = input("El archivo no está vacío. ¿Quieres sobrescribirlo? (s/n): ").strip().lower()
        sobrescribir = r == "s"
    
    if sobrescribir:
        with open(output, 'w') as f:
            # Metadatos del archivo.
            t = f"""
ID:                 {metadatos["id"]}
Table-Type:         {metadatos["table-type"]}
Format-URL:         {metadatos["url"]}
Format-Version:     {metadatos["version"]}
Generated-By:       {metadatos["generated-by"]}
Creation-Date:      {metadatos["creation-date"]}
Shape:              {metadatos["shape"]}
Non-Zero-Values:    {metadatos["nnz"]}
Density:            {metadatos["density"]}

"""
            f.write(t)
            print(t)

            for sample in metadatos["Samples"]:
                for metadata in sample:
                    t = f"Sample: {metadata} metadata: {sample[metadata]}"
                    f.write(f"\n{t}")
                    if verbose: print(t)
            
            for observation in metadatos["Observations"]:
                for metadata in observation:
                    t = f"Observation: {metadata} metadata: {observation[metadata]}"
                    f.write(f"\n{t}")
                    if verbose: print(t)

    else:
        print("Operación cancelada.")
        exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extractor de metadatos de un archivo .biom")
    parser.add_argument("-i", "--input", help="Ruta del archivo del que extraer los metadatos.", required=True)
    parser.add_argument("-o", "--output", help="Ruta del archivo de texto que contendrá los metadatos del input.", required=True)
    parser.add_argument("-v", "--verbose", help="Muestra los metadatos extraidos en la terminal.", action="store_true")

    obs_metadata = parser.add_mutually_exclusive_group(required=True)
    obs_metadata.add_argument("--raw", help="Modo de extracción; se extraen los metadatos de las observaciones en crudo", action="store_true")
    obs_metadata.add_argument("--rich", help="Modo de extracción; se extraen los campos de los metadatos de las observaciones de forma separada, se muestra la taxonomía sin la definición del diccionario.", action="store_true")
    
    args = parser.parse_args()

    generar_informe(extraer_metadatos(args.input,args.rich),args.output,args.verbose)

    