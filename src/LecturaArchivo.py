import csv
from Cruise import Cruise
from Ship import Ship
from Cargo import Cargo


def abrirArchivo():
    listabarcos=[]
    with open ("ships.csv") as file:
        reader=csv.reader(file) 
        for row in reader:
            listabarcos.append(row)
    return listabarcos



