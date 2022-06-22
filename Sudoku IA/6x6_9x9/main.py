from time import time

retorno = 0

class Sudoku():#Agente observador
    def __init__(self,nombre,dimension,tablero):
        self.nombre = nombre
        self.dimension = dimension
        self.tablero = tablero
        
        
    def impresion(self):#imprimir tablero
        if self.dimension == 9:#9x9
            for index,fila in enumerate(self.tablero):
                linea = ""
                if index == 3 or index == 6:
                    print("--------------------")
                for i, columna in enumerate(fila):
                    if i == 3 or i == 6:
                        linea += "|"
                    linea += " "+str(self.tablero[index][i])
                print(linea)
        if self.dimension == 6:#6x6
            for index,fila in enumerate(self.tablero):
                linea = ""
                if index == 2 or index == 4:
                    print("--------------------")
                for i, columna in enumerate(fila):
                    if i == 3 or i == 6:
                        linea += "|"
                    linea += " "+str(self.tablero[index][i])
                print(linea)
                
                
    def solucion(self,mensaje,archivo):#notificar la solucion y escribirla en un archivo .txt
        print(mensaje)
        arch=open("6x6_9x9/"+self.nombre+"Solucion.txt","w") 
        if archivo != "-1":
            for element in archivo:
                for index in element:
                    arch.write(str(index)+" ")
                arch.write("\n")
        else:
            arch.write(archivo)
        arch.close() 
                


class Cuadricula:#Entorno observador
    def __init__(self):
        self.observers = []

    def add_observers(self, observer):#añadir observadores
        self.observers.append(observer)
        return self

    def remove_observer(self, observer):#remover observadores
        self.observers.remove(observer)
        return self

    def notificar(self, msg,archivo): #notificacion solucion sudoku
        for observer in self.observers:
            observer.solucion(msg,archivo)
                   


def encontrarCasilla(arr, l,dim):#retorna la casilla donde todavia se pueden hacer movimientos
    for row in range(dim):
        for col in range(dim):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False
 
 

def fila(arr, row, num,dim):#indica si el numero ya se encuentra en una fila
    for i in range(dim):
        if(arr[row][i] == num):
            return True
    return False
 
 

def columna(arr, col, num,dim):#indica si el numero ya se encuentra en una columna
    for i in range(dim):
        if(arr[i][col] == num):
            return True
    return False
 


def recuadro(arr, row, col, num,dim):#indica si el numero ya se encuentra en un recuadro   
    if dim == 6:
        primera = 2
        segunda = 3
    if dim == 9:
        primera = 3
        segunda = 3
        
    for i in range(primera):
        for j in range(segunda):
            if(arr[i + row][j + col] == num):
                return True
    return False
 


def movimientoLegal(arr, row, col, num,dimension): #comprueba que el numero a poner no rompe ninguna regla
    if dimension == 9:
        return not fila(arr, row, num,dimension) and not columna(arr, col, num,dimension) and not recuadro(arr, row - row % 3,col - col % 3, num,dimension)
    if dimension == 6:
        return not fila(arr, row, num,dimension) and not columna(arr, col, num,dimension) and not recuadro(arr, row - row % 2,col - col % 3, num,dimension)
 


def SolverSudoku(arr,dimension):#funcion de backtracking recursivo
    global retorno
    if retorno >= 200:
        return False
        
    l =[0, 0]
     
    if(not encontrarCasilla(arr, l,dimension)):
        return True
     
    row = l[0]
    col = l[1]
     
    for num in range(1, dimension+1):#rango de numeros

        if(movimientoLegal(arr,row, col, num,dimension)):
            arr[row][col]= num

            if(SolverSudoku(arr,dimension)):
                return True

            arr[row][col] = 0 #si el movimiento no funciona se devuelve

    return False



if __name__ == "__main__":
    #Lectura archivo
    nombre = "sudoku9" #poner en la variable el archivo que se quiere resolver ej: nombre = "sudoku6"
    f = open ("6x6_9x9/"+nombre+'.txt','r')
    dimension = f.readline() #dimension del tablero
    dimension = int(dimension) 
    inicial = f.readlines() #contenido del tablero
    tablero = [list(x.strip()) for x in inicial]
    f.close()
    
    #quitar los espacios del tablero y convertirlos a numeros
    for index,element in enumerate(tablero):
        cadena = [i for i in element if i != ' ']
        for ind,i in enumerate(cadena):
            cadena[ind] = int(i)
        tablero[index] = cadena

    #estadisticas: inicio
    inicio = time()
    
    #agente sudoku solver
    sudoku = Sudoku(nombre,dimension,tablero)
    cuadricula = Cuadricula()
    cuadricula.add_observers(sudoku)#agente observador
    
    #tablero inicial
    print("Sudoku a resolver")
    sudoku.impresion() 
    
    #comprobacion si tiene solucion
    if (SolverSudoku(sudoku.tablero,dimension)):#backtracking
        cuadricula.notificar("\nLa solucion encontrada es: ",sudoku.tablero)
        sudoku.impresion() 
    else:
        cuadricula.notificar("\nNo se encontro una solucion valida","-1")
        
    
    #estadisticas: final
    final = time()
    
    print("\nEl algoritmo de Backtracking ha resuelto el problema en ",final-inicio)
