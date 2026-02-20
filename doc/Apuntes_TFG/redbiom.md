# Índice:


Redbiom es un servicio de caché para muestras de datos y metadatos. Pensado para encontrar muestras por características y metadatos, además de poder reunir dichas muestras en el formato [[biom-format|BIOM]]. Se implementa con una base de datos no-sql llamada [[Redis]]. 

---
# Estructura de los comandos:
Redbiom utiliza una interfaz de comandos por niveles, y está pensado para que las queries se asemezcan a una frase en inglés que represente el significado de lo que se encargará el comando.

- redbiom
	- admin          Update database, etc.
	- fetch            Sample data and metadata retrieval.
	- search         Feature and sample search support.
	- select          Select items based on metadata
	- summarize  Summarize things.

Cada opción tiene subopciones para enriquecer y especificar más la búsqueda.
# Contextos:
El primer paso a la hora de utilizar redbiom es determinar el o los contextos a utilizar. La motivación de los mismos es agrupar datos similares para reducir sesgos al comparar resultados. El comando:
```bash
redbiom summarize contexts
```
lista los contextos disponibles con algo de información básica sobre los mismos:
```bash
# Output de ejemplo:
ContextName	SamplesWithData	FeaturesWithData	Description
Pick_closed-reference_OTUs-Greengenes-illumina-16S-v4-100nt-a243a1	129596	74983	Qiita context
Pick_closed-reference_OTUs-Greengenes-flx-16S-v2-41ebc6	3034	24839	Qiita context
...
```
Para acceder a  un contexto de forma cómoda  se puede exportar como una variable del entorno:
```bash
export ctx=Pick_closed-reference_OTUs-Greengenes-Illumina-16S-V4-5c6506
```
# Categorías:
redbiom permite hacer búsquedas por categorías de metadatos, una de interés es "qiita_empo_3" pues esta representa la ontología del [[Earth Microbiome Project]].
```bash
redbiom summarize metadata-category --category "qiita_empo_3" --counter
# Output:
Category value	count
Hypersaline (saline)	13
water 34
...
```
# Consultas básicas:
## Búsqueda:
```sh
redbiom search metadata oak | head
```
Este ejemplo devuelve las muestras de [Qiita](https://qiita.ucsd.edu/)(servicio que redbiom utiliza por defecto) con metadatos que contengan la raíz de la palabra "oak". Además el output de los comandos están pensados para ser tratados fácilmente con pipelines de Unix.




#tfg 
#Informática 
#Uni 
