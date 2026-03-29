# Explicación:
QIITA-public es un directorio con todos los archivos .biom y documentos de texto con sus metadatos públicos de qiita.

Debido al tamaño del archivo original QIITA-public (136.2GB descomprimido), he extraido los metadatos de cada archivo biom y los iré subiendo poco a poco utilizando lfs para poder tratarlos.

# Cambios realizados a la carpeta original:
La carpeta original contiene tres subcarpetas; BIOM (archivos .biom sin procesar), processed_data (archivos .biom procesados), templates (metadatos de algunas muestras). Todos los archivos .biom de la carpeta BIOM están almacenados en una carpeta con un identificador único de 6 dígitos, en processed_data al haber pocos están todos en la misma carpeta. 

El problema reside en que BIOM contenía originalmente 18624 carpetas con un archivo .biom, entonces hacer operaciones sobre la carpeta consume mucho tiempo. Por suerte los identificadores están repartidos de forma más o menos uniforme, hay aproximadamente 11000 que empiezan por 1 y unos 3000 que empiezan por dos, pero el resto de digitos son bastante parejos. Y he aprovechado esto para poder separar las carpetas en subcarpetas y así trabajar en lotes manejables.

Ahora BIOM contiene 10 carpetas; 1...,2...,...,9... Y cada una de estas carpetas otras 10; 10...,11...,...,19...

El resto de archivos respetan la disposición original.

## Comando de rsync para sincronizar las carpetas:
Ejecutado desde la raiz del repo:
```bash
rsync -avm --include='*/' --include='*.txt' --exclude='*.biom' /mnt/datos/TFG/QIITA-public/BIOM/1... ./scripts/data/QIITA-public/BIOM
```