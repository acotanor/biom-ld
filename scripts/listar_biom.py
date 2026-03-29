import os
import argparse
from typing import List, Tuple

def listar_archivos(ruta_base: str, reverse: True, extension: str) -> List[Tuple[str, float]]:
    """
    Lista archivos .biom, los ordena por tamaño de menor a mayor
    y devuelve su ruta junto con su peso.
    """
    archivos_con_peso = []

    for raiz, _, archivos in os.walk(ruta_base):
        for archivo in archivos:
            if archivo.lower().endswith(extension):
                ruta_completa = os.path.join(raiz, archivo)
                # Obtener el tamaño en bytes
                tamaño = os.path.getsize(ruta_completa)
                archivos_con_peso.append((ruta_completa, tamaño))

    archivos_con_peso.sort(key=lambda x: x[1], reverse=reverse)
    
    return archivos_con_peso

def formatear_tamaño(bytes: int) -> str:
    """
    Convierte bytes a KB, MB o GB.
    """
    for unidad in ['B', 'KB', 'MB', 'GB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unidad}"
        bytes /= 1024
    return f"{bytes:.2f} TB"

def print_res(resultados, n):
    print(f"PUESTO \t| {'RUTA':<50} | \t{'TAMAÑO'}")
    print("-" * 75)
    cont = 1
    if n == -1: n=len(resultados+1)
    for ruta, tam in resultados:
        print(f"{cont}\t| {ruta:<50} | \t{formatear_tamaño(tam)}")
        cont += 1
        if cont == n+1: break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script que lista los archivos .biom de un directorio y sus subcarpetas.")
    parser.add_argument("-i", "--input", type=str, help="Ruta del directorio a listar.", required=True)
    parser.add_argument("-n", type=int, help="La cantidad de archivos que mostrar, si es -1 se muestran todos.", default="-1")
    parser.add_argument("-r", "--reverse", action="store_true", help="Si se ordena de mayor a menor o no.")
    parser.add_argument("-e", "--extension", type=str, help="Extensión de los archivos a listar, .biom por defecto.", default=".biom")

    args = parser.parse_args()

    print_res(listar_biom(args.input,args.reverse,args.extension),args.n)