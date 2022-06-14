# **Compilador Mini C**
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)
![](https://img.shields.io/badge/Code-C-informational?style=flat&logo=C&logoColor=white&color=5E97D0)

Compilador simplificado del lenguaje C. Las reglas gramaticales que utiliza este lenguaje se encuentran especificadas en  ```minic.txt ```.

Para iniciar el programa ejecutar el archivo:
```
miniC.py
```

## Menu
El compilador puede realizar las siguientes operaciones:
- Analisis sintactico --> AST
- Analisis semantico --> Tabla de simbolos
- Analisis lexico
- Interprete
<br>

  ### Analisis sintactico
  
  DESCRIPCION
  <br>
Esta parte es la encargada de transformar la entrada en un arbol de derivacion (AST). Para esto el lexer lee la entrada e identifica y clasifica cada uno de los      tokens que hacen parte de la entrada, luego el analizador descendente identifica las jerarquias que presentan los tipos de los tokens y los organiza en un AST, el cual es impreso por la funcion de DotRender.

  PRUEBA FUNCIONAMIENTO
  ```
  $ a = b * 4 + 5
  ```
  ```
   Assignment(ident=Ident(name='a'), expr=Binop(oper='+', left=Binop(oper='*', 
   left=Ident(name='b'), right=Number(value=4)), right=Number(value=5)))

  digraph AST {
        node [color=lightblue2 shape=box style=filled]
        edge [arrowhead=none]
        n01 [label="="]
        n02 [label=a]
        n01 -> n02
        n03 [label="+"]
        n04 [label="*"]
        n05 [label=b]
        n04 -> n05
        n06 [label=4]
        n04 -> n06
        n03 -> n04
        n07 [label=5]
        n03 -> n07
        n01 -> n03
  }
  ```


  ### Analisis semantico
  
   DESCRIPCION
  <br>
  Este analizador utiliza la información recoletada por el arbol de derivacion para comprobar la consistencia semantica de la entrada con la definicion del lenguaje. Despues de ejecutar el lexer y realizar la tokenizacion, se organiza la informacion en una tabla de simbolos que recibe el tipo y el valor del token para realizar la clasificacion, para finalizar se hace uso de la libreria  ```tabulate``` para realizar la impresion de la tabla.
  
   PRUEBA FUNCIONAMIENTO
  ```
  $ b = 2 + 6 * 3
  ```
  ```
  {'IDENT': 'b', '=': '=', 'NUMBER': '3', '+': '+', '*': '*'}


  Tabla de simbolos

  ╒═════════╤═════╤══════════╤═════╤═════╕
  │ IDENT   │ =   │   NUMBER │ +   │ *   │
  ╞═════════╪═════╪══════════╪═════╪═════╡
  │ b       │ =   │        3 │ +   │ *   │
  ╘═════════╧═════╧══════════╧═════╧═════╛
  ```
  
  ### Analisis lexico
  
   DESCRIPCION
   <br>
   La funcion del lexer es desglozar el codigo y separar cada uno de los tokens que la conforman, guarda la informacion necesaria como identificadores, literales y operadores. Se devuelve una lista con todos los elementos clasificados que hacen parte de la entrada. 
  
   PRUEBA FUNCIONAMIENTO
  ```
  $ c = d + 34 * 5 / ( 4 + 3 )
  ```
  ```
  Token(type='IDENT', value='c', lineno=1, index=0)
  Token(type='=', value='=', lineno=1, index=2)
  Token(type='IDENT', value='d', lineno=1, index=4)
  Token(type='+', value='+', lineno=1, index=6)
  Token(type='NUMBER', value=34, lineno=1, index=8)
  Token(type='*', value='*', lineno=1, index=11)
  Token(type='NUMBER', value=5, lineno=1, index=13)
  Token(type='/', value='/', lineno=1, index=15)
  Token(type='(', value='(', lineno=1, index=17)
  Token(type='NUMBER', value=4, lineno=1, index=19)
  Token(type='+', value='+', lineno=1, index=21)
  Token(type='NUMBER', value=3, lineno=1, index=23)
  Token(type=')', value=')', lineno=1, index=25)
  ```
  
  ### Interprete
  
   DESCRIPCION
   <br>
   El interprete traduce cada una de las lineas del codigo, las lee, las analiza y realiza su ejecucion. Para agregar esta parte al compilador se deben modificar los archivos que conforman el ```lexer``` y el ```parser```. Se agregan constantes (pi, euler) , funciones trigonometricas (sin, cos, asin, acos, atan, sinh, cosh, tanh, log, log10, exp, sqrt, int, abs, chr, clock), asignaciones (+=, -=, *=, /=, %=) y operadores (++, --).
   
   PRUEBA FUNCIONAMIENTO
  ```
  $ -10 / 2 * sin(10) + pi
  ```
  ```
  5.861698208036642
  ```
