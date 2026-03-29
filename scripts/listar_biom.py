import os
import argparse
from typing import List, Tuple

def listar_archivos(ruta_base: str, reverse: bool, extension: str) -> List[Tuple[str, float]]:
    """
    Lista archivos con la extensión dada, los ordena por tamaño
    y devuelve su ruta junto con su peso.
    """
    archivos_con_peso = []

    for raiz, _, archivos in os.walk(ruta_base):
        for archivo in archivos:
            if archivo.lower().endswith(extension):
                ruta_completa = os.path.join(raiz, archivo)
                tamaño = os.path.getsize(ruta_completa)
                archivos_con_peso.append((ruta_completa, tamaño))

    archivos_con_peso.sort(key=lambda x: x[1], reverse=reverse)
    
    return archivos_con_peso

def formatear_tamaño(bytes: int) -> str:
    """
    Convierte bytes a KB, MB o GB.
    """
    tam = float(bytes)
    for unidad in ['B', 'KB', 'MB', 'GB']:
        if tam < 1024:
            return f"{tam:.2f} {unidad}"
        tam /= 1024
    return f"{tam:.2f} TB"

def print_res(resultados: List[Tuple[str, float]], n: int):
    print(f"PUESTO \t| {'RUTA':<50} | \t{'TAMAÑO'}")
    print("-" * 75)
    
    if n == -1: 
        n = len(resultados)
        
    cont = 1
    for ruta, tam in resultados:
        print(f"{cont}\t| {ruta:<50} | \t{formatear_tamaño(tam)}")
        cont += 1
        if cont > n: 
            break

    print("-" * 75)
    cantidad_total = len(resultados)
    
    if cantidad_total == 0:
        print("No se encontraron archivos con esa extensión.")
    else:
        # Sumamos el tamaño de todos los archivos encontrados
        tamaño_total_bytes = sum(tam for _, tam in resultados)
        
        print(f"TOTAL ARCHIVOS: {cantidad_total}")
        print(f"PESO TOTAL:     {formatear_tamaño(tamaño_total_bytes)}")
        
        if n < cantidad_total:
            print(f"(Mostrando los primeros {n} archivos de {cantidad_total})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script que lista los archivos de un directorio y sus subcarpetas.")
    parser.add_argument("-i", "--input", type=str, help="Ruta del directorio a listar.", required=True)
    # Mejor usar default=-1 (como entero) en lugar de "-1" (como string)
    parser.add_argument("-n", type=int, help="La cantidad de archivos que mostrar, si es -1 se muestran todos.", default=-1)
    parser.add_argument("-r", "--reverse", action="store_true", help="Si se ordena de mayor a menor o no.")
    parser.add_argument("-e", "--extension", type=str, help="Extensión de los archivos a listar, .biom por defecto.", default=".biom")

    args = parser.parse_args()

    resultados_busqueda = listar_archivos(args.input, args.reverse, args.extension)
    print_res(resultados_busqueda, args.n)