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


while(flag!="0"):
    print("Ingrese Rut a verificar:")
    rut = str(input())
    for row in rows:
        if row[2]== rut:
            if(row[3]!="0"):
                print("Esta vigente")
            else: print("No esta vigente")
            break
    print("ingrese 1 si desea verificar otro rut o 0 para terminar la tarea")
    flag = input()    

    