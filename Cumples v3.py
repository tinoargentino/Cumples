#Cumples v2
#Consultas: valentinsch@gmail.com
#https://github.com/tinoargentino

from urllib.request import urlopen
from bs4 import BeautifulSoup
import smtplib, ssl
import requests
import csv
import datetime


# # Elegir cantidad de años
while True:
    try:
        years = int(input("Cuantos años querés actualizar? Recomiendo entre 1 y 3: "))
    except ValueError:
        print("Disculpas, no entendí eso, probá de nuevo.")
        continue
    else:
        break

filename ='cumples.html'
outfile = 'cumples.csv'

file = open(filename, "r")
file2=open(outfile, "w")

soup = BeautifulSoup(file, 'html.parser')
divTag = soup.findAll('li',{'class':'_43q7'})
len(divTag)

file2.write('Subject' +','+ 'Start Date' + ',' + 'All Day Event' + '\r')
registros=0

for tag in divTag:
    text = tag.find("a")['data-tooltip-content']

    name=text.split('(')[0]
    date=text.split('(')[1].replace(")","")
    #print(name)
    registros+=1
    for i in range(years):
        file2.write('Cumple de ' + name +','+ date + "/" + str(datetime.datetime.today().year+i) + ',' + 'TRUE' + '\r')

print("El archivo cumples.csv está listo. Se copiaron " + str(registros) + " cumples.")
