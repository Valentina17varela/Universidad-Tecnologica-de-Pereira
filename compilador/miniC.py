from cast import *
from cparser import *
from checker import *
from clex import Lexer
from model import *
from topdown import sintactico
from interpretador.calculator import inicio
from topdown import *
from interpreter import *
from tabulate import tabulate


if __name__ == '__main__':
	
	while True:
		try:
			text = input('$ ')

		except KeyboardInterrupt:
			break

		print("\n\nCOMPILADOR MINI-C\n")
		print("1. Analisis sintactico --> AST\n")
		print("2. Analisis semantico --> Tabla de simbolos\n")
		print("3. Analisis Lexico\n")
		print("4. Interprete\n\n")
		opcion = int(input("Opcion: "))

		if opcion == 1:
			sintactico(text)
		elif opcion == 2:
			l = Lexer()
			symTable = Symtab()
			for tok in l.tokenize(text):
				symTable.add(str(tok.type),str(tok.value))
			print(symTable.entries)
			print("\n\nTabla de simbolos\n")
			print(tabulate(symTable.entries,headers=symTable.entries.keys(),tablefmt='fancy_grid'))
		elif opcion == 3:
			l = Lexer()
			for tok in l.tokenize(text):
				print(tok)
		elif opcion == 4:
			inicio(text)
		else:
			print("Opcion no valida")





		

    

    

    