class Ship:
    pesoTripulacion = 1.5  # static, luego lo uso con Ship no con Self, claro SELF=THIS
    contadorShip = 0
    
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        Ship.contadorShip = Ship.contadorShip +1

    def is_worth_it(self) ->float:
        pesoFinal = self.calcularPeso()
        
        if pesoFinal > 0:
           print("Peso Barco:", pesoFinal)
           
        else:
            print("Peso Barco Negativo:", pesoFinal, "Error probable")
        
        if pesoFinal >= 20:
            print("¡TRIPULACION ATAQUE!") 
        else:
            raise ValueError("¡TRIPULACION BAJE LA GUARDIA! No hay tal botin (Menor a 20)")
        
        return pesoFinal         

    def calcularPeso(self) ->float:
        aux = self.draft - (self.crew * Ship.pesoTripulacion)
        return aux
