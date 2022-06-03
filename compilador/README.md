# **Compilador Mini C**

Para iniciar el programa ejecutar el archivo
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
  ```
  $ -10 / 2 * sin(10) + pi
  ```
  ```
  5.861698208036642
  ```
