import csv
from Codificador import qrCodificador

file = open("lista_etapa_1.csv")
csvreader = csv.reader(file)
nombre, apellido, rut = next(csvreader)
for usuario in csvreader:
    nombre, apellido, rut = usuario
    qrCodificador(nombre,apellido,rut)
file.close()