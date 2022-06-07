import sys
import os
import time
import tabulate
from ui import user_interface
from api import data_collector


def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def run():
    borrarPantalla()
    option =user_interface.menu_principal()
    if option == 1:
        limite_registros,Departamento =user_interface.menu_datos()
        borrarPantalla()
        tabla = data_collector.consulta_datos(limite_registros,Departamento)
        print(tabulate.tabulate(tabla,headers=['ciudad','departamento','edad','tipo','estado'
                                               ,'pais de procedencia'], tablefmt='fancy_grid'))
        input("continuar: ")
        run()
    elif option == 2:
        sys.exit()
    else:
        print("La opcion no es valida, intentelo nuevamente")
        time.sleep(3)
        run()


if __name__ == '__main__':
    run()