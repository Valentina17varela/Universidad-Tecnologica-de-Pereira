def inicializar(valor):
    fic = open("caja.txt", "w")
    fic.write(str(valor))
    fic.close()

def sumar(venta):
    fic = open("caja.txt", "r")
    lista = list(fic)
    valor = float(lista[0])
    valor = valor + venta
    fic.close()
    fic = open("caja.txt", "w")
    fic.write(str(valor))
    fic.close()

def restar(venta):
    fic = open("caja.txt", "r")
    lista = list(fic)
    valor = float(lista[0])
    valor = valor - venta
    fic.close()
    fic = open("caja.txt", "w")
    fic.write(str(valor))
    fic.close()


