from Ship import Ship

class Cargo (Ship):
 def __init__(self, cargo, quality, draft, crew): #constructor.
    self.cargo = cargo
    self.quality = quality

def is_worth_it(self): #VIRTUAL HIJO
  pesoFinal= self.calcularPeso
  
  if (pesoFinal > 20):
        print("¡TRIPULACION ATAQUE!") 
  else:
     raise ValueError ("¡TRIPULACION BAJE LA GUARDIA! No hay tal botin:,)")

def calcularPeso(self): #VIRTUAL HIJO
   auxCargo=0

   if(self.quality==1):
      auxCargo=3.5
   elif(self.quality==0.5):
    auxCargo=2
   elif(self.quality==0.25):
    auxCargo=0.5
   
   auxCargo = auxCargo*self.quality #asumimos que todos los cargos son del mismo peso por como esta presentado en el archivo csv
   aux= self.draft - (self.crew* Ship.pesoTripulacion + auxCargo)
   return aux
