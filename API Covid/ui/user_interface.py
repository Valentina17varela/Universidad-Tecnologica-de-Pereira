def menu_principal():
    print("""
    --------------------------------------------------------------------------------------------------------------
     |                                      CONSULTA DE DATOS COVID-19                                           |
    --------------------------------------------------------------------------------------------------------------
     |    Bienvenido ,que desea realizar:                                                                        |
     |                                                                                                           |
     |   [1] Consultar reporte de casos de covid-19                                                              |
     |   [2] Salir                                                                                               |
     |                                                                                                           | 
     -------------------------------------------------------------------------------------------------------------
    """)
    op=int(input("opcion: "))
    return op

def menu_datos():
    print(""""
                                          REPORTE DE CASOS DE COVID-19
         
         Ingrese los datos que desea conocer\n
    """)
    limite = int(input("         * Limite de registros: "))
    departamento = input("         * Departamento: ").capitalize()
    return limite,departamento