class Ship:
    pesoTripulacion = 1.5  # static, luego lo uso con Ship no con Self, claro SELF=THIS

    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self) -> None:
        pesoFinal = self.calcularPeso()
        
        if pesoFinal > 20:
            print("¡TRIPULACION ATAQUE!") 
        else:
            raise ValueError("¡TRIPULACION BAJE LA GUARDIA! No hay tal botin:,")

    def calcularPeso(self):
        aux = self.draft - (self.crew * Ship.pesoTripulacion)
        return aux
