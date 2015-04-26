# -*- coding: utf-8 -*-
__author__ = 'Richard'

# Tengo que instalar el beautiful soup: pip install beautifulsoup4  & pip install requests
#
# En este proyecto voy a scrapear resulados de partidos de futbol con la siguiente información
#   1.- Temporada
#   2.- Jornada
#   3.- Equipos
#   4.- Resultado
#   5.- Fecha
#
# Para ello voy a obtener los resultados de dos webs:
#   1º.- http://www.bdfutbol.com                -> Obtengo los resultados de las temporadas anteriores
#   2º.- http://www.resultados-futbol.com       -> Obtengo los resultado de la presente temporada 2014-15
#
#   También voy a obtener en ficheros los partidos de cada jornada para poder predecir sus resultados


import ScrapBDFutbol as bdFutbol
import ScrapTemporada2014 as thisTemporada

# Guardo los partidos de futbol en un diccionario
partidos = dict()

# Obtengo los partidos de futbol de las temporadas anteriores
partidos = bdFutbol.getPartidos()

# Obtengo los partidos de futbol de la temporada presente
partidos2014_15 = thisTemporada.getPartidos(bdFutbol.getContador())



file = open('DataSetPartidos.txt','w')
for key,value in partidos.items():
    file.write('%s\n' %str(value))

for key,value in partidos2014_15.items():
    file.write('%s\n' %str(value))

file.close()
