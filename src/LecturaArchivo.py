import csv

def abrirArchivo():
    listabarcos=[]
    with open ("ships.csv") as file:
        reader=csv.reader(file) 
        for row in reader:
            listabarcos.append(row)
    return listabarcos



