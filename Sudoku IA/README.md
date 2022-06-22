## Sudoku Inteligencia Artificial 
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)

### Requerimientos 
Implemente y pruebe un algoritmo con vuelta atrás (backtracking) para resolver problemas de Sudoku.

Su software necesita leer la entrada de la siguiente manera. El primer número, que aparece solo en una fila, representa el tamaño del tablero. Los siguientes números representan el problema dado. Aparecen en una cuadrícula que corresponde al tamaño del tablero. Cada número está separado de los demás por espacios en blanco. A continuación se muestra un ejemplo de una cuadrícula de 9x9.
```bash
9
3 6 0 0 2 0 0 8 9
0 0 0 3 6 1 0 0 0
0 0 0 0 0 0 0 0 0
8 0 3 0 0 0 6 0 2
4 0 0 6 0 3 0 0 7
6 0 7 0 0 0 1 0 8
0 0 0 0 0 0 0 0 0
0 0 0 4 1 8 0 0 0
9 7 0 0 3 0 0 1 4
```

Su software también necesita generar la solución en un archivo. El nombre del archivo debe ser el mismo que el del archivo de entrada con la cadena “Solucion” adjunta después. Por ejemplo, si el archivo de entrada se llama “sudoku9Facil.txt”, la salida debería aparecer en el archivo “sudoku9FacilSolucion.txt”. El archivo de solución debe tener el mismo formato que el archivo de entrada, excepto que NO contiene la primera línea sobre el tamaño de la 
cuadrícula.  Si no existe una solución, debe escribir -1 en el archivo.


<br>

### Implementacion 
- En la carpeta "6x6_9x9" se encuentra la solución con backtracking y el patrón observador en un agente inteligente para problemas de 6x6 y 9x9.

- En la carpeta "9x9_16x16"  se implementó la inferencia AC3 y backtracking para resolver problemas 9x9_16x16.

<br>

#### Input
```bash
6
1 0 0 0 0 2
0 0 3 0 0 0
0 0 0 4 0 0
0 0 0 0 0 0
0 6 0 0 0 0
0 0 0 0 0 0
```

#### Output
```bash
1 4 5 3 6 2 
6 2 3 1 4 5 
2 1 6 4 5 3 
3 5 4 2 1 6 
4 6 2 5 3 1 
5 3 1 6 2 4 
```

