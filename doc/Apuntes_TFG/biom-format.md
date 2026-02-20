
# Índice:
- [[#Motivación]]
- [[#Versiones]]
	- [[#BIOM 1.0 Basado en JSON]]
		- [[#Estructura de BIOM en JSON]]
			- [[#Ejemplo]]
		- [[#Pros y contras]]
	- [[#BIOM 2.1 Basado en HDF5]]
		- [[#Estructura de BIOM en HDF5]]
			- [[#Ejemplo en DDL (data description language)]]
- [[#Bibliografía]] 
---
# Motivación:
El cuello de botella de la bioinformática se causa por el análisis de los datos más que por su adquisición. Por lo que la Biological Observation Matrix (BIOM) se diseñó para facilitar este trabajo. La idea es estandarizar la representación de las ome-ome haciendo alusión de las características estructurales específicas de las tablas de contingencia biológicas. 

Los datos biológicos se caracterizan por su escasez, en un estudio típico cualquier muestra contiene muy poca información. Por lo que las tablas de contingencia tienen una densidad de menos del 1%, esto significa que la mayoría de las entradas de la matriz son cero. El formato TSV, por ejemplo, sí almacenaba dichos ceros, lo cual aumentaba significativamente el coste de memoria.
>> McDonald et al: The Biological Observation Matrix (BIOM) format or: how I learned to stop worrying and love the ome-ome. GigaScience 2012 1:7.

---
# Versiones:
Existen dos formatos principales; BIOM 1.0 (basado en json) y BIOM 2.0/2.1 (basado en HDF5).
## BIOM 1.0 Basado en JSON:
Aunque está prácticamente reemplazado por la versión 2.1 de HDF5 en el caso de datasets muy grandes, sigue siendo un formato válido y frecuente sobre todo en pipelines antiguas o en herramientas web.
### Estructura de BIOM en JSON:
![[BIOM_json.png]]
Los campos más interesantes son, sobre todo, matrix_type y data, el primero por que define la estructura de la matriz, lo cual facilita el tratamiento y la compresión de los datos, y el segundo por contar con la información de la muestra. 
Las estructuras de datos posibles, definidas por matrix_type, son las que siguen:
- dense:
	- Se utiliza un array de dos dimensiones estándar, es decir se representa la matriz en su totalidad, con todos los ceros y con cada valor observado. (Esta estructura existe solo por motivos de compatibilidad con estudios pequeños y densos aunque sea tan ineficiente).
- sparse:
	- Los datos se almacenan en una lista de triplets; \[\[row_index,col_index,value],\[row_index,col_index,value]...] 
	- \[\[0,1,12.0],\[5,3,1.5]] Significa que en las posiciones de la matrix (0,1) y (5,3) se observan los valores 12.0 y 1.5 respectivamente, y el resto de posiciones son ceros.
	- Aunque el formato no requiere que los datos vayan ordenados estos suelen estarlo por filas o columnas.
>>_The biom file format: Version 1.0—Biom-format.org_. (s. f.).
#### Ejemplo:
```json
{
     "id":"w00asdt",
     "format": "1.0.0",
     "format_url": "http://biom-format.org",
     "type": "OTU table",
     "generated_by": "QIIME revision XYZ",
     "date": "2011-12-19T19:00:00",
     "rows":[
        {"id":"GG_OTU_1", "metadata":{"taxonomy":["k__Bacteria", "p__Proteobacteria", "c__Gammaproteobacteria", "o__Enterobacteriales", "f__Enterobacteriaceae", "g__Escherichia", "s__"]}},
        {"id":"GG_OTU_2", "metadata":{"taxonomy":["k__Bacteria", "p__Cyanobacteria", "c__Nostocophycideae", "o__Nostocales", "f__Nostocaceae", "g__Dolichospermum", "s__"]}},
        {"id":"GG_OTU_3", "metadata":{"taxonomy":["k__Archaea", "p__Euryarchaeota", "c__Methanomicrobia", "o__Methanosarcinales", "f__Methanosarcinaceae", "g__Methanosarcina", "s__"]}},
        {"id":"GG_OTU_4", "metadata":{"taxonomy":["k__Bacteria", "p__Firmicutes", "c__Clostridia", "o__Halanaerobiales", "f__Halanaerobiaceae", "g__Halanaerobium", "s__Halanaerobiumsaccharolyticum"]}},
        {"id":"GG_OTU_5", "metadata":{"taxonomy":["k__Bacteria", "p__Proteobacteria", "c__Gammaproteobacteria", "o__Enterobacteriales", "f__Enterobacteriaceae", "g__Escherichia", "s__"]}}
        ],
     "columns":[
        {"id":"Sample1", "metadata":{
                                 "BarcodeSequence":"CGCTTATCGAGA",
                                 "LinkerPrimerSequence":"CATGCTGCCTCCCGTAGGAGT",
                                 "BODY_SITE":"gut",
                                 "Description":"human gut"}},
        {"id":"Sample2", "metadata":{
                                 "BarcodeSequence":"CATACCAGTAGC",
                                 "LinkerPrimerSequence":"CATGCTGCCTCCCGTAGGAGT",
                                 "BODY_SITE":"gut",
                                 "Description":"human gut"}},
        {"id":"Sample3", "metadata":{
                                 "BarcodeSequence":"CTCTCTACCTGT",
                                 "LinkerPrimerSequence":"CATGCTGCCTCCCGTAGGAGT",
                                 "BODY_SITE":"gut",
                                 "Description":"human gut"}},
        {"id":"Sample4", "metadata":{
                                 "BarcodeSequence":"CTCTCGGCCTGT",
                                 "LinkerPrimerSequence":"CATGCTGCCTCCCGTAGGAGT",
                                 "BODY_SITE":"skin",
                                 "Description":"human skin"}},
        {"id":"Sample5", "metadata":{
                                 "BarcodeSequence":"CTCTCTACCAAT",
                                 "LinkerPrimerSequence":"CATGCTGCCTCCCGTAGGAGT",
                                 "BODY_SITE":"skin",
                                 "Description":"human skin"}},
        {"id":"Sample6", "metadata":{
                                 "BarcodeSequence":"CTAACTACCAAT",
                                 "LinkerPrimerSequence":"CATGCTGCCTCCCGTAGGAGT",
                                 "BODY_SITE":"skin",
                                 "Description":"human skin"}}
        ],
     "matrix_type": "sparse",
     "matrix_element_type": "int",
     "shape": [5, 6], 
     "data":[[0,2,1],
             [1,0,5],
             [1,1,1],
             [1,3,2],
             [1,4,3],
             [1,5,1],
             [2,2,1],
             [2,3,4],
             [2,5,2],
             [3,0,2],
             [3,1,1],
             [3,2,1],
             [3,5,1],
             [4,1,1],
             [4,2,1]
            ]
    }
```
>> https://github.com/biocore/biom-format/blob/master/examples/rich_sparse_otu_table.biom
### Pros y contras:
La mayor ventaja es que es un formato simple y basado en texto, esto lo hace muy fácil de leer e interpretar sin necesidad de parsear ni visualizar información. Por lo que cumplir satisfactoriamente [[Principios FAIR|los principios FAIR]] pasaría por simplemente describir de forma exhaustiva los metadatos de cada archivo. Sin embargo, el formato flojea cuando se quieren analizar muestras grandes y o complejas, además, no permite mucha compresión cuando la densidad de los datos es alta.
## BIOM 2.1 Basado en HDF5:
La transición a la versión 2.1 supone un cambio de enfoque para el formato, pasamos de texto fácilmente legible por personas a almacenamiento binario de alto rendimiento. Esta versión utiliza Hierarchical Data Format version 5 ([[HDF5]]), la cual está diseñada para datos científicos complejos. Aunque introduce complejidad en la estructura y análisis de los archivos este formato permite el acceso aleatorio y una buena compresión de los datos.
### Estructura de BIOM en HDF5:
![[BIOM_HDF5.png]]

#### Ejemplo en DDL (data description language):
```json
HDF5 "examples/rich_sparse_otu_table_hdf5.biom" {
GROUP "/" {
   ATTRIBUTE "creation-date" {
      DATATYPE  H5T_STRING {
         STRSIZE H5T_VARIABLE;
         STRPAD H5T_STR_NULLTERM;
         CSET H5T_CSET_ASCII;
         CTYPE H5T_C_S1;
      }
      DATASPACE  SCALAR
      DATA {
      (0): "2014-07-29T16:16:36.617320"
      }
   }
   ATTRIBUTE "format-url" {
      DATATYPE  H5T_STRING {
         STRSIZE H5T_VARIABLE;
         STRPAD H5T_STR_NULLTERM;
         CSET H5T_CSET_ASCII;
         CTYPE H5T_C_S1;
      }
      DATASPACE  SCALAR
      DATA {
      (0): "http://biom-format.org"
      }
   }
   ...
```
>> https://github.com/biocore/biom-format/blob/master/examples/rich_sparse_otu_table_hdf5.biom


---
# Codificación y Endianness:

---
# Compresión:


---
# Bibliografía:
1.  McDonald et al: The Biological Observation Matrix (BIOM) format or: how I learned to stop worrying and love the ome-ome. GigaScience 2012 1:7.
2. _The biom file format: Version 1.0—Biom-format.org_. (s. f.). Recuperado 18 de septiembre de 2025, de [https://biom-format.org/documentation/format_versions/biom-1.0.html](https://biom-format.org/documentation/format_versions/biom-1.0.html)
3. _The biom file format: Version 2.1—Biom-format.org_. (s. f.). Recuperado 18 de septiembre de 2025, de [https://biom-format.org/documentation/format_versions/biom-2.1.html](https://biom-format.org/documentation/format_versions/biom-2.1.html)