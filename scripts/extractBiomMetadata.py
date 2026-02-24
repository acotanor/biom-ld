import biom
from pathlib import Path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extractor de metadatos de un archivo .biom")
    parser.add_argument("-i", "--input", help="Ruta del archivo del que extraer los metadatos. Debe ser un archivo .biom.", required=True)
    parser.add_argument("-o", "--output", help="Ruta del archivo de texto que contendrá los metadatos del input.", required=True)
    parser.add_argument("-v", "--verbose", help="Muestra los metadatos extraidos en la terminal.", action="store_true")

    obs_metadata = parser.add_mutually_exclusive_group(required=True)
    obs_metadata.add_argument("--raw", help="Modo de extracción; se extraen los metadatos de las observaciones en crudo", action="store_true")
    obs_metadata.add_argument("--rich", help="Modo de extracción; se extraen los campos de los metadatos de las observaciones de forma separada, se muestra la taxonomía sin la definición del diccionario.", action="store_true")
    

    args = parser.parse_args()

    try:
        table = biom.load_table(args.input)

    except Exception as e:
        print(f"""Error al cargar el archivo {args.input}:
            - {e}""")

    output_path = Path(args.output)
    sobrescribir = True

    if output_path.exists() and output_path.stat().st_size > 0:
        r = input("El archivo no está vacío. ¿Quieres sobrescribirlo? (s/n): ").strip().lower()
        sobrescribir = r == "s"

    if sobrescribir:
        with open(args.output, 'w') as f:
            # Metadatos del archivo.
            t = f"""
ID:                 {table.table_id}
Table-Type:         {table.type}
Format-URL:         {biom.util.get_biom_format_url_string()}
Format-Version:     {table.format_version}
Generated-By:       {table.generated_by}
Creation-Date:      {table.create_date}
Shape:              {table.shape}
Non-Zero-Values:    {table.nnz}
Density:            {table.get_table_density():.2%}

"""
            if args.verbose:print(t)
            f.write(t)

            # Metadatos de las muestras.
            for sample_id in table.ids(axis='sample'):
                t = f"Sample {sample_id} metadata: {table.metadata(id=sample_id, axis='sample')}\n"
                if args.verbose:print(t)
                f.write(t)

            # Metadatos de las observaciones.
            if args.raw:
                for observation_id in table.ids(axis='observation'):
                    t = f"Observation {observation_id} metadata: {table.metadata(id=observation_id, axis='observation')}\n"
                    if args.verbose:print(t)
                    f.write(t)
            elif args.rich:
                for observation_id in table.ids(axis='observation'):
                    t = f"Observation {observation_id} taxonomy: {';'.join([t for t in table.metadata(id=observation_id, axis='observation').get('taxonomy') if t])}\n"
                    if args.verbose:print(t)
                    f.write(t)
            else:
                print("Se debe elegir un modo de extracción de metadatos; --raw o --rich.")
                exit(1)


    else:
        print("Operación cancelada.")
        exit(0)