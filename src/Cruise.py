from Ship import Ship
class Cruise(Ship):
 pesoPasajero= 2.25 #static
 def __init__(self, passengers, draft, crew):
    self.passengers = passengers


def is_worth_it(self): #VIRTUAL HIJO
  pesoFinal= self.calcularPeso
  
  if (pesoFinal > 20):
        print("¡TRIPULACION ATAQUE!") 
  else:
     raise ValueError ("¡TRIPULACION BAJE LA GUARDIA! No hay tal botin:,)")

def calcularPeso(self): #VIRTUAL HIJO
   aux= self.draft - (self.crew* Ship.pesotripulacion + self.passengers*Cruise.pesoPasajero)
   return aux