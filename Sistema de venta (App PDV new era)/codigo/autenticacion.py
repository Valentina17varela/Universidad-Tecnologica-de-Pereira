from tkinter import *
import PV_inicio
import main
import sqlite3



class error():
    def __init__(self,texto):
        self.texto = texto
        self.CL = Tk()
        self.CL.geometry("440x300")
        self.CL.title("PDV nueva era")
        self.CL.configure(background = "dark blue")
        self.agregar_componentes()
        self.CL.mainloop()

    def agregar_componentes(self):
        self.L1 = Label(self.CL,text="Bienvenido al sistema de reconocimiento",font=("",14),background= "dark blue",fg = "white").place(x=40, y=40)
        self.L2 = Label(self.CL,text="Por favor introduzca sus datos",font=("",12),background= "dark blue",fg = "white").place(x=80, y=70)
        self.T1 = IntVar()
        self.T2 = StringVar()
        self.L3 = Label(self.CL,text="Documento de identidad",background= "dark blue",fg = "white").place(x=80, y=110)
        self.E1 = Entry(self.CL,textvariable=self.T1, width=30).place(x=90, y=130)
        self.L4 = Label(self.CL,text="Clave",background= "dark blue",fg = "white").place(x=80, y=160)
        self.E2 = Entry(self.CL,textvariable=self.T2, width=30,show="*").place(x=90, y=180)
        self.L5 = Label(self.CL,text=self.texto,background= "dark blue",fg = "red").place(x=80, y=200)
        self.B1 = Button(self.CL, text="Aceptar", width=15, command=self.buscar).place(x=120, y=230)

    def buscar(self):
        a = self.T1.get()
        b = self.T2.get()
        datos = sqlite3.connect('facturas.db')
        cursor = datos.cursor()
        cursor.execute('SELECT Id,Clave FROM Usuarios  WHERE Id = ? ',(a,))
        data = cursor.fetchall()
        if data != []:
            if data[0][1] == b:
                self.CL.destroy()
                PV_inicio.ventana_inicial()
            else:
                texto = "Password incorrecto"
                self.CL.destroy()
                error(texto)
        else:
            texto = "Usuario no encontrado"
            self.CL.destroy()
            error(texto)




class cajero():
    def __init__(self):
        self.CL2 = Tk()
        self.CL2.geometry("440x300")
        self.CL2.title("PDV nueva era")
        self.CL2.configure(background = "dark blue")
        self.agregar_componentes()
        self.CL2.mainloop()

    def agregar_componentes(self):
        self.L1 = Label(self.CL2,text="Bienvenido al sistema de reconocimiento",font=("",14),background= "dark blue",fg = "white").place(x=40, y=40)
        self.L2 = Label(self.CL2,text="Por favor introduzca sus datos",font=("",12),background= "dark blue",fg = "white").place(x=80, y=70)
        self.T1 = IntVar()
        self.T2 = StringVar()
        self.L3 = Label(self.CL2,text="Documento de identidad",background= "dark blue",fg = "white").place(x=80, y=110)
        self.E1 = Entry(self.CL2,textvariable=self.T1, width=30).place(x=90, y=130)
        self.L4 = Label(self.CL2,text="Clave",background= "dark blue",fg = "white").place(x=80, y=160)
        self.E2 = Entry(self.CL2,textvariable=self.T2, width=30,show="*").place(x=90, y=180)
        self.B1 = Button(self.CL2, text="Aceptar", width=15, command=self.buscar).place(x=120, y=230)

    def buscar(self):
        a = self.T1.get()
        b = self.T2.get()
        datos = sqlite3.connect('facturas.db')
        cursor = datos.cursor()
        cursor.execute('SELECT Id,Clave FROM Usuarios  WHERE Id = ? ',(a,))
        data = cursor.fetchall()
        if data != []:
            if (data[0][1]) == b:
                self.CL2.destroy()
                PV_inicio.ventana_inicial()
            else:
                texto = "Password incorrecto"
                self.CL2.destroy()
                error(texto)
        else:
            texto = "Usuario no encontrado"
            self.CL2.destroy()
            error(texto)

            


class agregarUsuario():
    def __init__(self):
        self.CL2 = Tk()
        self.CL2.geometry("440x300")
        self.CL2.title("PDV nueva era")
        self.CL2.configure(background = "dark blue")
        self.agregar_componentes()
        self.CL2.mainloop()

    def agregar_componentes(self):
        self.L1 = Label(self.CL2,text="Añadir nuevo usuario",font=("",14),background= "dark blue",fg = "white").place(x=40, y=40)
        self.L2 = Label(self.CL2,text="Por favor introduzca sus datos",font=("",12),background= "dark blue",fg = "white").place(x=80, y=70)
        self.T1 = IntVar()
        self.T2 = StringVar()
        self.L3 = Label(self.CL2,text="Documento de identidad",background= "dark blue",fg = "white").place(x=80, y=110)
        self.E1 = Entry(self.CL2,textvariable=self.T1, width=30).place(x=90, y=130)
        self.L4 = Label(self.CL2,text="Clave",background= "dark blue",fg = "white").place(x=80, y=160)
        self.E2 = Entry(self.CL2,textvariable=self.T2, width=30,show="*").place(x=90, y=180)
        self.B1 = Button(self.CL2, text="Aceptar", width=15, command=self.agregar).place(x=120, y=230)

    def agregar(self):
        a = self.T1.get()
        b = self.T2.get()
        datos = sqlite3.connect('facturas.db')
        cursor = datos.cursor()
        cursor.execute("INSERT INTO Usuarios VALUES(?,?)",(a,b))
        datos.commit()
        self.CL2.destroy()
        main.aplicativo()



   