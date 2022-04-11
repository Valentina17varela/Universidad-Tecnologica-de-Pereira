from tkinter import *
import sqlite3

class Ventana(object):
    def __init__(self):
	    self.valor = None

    def agregar(self):
	    print(self.valor)


class General(Ventana): 
    def __init__(self):
        self.CL = Tk()
        self.CL.geometry("460x260")
        self.CL.title("Facturas General")
        self.CL.configure(background = "dark blue")
        self.lista = Listbox(self.CL, width = 60)
        self.lista.place(x=50, y=40)
        self.agregar()
        self.CL.mainloop()#inicializacion ventana interfaz

    def agregar(self):
        self.lista.insert(END,"     No Factura             Total                 +impuestos               Metodo")
        datos = sqlite3.connect('facturas.db')
        cursor = datos.cursor()
        cursor.execute('SELECT No_Factura,Total,Total_impuestos,Metodo FROM Facturas')
        data = cursor.fetchall()
        for element in data:
            self.lista.insert(END,"             "+str(element[0])+"                     "+str(element[1])+"                     "+str(element[2])+"                     "+str(element[3]))

class Detalles(Ventana): 
    def __init__(self):
        self.CL = Tk()
        self.CL.geometry("460x260")
        self.CL.title("Facturas Detalle")
        self.CL.configure(background = "dark blue")
        self.T1 = IntVar()
        self.L1 = Label(self.CL,text="No. factura",background= "dark blue",fg = "white").place(x=40, y=20)
        self.E1 = Entry(self.CL,textvariable=self.T1, width=15).place(x=120, y=20)
        self.B1 = Button(self.CL, text="Buscar", width=20, command=self.agregar).place(x=240, y=20)
        self.lista = Listbox(self.CL, width = 60)
        self.lista.place(x=50, y=70)
        self.CL.mainloop()#inicializacion ventana interfaz

    def agregar(self):
        a = self.T1.get()
        self.lista.delete(0,END)
        self.lista.insert(END,"     Id producto          Cantidad")
        datos = sqlite3.connect('facturas.db')
        cursor = datos.cursor()
        cursor.execute('SELECT Id_producto,Cantidad FROM Detalles WHERE No_Factura = ? ',(a,))
        data = cursor.fetchall()
        for element in data:
            self.lista.insert(END,"          "+str(element[0])+"                  "+str(element[1]))
        self.lista.insert(END,"__________________________________________________________________________")
        cursor.execute('SELECT Total,Total_impuestos,Metodo FROM Facturas WHERE No_Factura = ? ', (a,))
        data = cursor.fetchall()
        self.lista.insert(END,"Total: "+str(data[0][0])+"     +impuestos: "+str(data[0][1])+"    Metodo: "+str(data[0][2]))
        
class Caja(Ventana): 
    def __init__(self):
        self.CL = Tk()
        self.CL.geometry("280x300")
        self.CL.title("Caja")
        self.CL.configure(background = "dark blue")
        self.L1 = Label(self.CL,text="Dinero en la caja",background= "dark blue",fg = "white",font=("", 12)).place(x=40, y=20)
        fic = open("caja.txt", "r")
        lista = list(fic)
        valor = float(lista[0])
        self.lista = Listbox(self.CL, width = 30)
        self.lista.place(x=50, y=70)
        self.lista.insert(END,str(valor))
        self.CL.mainloop()#inicializacion ventana interfaz

class Inventario(Ventana): 
    def __init__(self):
        self.CL = Tk()
        self.CL.geometry("510x260")
        self.CL.title("Inventario")
        self.CL.configure(background = "dark blue")
        self.lista = Listbox(self.CL, width = 70)
        self.lista.place(x=50, y=40)
        self.agregar()
        self.CL.mainloop()#inicializacion ventana interfaz

    def agregar(self):
        self.lista.insert(END,"     Id             Descripcion            Precio             Cantidad                Impuesto")
        datos = sqlite3.connect('facturas.db')
        cursor = datos.cursor()
        cursor.execute('SELECT Id,Descripcion,Precio,Cantidad,Impuesto FROM Inventario')
        data = cursor.fetchall()
        for element in data:
            self.lista.insert(END,str(element[0])+"               "+str(element[1])+"                  "+str(element[2])+"                     "+str(element[3])+"                     "+str(element[4]))


class Factoria(object):
    def get_ventana(self,valor):
        if valor == 1:
            General()
        elif valor == 2:
            Detalles()
        elif valor == 3:
            Caja()
        else:
            Inventario()


def inicio(valor):
	mi_factoria = Factoria()
	persona = mi_factoria.get_ventana(valor)
