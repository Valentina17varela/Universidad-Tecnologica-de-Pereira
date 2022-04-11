import autenticacion
import BaseDatos
import caja

def aplicativo():
    BaseDatos.baseF()
    BaseDatos.baseInv()
    caja.inicializar(1200000)
    autenticacion.cajero()

if __name__ == "__main__":
    aplicativo()
    