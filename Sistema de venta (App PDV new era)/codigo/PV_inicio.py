from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from tkinter import *
import PV_sumaParcial
import PV2
import GD_inicio
import BaseDatos
import analizar
import autenticacion

contador = 0

def segunda_ventana():
    director = Director()
    builder2 = ConstructorVentana2()
    director.builder = builder2


class ConstructorVentanas(ABC):
    @abstractproperty
    def agregar_componentes(self) -> None:
        pass

    @abstractmethod
    def eliminar(self) -> None:
        pass

    @abstractmethod
    def buscar(self) -> None:
        pass

    @abstractmethod
    def agregar(self) -> None:
        pass

    @abstractmethod
    def facturar(self) -> None:
        pass


class ConstructorVentana1(ConstructorVentanas):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._elementos = Ventana1()

    @property
    def agregar_componentes(self) -> Ventana1:
        elementos = self._elementos
        self.reset()
        return elementos

    def eliminar(self) -> None:
        pass

    def buscar(self) -> None:
        pass

    def agregar(self) -> None:
        pass

    def facturar(self) -> None:
        pass
        

class ConstructorVentana2(ConstructorVentanas):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._elementos = Ventana2()

    @property
    def agregar_componentes(self) -> Ventana2:
        elementos = self._elementos
        self.reset()
        return elementos

    def eliminar(self) -> None:
        pass

    def buscar(self) -> None:
        pass

    def agregar(self) -> None:
        pass

    def facturar(self) -> None:
        pass
 

class Ventana1():
    def __init__(self):
        #crea la ventana en donde se muestra la interfaz
        self.CL = Tk()
        self.CL.geometry("400x400")
        self.CL.title("PDV nueva era")
        self.CL.configure(background = "dark blue")
        self.B1 = Button(self.CL, text="Nueva venta", width=20, command=self.eliminar,foreground="white",background="red", font=("", 14)).place(x=80, y=70)
        self.B2 = Button(self.CL, text="Devolucion", width=20, command=self.eliminar2,foreground="white",background="red", font=("", 14)).place(x=80, y=130)
        self.B3 = Button(self.CL, text="Analizar", width=20, command=self.eliminar3,foreground="white",background="red", font=("", 14)).place(x=80, y=190)
        self.B3 = Button(self.CL, text="Seguridad", width=20, command=self.eliminar4,foreground="white",background="red", font=("", 14)).place(x=80, y=250)
        self.CL.mainloop()#inicializacion ventana interfaz

    def eliminar(self):
        self.CL.destroy()
        segunda_ventana()

    def eliminar2(self):
        self.CL.destroy()
        GD_inicio.inicio()

    def eliminar3(self):
        self.CL.destroy()
        analizar.inicio()

    def eliminar4(self):
        self.CL.destroy()
        autenticacion.agregarUsuario()


class Ventana2():
    def __init__(self):
        self.CL2 = Tk()
        self.CL2.geometry("600x300")
        self.CL2.title("PDV nueva era")
        self.CL2.configure(background = "dark blue")
        self.agregar_componentes()
        self.CL2.mainloop()

    def agregar_componentes(self):
            self.total = 0
            self.impuestos = 0
            self.factura = []
            self.T1 = StringVar()#variable para guardar la informacion obtenida en la interfaz
            self.T2 = IntVar()
            self.L2 = Label(self.CL2,text="Id Producto",background= "dark blue",fg = "white").place(x=40, y=50)#campo de informacion
            self.L3 = Label(self.CL2,text="Cantidad",background= "dark blue",fg = "white").place(x=40, y=75)
            self.E1 = Entry(self.CL2,textvariable=self.T1, width=30).place(x=120, y=50)#espacio en blanco
            self.E2 = Entry(self.CL2,textvariable=self.T2, width=30).place(x=120, y=75)
            self.B1 = Button(self.CL2, text="Agregar", width=15, command=self.agregar).place(x=155, y=120)
            self.B3 = Button(self.CL2, text="PAGAR", width=15, command=self.facturar,foreground="white",background="red", font=("", 14)).place(x=200, y=230)
            self.lista = Listbox(self.CL2, width = 35)
            self.lista.place(x=350, y=40)

    def agregar(self):
        a = self.T1.get()
        b = self.T2.get()
        self.lista.delete(0,END)#inicia vacia en cada iteracion
        l1,suma,impuestos, self.factura,base = PV_sumaParcial.busqueda(a,b)
        if base == 1:
            BaseDatos.detalles(a,b,contador)
        for element in l1:
            self.lista.insert(END,element)
        self.total = self.total + suma
        self.impuestos = self.impuestos + impuestos
        self.lista.insert(END,"                                    ")
        self.lista.insert(END,"----------------------------------------")
        self.lista.insert(END,"TOTAL:    $"+str(self.total))
        self.lista.insert(END,"TOTAL+impuesto:   $"+str(self.impuestos))

    def facturar(self):
        self.CL2.destroy()
        PV2.factura(self.factura,contador,self.total,self.impuestos)
        PV_sumaParcial.limpiar()
        ventana_inicial()

        
                  
class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder


def ventana_inicial():
    global contador
    contador = contador + 1
    director = Director()
    builder = ConstructorVentana1()
    director.builder = builder

    
   



                                  
  
    

