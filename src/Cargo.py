from Ship import Ship

class Cargo (Ship):
 def __init__(self, cargo, quality, draft, crew): #constructor.
    Ship.__init__(self, draft, crew)
    self.cargo = cargo
    self.quality = quality

def is_worth_it(self)->float: #VIRTUAL HIJO
   pesoFinal= self.calcularPeso
   
   if pesoFinal > 0:
      print("Peso Barco:", pesoFinal)
           
   else:
       print("Peso Barco Negativo:", pesoFinal, "Error probable")
        
   if pesoFinal >= 20:
      print("¡TRIPULACION ATAQUE!") 
   else:
      raise ValueError("¡TRIPULACION BAJE LA GUARDIA! No hay tal botin")

   return pesoFinal       

 
def calcularPeso(self)->float: #VIRTUAL HIJO
   auxCargo=0

   if(self.quality==1):
      auxCargo=3.5
   elif(self.quality==0.5):
    auxCargo=2
   elif(self.quality==0.25):
    auxCargo=0.5
   
   auxCargo = auxCargo*self.quality #asumimos que todos los cargos son del mismo peso por como esta presentado en el archivo csv
   aux= self.draft - (self.crew*Ship.pesoTripulacion + auxCargo)
   return aux
