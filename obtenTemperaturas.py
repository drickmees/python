# Este script descarga las temperaturas maxima, promedio y minima, y precipitacion
# desde el sitio https://www.wunderground.com/history/airport/MMMX/
# la url puede cambiarse en la variable url1 por ejemplo a
# https://www.wunderground.com/history/airport/KLRD/. Las fechas de
# obtencion estan en el archivo fechas0.txt, al final la url completa se
# guarda en la variable url. El resultado es un csv donde la primera columna es
# la temperatura promedio, segunda es la maxima, tercera es la minima, y la cuarta
# columna es la precipitacion en mm; cada fila corresponde a los datos de cada dia.

__author__ = 'mrmendo'

from bs4 import BeautifulSoup
import urllib
import os
import numpy

url1='https://www.wunderground.com/history/airport/MMMX/'
url3='/DailyHistory.html'

os.chdir(r'C:/Users/mrmendo/Documents/temperaturas')
f=open('fechas.txt')

for line in f:
 print line
 url2=str(line.rstrip("\n"))
 url=url1+url2+url3
 print url
 #r = urllib.urlopen(url).read()





f.close()
