import csv

flag=1
fields = []
rows = []

filename = "lista_vig_etapa_1.csv"
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)


### codigo para agregar usuarios

print("Ingrese Nombre:")
nombre=input()
print("Ingrese Apellido")
apellido=input()
print("Rut")
rut=input()
print("vigente")
vigente=input()
qrPath= "qrPath"
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the data rows
    csvwriter.writerows(rows)