import copy

class Camiseta:
    def clone(self):
        pass
   
    def setters (self,talla,color,estampado):
        self.talla = talla
        self.color = color
        self.estampado = estampado

    def getters(self):
        return "Talla: "+self.talla+" Color: "+self.color+" Estampado: "+self.estampado

    def impresion(self):
        print("")
   

class CamisetaMCorta(Camiseta):
    def clone(self):
      return copy.copy(self)

    def impresion(self):
        return self.getters()


def Cliente():
    c1 = CamisetaMCorta()
    c1.setters("40", "rojo", "prototipo1")
    print(c1.impresion())

    c2 = c1.clone()
    c2.setters("20", "azul", "Prototipo2")
    print(c2.impresion())


if __name__ == "__main__":
    Cliente()