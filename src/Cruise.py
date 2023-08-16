from Ship import Ship
class Cruise(Ship):
 pesoPasajero= 2.25 #static
 def __init__(self, passengers, draft, crew):
    Ship.__init__(self, draft, crew)
    self.passengers = passengers


def is_worth_it(self)->float: #VIRTUAL HIJO
  pesoFinal= self.calcularPeso
  if pesoFinal > 0:
      print("Peso Barco:", pesoFinal)
           
  else:
       print("Peso Barco Negativo:", pesoFinal, "Error probable")
        
  if pesoFinal >= 20:
      print("¡TRIPULACION ATAQUE!") 
  else:
      raise ValueError("¡TRIPULACION BAJE LA GUARDIA! No hay tal botin:,")

  return pesoFinal         

def calcularPeso(self)->float: #VIRTUAL HIJO
   aux= self.draft - (self.crew* Ship.pesotripulacion + self.passengers*Cruise.pesoPasajero)
   return aux