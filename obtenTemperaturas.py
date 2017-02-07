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
import numpy as np

def obtenTem(t):
 t=t.replace('<span class="wx-value">',"")
 t=t.replace('</span>',"")
 t=int(float(t))
 return (t)


url1='https://www.wunderground.com/history/airport/MMMX/'
url3='/DailyHistory.html'

os.chdir(r'C:/../Documents/temperaturas')
f=open('fechas0.txt')
matriz = np.array([0, 0, 0,0], np.int32)

for line in f:
 print line
 url=url1+str(line.rstrip("\n"))+url3
 print url
 r = urllib.urlopen(url).read()
 soup = BeautifulSoup(r)
 datosT = soup.find_all("span", class_="wx-value")
 tmedia=obtenTem(str(datosT[0]))
 tmaxima=obtenTem(str(datosT[1]))
 tminima=obtenTem(str(datosT[4]))
 precipitacion=obtenTem(str(datosT[8]))
 #print'Temperatura media: ', tmedia
 #print'Temperatura maxima: ', tmaxima
 #print'Temperatura minima: ', tminima
 #print'Mm de lluvia: ', precipitacion
 vector=[tmedia,tmaxima,tminima, precipitacion]
 matriz=np.vstack([matriz,vector])
 #print matriz

f.close()

np.savetxt("datosAeropuertoMMMX.csv", matriz, delimiter=",")
