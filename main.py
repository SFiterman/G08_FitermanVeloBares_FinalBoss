from src.LecturaArchivo import abrirArchivo
from src.Cargo import cargo
from src.Ship import ship
from src.Cruise import cruise


def main() -> None:
 print("Hola!!!!!!!")
 
 barcos=[]
 cargos=[]
 cruceros=[]
 lectura=[]
 
 lectura= abrirArchivo()
 
 for i in range (1, len(lectura)):
   if lectura[i][2] != "" and lectura[i][3]!= "" : # es cargo
      cargos.append(cargo(float(lectura[i][0]), float(lectura[i][1]),float(lectura[i][2]), float(lectura[i][3])))
    
      try:
        auxCargo= cargos[i].is_worth_it()
      except Exception as e: 
        print(str(e))

   elif lectura[i][2] != " " and lectura[i][3]== " " : #es crucero
      cruceros.append(cruise(float(lectura[i][0]), float(lectura[i][1]),float(lectura[i][2])))
      try:
        auxCruise= cruceros[i].is_worth_it()
      except Exception as e: 
        print(str(e))
        
   elif lectura[i][2] == " " and lectura[i][3]== " " : #es barco normal
      barcos.append(ship(float(lectura[i][0]), float(lectura[i][1])))
      try:
        auxShip= barcos[i].is_worth_it()
      except Exception as e: 
        print(str(e))
     
        

  
  
if __name__ == "__main__":
  main()