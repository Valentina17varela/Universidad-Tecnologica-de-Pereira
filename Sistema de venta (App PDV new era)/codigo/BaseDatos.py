import sqlite3

def baseF():
    datos = sqlite3.connect('facturas.db')
    cursor = datos.cursor()#para realizar consultas
    cursor.execute("DROP TABLE IF EXISTS Facturas")
    cursor.execute("DROP TABLE IF EXISTS Detalles")
    cursor.execute("CREATE TABLE Facturas(No_Factura integer PRIMARY KEY, Total float, Total_impuestos float, Metodo text)")
    cursor.execute("CREATE TABLE Detalles(Id_producto integer,Cantidad integer,No_Factura integer)")

def insertarF(numero,total,impuestos,metodo):
    datos = sqlite3.connect('facturas.db')
    cursor = datos.cursor()#para realizar consultas
    cursor.execute("INSERT INTO Facturas VALUES(?,?,?,?)",(numero,total,impuestos,metodo))
    datos.commit()


def detalles(idC,cantidad,factura):
    datos = sqlite3.connect('facturas.db')
    cursor = datos.cursor()
    cursor.execute("INSERT INTO Detalles VALUES(?,?,?)",(idC,cantidad,factura))
    datos.commit()
    

def baseInv():
    datos = sqlite3.connect('facturas.db')
    cursor = datos.cursor()#para realizar consultas
    cursor.execute("DROP TABLE IF EXISTS Inventario")
    cursor.execute("CREATE TABLE Inventario(Id integer PRIMARY KEY, Descripcion text, Precio float,Cantidad integer, Impuesto float)")
    cursor.execute("INSERT INTO Inventario VALUES(?,?,?,?,?)",(102030,"pan     ",500,5,0.2))
    cursor.execute("INSERT INTO Inventario VALUES(?,?,?,?,?)",(123456,"leche  ",3500,3,0.015))
    cursor.execute("INSERT INTO Inventario VALUES(?,?,?,?,?)",(111111,"huevos",500,10,0.03))
    cursor.execute("INSERT INTO Inventario VALUES(?,?,?,?,?)",(785412,"arroz ",2500,6,0.05))
    cursor.execute("INSERT INTO Inventario VALUES(?,?,?,?,?)",(565656,"queso ",5100,10,0.02))
    cursor.execute("INSERT INTO Inventario VALUES(?,?,?,?,?)",(963751,"sal     ",1300,5,0.01))
    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='Usuarios'")
    data = cursor.fetchall()
    if data[0][0] == 0:
        cursor.execute("CREATE TABLE Usuarios(Id integer PRIMARY KEY, Clave text)")
        cursor.execute("INSERT INTO Usuarios VALUES(?,?)",(1004739145,"Valentina17"))
        cursor.execute("INSERT INTO Usuarios VALUES(?,?)",(1005896452,"32Mario2001"))
        cursor.execute("INSERT INTO Usuarios VALUES(?,?)",(1002569478,"Programacion4"))
        cursor.execute("INSERT INTO Usuarios VALUES(?,?)",(1005698521,"ServicioEspecial123"))
    datos.commit()


