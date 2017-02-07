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