import copy

class TelefoniaCelular:
    def clone(self):
        pass
   
    def setters (self,cargo_fijo,datos,minutos):
        self.cargo_fijo = cargo_fijo
        self.datos = datos
        self.minutos = minutos

    def getters(self):
        return "Cargo fijo: "+self.cargo_fijo+" Datos: "+self.datos+" Minutos celular: "+self.minutos

    def impresion(self):
        print("")
   

class Plan(TelefoniaCelular):
    def clone(self):
      return copy.copy(self)

    def impresion(self):
        return self.getters()


def Cliente():
    Plan1 = Plan()
    Plan1.setters("35000 pesos", "15GB", "300min")
    print("\nPlan1")
    print(Plan1.impresion())

    Plan2 = Plan1.clone()
    Plan2.setters("45000 pesos", "25GB", "650min")
    print("\nPlan2")
    print(Plan2.impresion())

    Plan3 = Plan1.clone()
    Plan3.setters("60000 pesos", "40GB", "ilimitados")
    print("\nPlan3")
    print(Plan3.impresion())


if __name__ == "__main__":
    Cliente()