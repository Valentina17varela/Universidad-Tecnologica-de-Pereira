from tkinter import *
from tkinter import ttk
import PV_inicio
import BaseDatos
import sqlite3
import caja


class recibo():
    def __init__(self,info,contador,total,impuestos):
        self.info = info
        self.contador = contador
        self.total = total
        self.impuestos = impuestos
        self.CL2 = Tk()
        self.CL2.geometry("480x380")
        self.CL2.title("PDV nueva era")
        self.CL2.configure(background = "dark blue")
        self.agregar_componentes()
        self.CL2.mainloop()

    def agregar_componentes(self):
            self.L2 = Label(self.CL2,text="Recibo",background= "dark blue",fg = "white").place(x=40, y=20)#campo de informacion
            self.B3 = Button(self.CL2, text="ACEPTAR", width=15, command=self.regresar,foreground="white",background="red", font=("", 14)).place(x=142, y=320)
            self.desplazamiento = Scrollbar(self.CL2)
            self.lista = Listbox(self.CL2, width = 60,yscrollcommand=self.desplazamiento.set)
            self.desplazamiento.config(command=self.lista.yview)
            self.desplazamiento.pack(side=RIGHT,fill=Y)
            self.lista.place(x=40, y=50)
            self.lista.insert(END,"No.Factura "+str(self.contador))
            for element in self.info:
                for i in element:
                    self.lista.insert(END,i)
                self.lista.insert(END,"                                    ")
            self.lista.insert(END,"Total: $"+str(self.total))
            self.lista.insert(END,"Total+imp: $"+str(self.impuestos))
            self.T1 = IntVar()
            self.L2 = Label(self.CL2,text="Total recibido: ",background= "dark blue",fg = "white").place(x=50, y=230)#campo de informacion
            self.E1 = Entry(self.CL2,textvariable=self.T1, width=30).place(x=140, y=230)#espacio en blanco
            self.L3 = Label(self.CL2,text="Metodo de pago ",background= "dark blue",fg = "white").place(x=50, y=250)
            self.selected = IntVar()
            self.rad1 = Radiobutton(self.CL2,text='Efectivo', value=1, variable=self.selected).place(x=150, y=280)
            self.rad2 = Radiobutton(self.CL2,text='Tarjeta', value=2, variable=self.selected).place(x=240, y=280)

    def regresar(self):
        texto = ""
        a = self.T1.get()
        b = self.selected.get()
        for element in self.info:
            texto = texto + str(element)
        if b == 1:
            devuelta(a,self.impuestos,self.CL2,self.contador,self.total)
        else:
            tarjeta(self.CL2)
            BaseDatos.insertarF(self.contador,self.total,self.impuestos,"tarjeta")


class tarjeta():
    def __init__(self,ventana):
        self.ventana = ventana
        self.CL = Tk()
        self.CL.geometry("420x360")
        self.CL.title("PDV nueva era")
        self.CL.configure(background = "dark blue")
        self.operacion()
        self.CL.mainloop()   

    def operacion(self):
        self.L1 = Label(self.CL,text="Naturaleza de la cuenta ",background= "dark blue",fg = "white").place(x=50, y=50)
        self.selected = IntVar()
        self.rad1 = Radiobutton(self.CL,text='Debito', value=1, variable=self.selected).place(x=140, y=80)
        self.rad2 = Radiobutton(self.CL,text='Credito', value=2, variable=self.selected).place(x=230, y=80)
        self.L2 = Label(self.CL,text="Documento",background= "dark blue",fg = "white").place(x=120, y=120)
        self.E1 = Entry(self.CL,textvariable="", width=30).place(x=140, y=140)
        self.L3 = Label(self.CL,text="Clave",background= "dark blue",fg = "white").place(x=120, y=180)
        self.E2 = Entry(self.CL,textvariable="", width=30, show="*").place(x=140, y=200)
        self.B3 = Button(self.CL, text="ACEPTAR", width=12, command=self.nueva,foreground="white",background="red", font=("", 14)).place(x=150, y=250)

    def nueva(self):
        self.ventana.destroy()
        self.CL.destroy()
        self.CL2 = Tk()
        self.CL2.geometry("340x80")
        self.CL2.title("PDV nueva era")
        self.CL2.configure(background = "dark blue")
        texto = "Transaccion aceptada"
        self.L2 = Label(self.CL2,text=texto,background= "dark blue",fg = "white").place(x=40, y=20)


class devuelta():
    def __init__(self,pago,total,ventana,contador,total2):
        self.impuestos = total
        self.devuelta = pago - total
        self.ventana = ventana
        self.contador = contador
        self.total2 = total2
        self.CL = Tk()
        self.CL.geometry("340x80")
        self.CL.title("PDV nueva era")
        self.CL.configure(background = "dark blue")
        self.operacion()
        self.CL.mainloop()

    def operacion(self):
        if self.devuelta < 0:
            texto = "La cantidad es insuficiente, intentelo de nuevo."
        else:
            
            self.ventana.destroy()
            texto = "El cambio es de: $" +str(self.devuelta)
            BaseDatos.insertarF(self.contador,self.total2,self.impuestos,"efectivo")
            caja.sumar(self.impuestos)
        self.L2 = Label(self.CL,text=texto,background= "dark blue",fg = "white").place(x=40, y=20)#campo de informacion


def factura(info,contador,total,impuestos): 
    imprimir = recibo(info,contador,total,impuestos)


    