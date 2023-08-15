class Ship:
 pesotripulacion= 1.5 #static, luego lo uso con Ship no con Self, claro SELF=THIS
 def __init__(self, draft, crew):
    self.draft = draft
    self.crew = crew


def is_worth_it(self):
  pesoFinal= self.calcularPeso
  
  if (pesoFinal > 20):
        print("¡TRIPULACION ATAQUE!") 
  else:
     raise ValueError ("¡TRIPULACION BAJE LA GUARDIA! No hay tal botin:,)")

def calcularPeso(self): #metodo virtual de la madre. NO TIENE EL VIRTUAL
   aux= self.draft - (self.crew* Ship.pesotripulacion)
   return aux 