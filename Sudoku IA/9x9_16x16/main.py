import  random
import sys
import numpy as np
from itertools import combinations
from inferenciaAC3 import *



class sudokuCSP(CSP):#agente sudoku
    def __init__(self, variables, domains, neighbors, constraints,nombre):
        super().__init__(variables, domains, neighbors, constraints)
        self.solucion = 1
        self.nombre = nombre
        self.init_assignment = {}

    def L3D(self):
        CSP.init_curr_domains(self)

        for i in range(dimension):
            row = [str(i) + ',' + str(col) for col in range(dimension)]
            for comb3 in combinations(row,3):
                if set(self.curr_domains[comb3[0]])&set(self.curr_domains[comb3[1]])&set(self.curr_domains[comb3[2]]):
                    u = set(self.curr_domains[comb3[0]])|set(self.curr_domains[comb3[1]])|set(self.curr_domains[comb3[2]])
                    if len(u) == 3:
                        for r in (set(row) - set(comb3)):
                            self.curr_domains[str(r)] = list(set(self.curr_domains[str(r)]) - u)

        for j in range(dimension):
            col = [str(row) + ',' + str(j) for row in range(dimension)]
            for comb3 in combinations(col, 3):
                if set(self.curr_domains[comb3[0]]) & set(self.curr_domains[comb3[1]]) & set(
                        self.curr_domains[comb3[2]]):
                    u = set(self.curr_domains[comb3[0]]) | set(self.curr_domains[comb3[1]]) | set(
                        self.curr_domains[comb3[2]])
                    if len(u) == 3:
                        for r in (set(col) - set(comb3)):
                            self.curr_domains[str(r)] = list(set(self.curr_domains[str(r)]) - u)


    def display(self, own="revise", assignment={}, removals=[], curr_domains={}):#impresion
        print(" ")
        hstr = ""
        bstr = ""
        strr="------+"
        for i in range(dimension_sqrt):
            if not i ==dimension_sqrt-1:
                strr+="------+"
            else:
                strr+="------"

        for l in range(self.nassigns + 1):
            hstr += "-"
            bstr += " "

        if own == "Initial state":
            print(own, '(num of assign:', len(assignment), '):')
        elif own == "Result, Goal reached!":
            print("Solucion encontrada")

        
        if assignment and (own == "Result, Goal reached!"):
            arch=open("9x9_16x16/"+self.nombre+"Solucion"+str(self.solucion)+".txt","w") 
            print(strr)

            for row in range(dimension):

                for col in range(dimension):
                    if str(row) + ',' + str(col) in assignment.keys():
                        if str(row) + ',' + str(col) in self.init_assignment.keys():
                            print('\033[1m'+str(assignment[str(row) + ',' + str(col)])+'\033[0m', '', end="")
                            arch.write(str(assignment[str(row) + ',' + str(col)])+" ")
                        else:
                            print(assignment[str(row) + ',' + str(col)], '', end="")
                            arch.write(str(assignment[str(row) + ',' + str(col)])+' ')
                            
                    else:
                        print('.', '', end="")

                    if (col + 1) % dimension_sqrt == 0 and col < dimension-1:
                        print('|', '',  end="")

                print("")
                arch.write("\n")

                if (row + 1) % dimension_sqrt == 0:
                    print(strr)
            arch.close() 
            self.solucion += 1
        elif own == "sinSolucion":
            arch=open("9x9_16x16/"+self.nombre+"Solucion"+str(self.solucion)+".txt","w") 
            arch.write("-1")
            arch.close()
            




def input_file(nombre):#Lectura del archivo
    try:
        f = open("9x9_16x16/"+nombre+".txt", 'r')
        dimension = f.readline()
        fline = f.readlines()
        f.close()
        return fline,int(dimension),nombre

    except FileNotFoundError:
        print("Archivo no encontrado")




def init_sudoku(fline):

    digit=[]
    sdk=np.zeros((1,dimension*dimension))
    line=[]

    for i in range(len(fline)):
        fline[i] = fline[i].split()
        for j in fline[i]:
            digit.append(int(j))

    for i in range(len(digit)):
        sdk[0,i]=digit[i]

    sudoku=np.reshape(sdk,(dimension,dimension))
    sudoku=sudoku.astype(int)
    print("Sudoku a resolver")
    print(sudoku)

    csgraph = {}
    do=[]
    domains={}
    vertex={}
    row=[]
    neighbor={}

    for i in range(dimension):
        do.append(i+1)
 

    for i in range(0,dimension):
        for j in range(0,dimension):
            vertex[str(i)+","+str(j)]=0
            domains[str(i)+","+str(j)] = []
            neighbor[str(i)+","+str(j)] = []

    for x in range(dimension):
        for y in range(dimension):

            for col in range(dimension):
                if not [x,col]==[x,y]:
                    neighbor[str(x) + "," + str(y)].append(str(x)+","+str(col))


            for row in range(dimension):
                if not [row,y]==[x,y]:
                    neighbor[str(x) + "," + str(y)].append(str(row) + "," + str(y))

            for a in range(dimension_sqrt):
                for b in range(dimension_sqrt):
                    j=a+dimension_sqrt*(x//dimension_sqrt)
                    k=b+dimension_sqrt*(y//dimension_sqrt)
                    if not [j,k]==[x,y]:
                        neighbor[str(x) + "," + str(y)].append(str(j) + "," + str(k))



    known={}
    for i in range(dimension):
        for j in range(dimension):
            if not sudoku[i,j]==0:
                domains[str(i)+","+str(j)].append(sudoku[i,j])
                known[str(i)+","+str(j)]=sudoku[i,j]
            else:
                domains[str(i)+","+str(j)]=do
 
    csgraph["domains"] = domains
    csgraph["vertex"] = vertex
    csgraph["neighbors"] = neighbor

    return csgraph




def sudoku_constraints(A, a, B, b):
    """Constraint is satisfied return true"""
    return a != b





if __name__ =="__main__":
    fline,dimension,nombre = input_file("sudoku16")#archivo de lectura
    dimension_sqrt=int(dimension**0.5)
    csgraph=init_sudoku(fline) #sudoku a resolver
    sudokucsp = sudokuCSP(csgraph["vertex"], csgraph["domains"], csgraph["neighbors"], sudoku_constraints,nombre)
    sudokucsp.init_assignment = sudokucsp.first_assignment()
    AC3(sudokucsp) #inferencia AC#
    
    if sudokucsp.goal_test(sudokucsp.first_assignment()):
        print("\nAC3 encontro la solucion\n")
        print("system exit!")
        sys.exit(0)

    sudokucsp.L3D()

    sudokucsp.init_assignment = sudokucsp.first_assignment()

    backtracking_search(sudokucsp, mrv_degree, lcv, mac) #backtracking
    

