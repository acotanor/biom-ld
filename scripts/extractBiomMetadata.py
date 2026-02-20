import biom
from pathlib import Path
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extractor de metadatos de un archivo .biom")
    parser.add_argument("-i", "--input", help="Ruta del archivo del que extraer los metadatos. Debe ser un archivo .biom.", required=True)
    parser.add_argument("-o", "--output", help="Ruta del archivo de texto que contendrá los metadatos del input.", required=True)
    
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
            for sample_id in table.ids(axis='sample'):
                # Obtenemos los metadatos de cada muestra
                t = f"Sample {sample_id} metadata: {table.metadata(id=sample_id, axis='sample')}"
                print(t)
                f.write(t)

            for observation_id in table.ids(axis='observation'):
                # Obtenemos los metadatos de cada observación
                t = f"Observation {observation_id} metadata: {table.metadata(id=observation_id, axis='observation')}"
                print(t)
                f.write(t)

    else:
        print("Operación cancelada.")