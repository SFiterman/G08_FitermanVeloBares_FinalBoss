from src.LecturaArchivo import abrirArchivo
from src.Cargo import Cargo
from src.Ship import Ship
from src.Cruise import Cruise



def main() -> None:
 barcos=[]
 cargos=[]
 cruceros=[]
 lectura=[]
 
 lectura= abrirArchivo()
 
 for i in range (1, len(lectura)):
   if lectura[i][2] != "" and lectura[i][3]!= "" : # es cargooo
      cargos.append(Cargo(float(lectura[i][0]), float(lectura[i][1]),float(lectura[i][2]), float(lectura[i][3])))
    
      try:
        auxCargo= cargos[i].is_worth_it()
      except Exception as e: 
        print(str(e))

   elif lectura[i][2] != "" and lectura[i][3]== "" : #es crucerooo
      cruceros.append(Cruise(float(lectura[i][0]), float(lectura[i][1]),float(lectura[i][2])))
      try:
        auxCruise= cruceros[i].is_worth_it()
      except Exception as e: 
        print(str(e))
   elif lectura[i][2] == "" and lectura[i][3]== "" : #es barco nomral
      barcos.append(Ship(float(lectura[i][0]), float(lectura[i][1])))
      try:
        auxShip= barcos[i].is_worth_it()
      except Exception as e: 
        print(str(e))
     
        

  
  
if __name__ == "__main__":
  main()