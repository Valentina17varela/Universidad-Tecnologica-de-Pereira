from tkinter import *
import sqlite3


factura = []

def busqueda(articulo, cantidad):
    texto = "disponible"
    base = 0
    imprimir = []
    datos = sqlite3.connect('facturas.db')
    cursor = datos.cursor()
    cursor.execute('SELECT Id,Descripcion,Precio,Cantidad,Impuesto FROM Inventario WHERE Id = ? ',(articulo,))
    data = cursor.fetchall()
    if data != []:
        if (data[0][3] - cantidad) >= 0:
            imprimir.append("Id producto: "+str(data[0][0]))
            imprimir.append("Descripcion: "+data[0][1])
            imprimir.append("Precio unitario: "+str(data[0][2]))
            imprimir.append("Cantidad: "+str(cantidad))
            suma = cantidad*data[0][2]
            impuestos = ((data[0][2] * data[0][4]) + data[0][2])*cantidad
            imprimir.append("Precio X Cantidad: $"+str(suma))
            resta = data[0][3] - cantidad
            cursor.execute('UPDATE Inventario SET Cantidad = ? where Id = ?',(resta,articulo))
            datos.commit()
            base = 1
        else:
            texto = "La cantidad del"
            imprimir.append(texto)
            imprimir.append("articulo no esta")
            imprimir.append("disponible")
            suma = 0
            impuestos = 0
    else: 
        texto = "El id no corresponde"
        imprimir.append(texto)
        imprimir.append("a ningun articulo")
        imprimir.append("disponible.")
        suma = 0
        impuestos = 0
    if texto == "disponible":
        factura.append(imprimir)
    return imprimir, suma, impuestos, factura,base

def limpiar():
    global factura
    factura = []