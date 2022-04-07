from queue import Queue
from tabulate import tabulate
import pandas as pd
import sys

'''
Algoritmo de despacho FIFO

Juan Esteban Corrales
Valentina varela Alzate

Desarrollar un algoritmo FIFO de reemplazo de páginas, se debe permitir el ingreso de una secuencia de mínimo 12 
caracteres separadas por coma, e ingresar n cantidades de módulos de memoria, al final se debe visualizar el 
resultado por medio de una tabla.
'''

#Algoritmo FIFO
def pageFaults(pages, n, capacity):
	
	# To represent set of current pages.
	s = set()
 
	# To store the pages in FIFO manner
	indexes = Queue()
 
	#lista para guardar los resultados que se mostraran en la tabla
	info = []
 
	#lista para guardar las posiciones de los fallos
	fallos = [""] * n

	# Start from initial page
	page_faults = 0
	for i in range(n):
		
		# Check if the set can hold
		# more pages
		if (len(s) < capacity):
			
			# Insert it into set if not present
			# already which represents page fault
			if (pages[i] not in s):
				s.add(pages[i])

				# increment page fault
				page_faults += 1
				fallos[i] = "F"

				# Push the current page into
				# the queue
				indexes.put(pages[i])


		# If the set is full then need to perform FIFO
		# i.e. remove the first page of the queue from
		# set and queue both and insert the current page
		else:
			
			# Check if current page is not
			# already present in the set
			if (pages[i] not in s):
				
				# Pop the first page from the queue
				val = indexes.queue[0]

				indexes.get()

				# Remove the indexes page
				s.remove(val)
    			

				# insert the current page
				s.add(pages[i])

				# push the current page into
				# the queue
				indexes.put(pages[i])

				# Increment page faults
				page_faults += 1
				fallos[i] = "F"

		tabla = []
		for index in s:
			tabla.append(index)
		tabla.append(fallos[i])
		info.append(tabla)

	return page_faults, info


def impresion(secuencia,cantidad, info):
    info1 = pd.DataFrame(info)
    info_organizada = info1.transpose()
    print(tabulate(info_organizada,headers=secuencia,showindex=False,tablefmt="fancy_grid"))
    print("Cantidad de fallos: "+str(cantidad))




if __name__ == '__main__':
	#pages = [1,2,3,4,1,2,5,1,2,3,4,5]
	#pages = [3,2,1,0,3,2,4,3,2,1,0,4]

	pages = input("Ingrese la secuencia (ej: 1,2,3,4... minimo 12 caracteres):\n")
	pages = pages.split(",")#convierte la cadena de texto en una lista delimitada por comas
	pages = list(map(int, pages))#convierte la lista str a una lista int
	n = len(pages)
	if n < 12:
		sys.exit("Ingrese una cadena de 12 caracteres o mas")
	capacity = int(input("\nIngrese la cantidad de modulos:\n"))
 
	cantidad, info= pageFaults(pages, n, capacity)
	impresion(pages,cantidad, info)


