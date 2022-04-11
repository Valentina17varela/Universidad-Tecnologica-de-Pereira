from tkinter import *
import sqlite3
import PV_inicio
import caja

buscar = []

class ventana():
    def __init__(self):
        self.buscar = []
        self.CL = Tk()
        self.CL.geometry("600x300")
        self.CL.title("PDV nueva era")
        self.CL.configure(background = "dark blue")
        self.agregar_componentes()
        self.CL.mainloop()

    def agregar_componentes(self):
            self.numero = 0
            self.factura = []
            self.T1 = IntVar()
            self.T2 = IntVar()
            self.T3 = IntVar()
            self.L1 = Label(self.CL,text="No. factura",background= "dark blue",fg = "white").place(x=40, y=50)
            self.E1 = Entry(self.CL,textvariable=self.T1, width=30).place(x=50, y=70)
            self.L2 = Label(self.CL,text="Id Producto",background= "dark blue",fg = "white").place(x=40, y=100)
            self.E2 = Entry(self.CL,textvariable=self.T2, width=30).place(x=50, y=120)
            self.L3 = Label(self.CL,text="Cantidad",background= "dark blue",fg = "white").place(x=40, y=150)
            self.E2 = Entry(self.CL,textvariable=self.T3, width=30).place(x=50, y=170)
            self.B1 = Button(self.CL, text="Agregar", width=15, command=self.agregar).place(x=80, y=210)
            self.B3 = Button(self.CL, text="DEVOLVER", width=15, command=self.devolver,foreground="white",background="red", font=("", 14)).place(x=370, y=220)
            self.lista = Listbox(self.CL, width = 35)
            self.lista.place(x=350, y=40)
            self.lista.insert(END,"ID                CANTIDAD")


    def agregar(self):
        self.a = self.T1.get()
        self.b = self.T2.get()
        self.c = self.T3.get()
        self.lista.insert(END,str(self.b)+"         "+str(self.c))
        self.buscar.append([self.a,self.b,self.c])

    def devolver(self):
        dinero = 0
        dinero2= 0
        add = 0
        self.lista.delete(0,END)#inicia vacia en cada iteracion
        datos = sqlite3.connect('facturas.db')
        cursor = datos.cursor()
        cursor.execute('SELECT Id_producto,Cantidad FROM Detalles WHERE No_Factura = ? ',(self.buscar[0][0],))
        data2 = cursor.fetchall()
        if data2 == []:
            texto = "Factura no encontrada en el sistema"
        else:
            for i in range(len(self.buscar)):
                for element in data2:
                    ID = self.buscar[i][1]
                    CANT = self.buscar[i][2]
                    cursor.execute('SELECT Precio,Cantidad,Impuesto FROM Inventario WHERE Id = ? ',(ID,))
                    data = cursor.fetchall()
                    dinero = dinero + (((data[0][0] * data[0][2]) + data[0][0])*CANT)
                    dinero2 = dinero2 + (data[0][0]*CANT)
                    add = data[0][1] + CANT
                    cursor.execute('UPDATE Inventario SET Cantidad = ? where Id = ?',(add,ID))
                    rest = element[1] - CANT
                    cursor.execute('UPDATE Detalles SET Cantidad = ? where Id_producto = ?',(rest,ID))
                    cursor.execute('SELECT Total,Total_impuestos FROM Facturas WHERE No_Factura = ? ',(self.buscar[i][0],))
                    data2 = cursor.fetchall()
                    nuevoTotal = data2[0][0] - dinero2
                    nuevoImpuestos = data2[0][1] - dinero
                    if nuevoImpuestos <= 0:
                        cursor.execute('DELETE FROM Facturas where No_Factura = ?',(self.buscar[i][0],))
                    else:
                        cursor.execute('UPDATE Facturas SET Total = ?,Total_impuestos = ? where No_Factura = ?',(nuevoTotal,nuevoImpuestos,self.buscar[i][0]))
                    datos.commit()
                    caja.restar(dinero)
                    texto = "La cantidad a devolver es de "+str(dinero)
                    self.CL.destroy()
        finalizar_devolucion(texto)


class finalizar_devolucion():
    def __init__(self,texto):
        self.CL = Tk()
        self.CL.geometry("340x80")
        self.CL.title("PDV nueva era")
        self.CL.configure(background = "dark blue")
        self.L2 = Label(self.CL,text=texto,background= "dark blue",fg = "white").place(x=40, y=20)
        self.CL.mainloop() 


def inicio():
    ventana()
    PV_inicio.ventana_inicial()