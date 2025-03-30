---
Autor: Daniel McDonald, Jose C Clemente, Justin Kuczynski, Jai Ram Rideout, Jesse Stombaugh, Doug Wendel, Andreas Wilke, Susan Huse, John Hufnagle, Folker Meyer, Rob Knight, J Gregory Caporaso
Publicación: GigaScience 2012
KeyWords: BIOM, Ome-Ome, Omics, collector curve, rarefraction analysis
---
# Índice:
- [[#Ideas principales]]
- [[#Resumen]]
- [[#Citas (texto)]]
- [[#Papers derivados]]
- [[#Cita (paper)]]
---
# Ideas principales:
La idea general del paper es demostrar la importancia de la reducción del cuello de botella de la bionformática, siendo este causado generalmente por la cantidad de [[Omics (Bioinformatics)|omics]] a tratar y el tamaño de las muestras. Para hacer frente a este problema la mejor solución es la estandarización de formatos.

---
# Resumen:
Los avances en las técnicas de secuenciación de ADN han hecho que la abundancia de datos sobre "comparative [[Omics (Bioinformatics)|omics]]" crezca exponencialmente. Lo cual genera un gran cuello de botella a la hora de investigar.  Un mecanismo que puede reducir dicho cuello de botella consiste en la estandarización de formatos, lo cual facilitaría compartir y archivar los datos, haciéndolos más [[Principios FAIR|FAIR]].

El aumento de la abundancia de datos también conlleva al desarrollo de nuevas categorías, todas ellas con sus particularidades y soluciones para representar los datos de interés de cada campo. ¿Cómo podemos entonces crear un formato universal? Analizando los distintos tipos de datos utilizados en análisis comparativo de omics, observamos un hilo conductor que los une, los "sample by observation contingency table". Una matriz de abundancia de observaciones por muestra. Podemos utilizar "rarefaction analysis" como los "collector curves" para tratar todo tipo de datos.

El biom file format está basado en [[JSON]], y hay más información sobre el tema en [[biom-format]].

---
# Citas (texto):


---
# Papers derivados:
- [[]]

---
# Temas para profundizar:
- [[Rarefaction Analysis]]
- [[Collector Curves]]
- [[Biological Contingency Tables]]

---
# Cita (paper):
McDonald et al: The Biological Observation Matrix (BIOM) format or: how I learned to stop worrying and love the ome-ome. GigaScience 2012 1:7.

---
#paper 
#tfg