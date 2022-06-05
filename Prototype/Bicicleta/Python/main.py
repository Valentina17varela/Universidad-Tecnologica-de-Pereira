import copy

class Bicicleta:
    def clone(self):
        pass

    def __init__(self,color,rodado):
        self.color = color
        self.rodado = rodado
        
    def verBicicleta(self):
        print("")

class BicicletaModificada(Bicicleta):
    def clone(self):
        return copy.copy(self)

    def verBicicleta(self):
        print("Este es el color: "+self.color+", Este es el rodado: "+self.rodado)

def Cliente():
    bc = BicicletaModificada("Rojo","22")
    bc.verBicicleta()
    bc2 = bc.clone()
    bc2.__init__("Negro","30")
    bc2.verBicicleta()

if __name__ =="__main__":
    Cliente()