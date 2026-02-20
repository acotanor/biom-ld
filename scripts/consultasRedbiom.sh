#!/bin/bash
out="./outputConsultas"

# Busqueda básica, metadatos que contengan la raíz de la palabra "oak".
echo "Metadatos que contengan la raíz de la palabra 'oak':"
redbiom search metadata oak

# Exportar una variable de entorno "ctx" para acceder al contexto de forma comoda.
export ctx=Pick_closed-reference_OTUs-Greengenes-Illumina-16S-V4-5c6506

# Búsqueda de muestras que contienen la raíz de "oak" en el contexto seleccionado.
echo "Muestras que contienen la raíz de 'oak' en el contexto: $ctx"
redbiom search metadata oak | head | redbiom fetch samples --context $ctx --output "$out/oak_example.biom"

# Búsqueda de los metadatos de las muestras obtenidas con la query anterior.
echo "Metadatos de las muestras obtenidas con la query anterior"
redbiom search metadata oak | head | redbiom fetch sample-metadata --context $ctx --output "$out/oak_example_metadata.txt"

# 
