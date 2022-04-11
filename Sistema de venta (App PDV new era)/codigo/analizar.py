from tkinter import *
import PV_inicio
import analizar2

class ventana():
    def __init__(self):
        self.CL = Tk()
        self.CL.geometry("400x350")
        self.CL.title("PDV nueva era")
        self.CL.configure(background = "dark blue")
        self.B1 = Button(self.CL, text="Facturas en general", width=20, command=self.leerDato1, font=("", 14)).place(x=80, y=70)
        self.B2 = Button(self.CL, text="Detallar factura", width=20, command=self.leerDato2, font=("", 14)).place(x=80, y=130)
        self.B3 = Button(self.CL, text="Revisar caja", width=20, command=self.leerDato3, font=("", 14)).place(x=80, y=190)
        self.B3 = Button(self.CL, text="Revisar inventario", width=20, command=self.leerDato4, font=("", 14)).place(x=80, y=250)
        self.CL.mainloop()#inicializacion ventana interfaz

    def leerDato1(self):
        self.CL.destroy()
        analizar2.inicio(1)

    def leerDato2(self):
        self.CL.destroy()
        analizar2.inicio(2)

    def leerDato3(self):
        self.CL.destroy()
        analizar2.inicio(3)

    def leerDato4(self):
        self.CL.destroy()
        analizar2.inicio(4)


def inicio():
    ventana()
    PV_inicio.ventana_inicial()