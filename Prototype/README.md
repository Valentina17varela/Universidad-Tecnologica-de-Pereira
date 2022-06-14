# Patron Prototipo
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)
![](https://img.shields.io/badge/Code-Java-informational?style=flat&logo=java&logoColor=whitew&color=ed1d25)

Es un patrón de diseño creacional, que tiene como objetivo crear a partir de un modelo. Especificar el tipo de objetos que se crearán mediante una instancia prototípica, 
y crear nuevos objetos copiando este prototipo.

<br>

## Solución y estructura
La solución consistirá en definir una interfaz que expone el método necesario para realizar la clonación del objeto. Las clases que pueden ser clonadas implementarán esta interfaz, mientras que las clases que deseen clonar deberán utilizar el método definido en la interfaz.

<div align=center>
  
![](https://github.com/Valentina17varela/Universidad-Tecnologica-de-Pereira/blob/main/Prototype/imagenes/Imagen1.png)
  
</div>

-	Client: Es la clase encargada de solicitar al prototipo que realice la clonación necesaria.
-	Prototype: Interfaz que define la operación de clonado. Será implementada por todos los objetos que puedan ser clonados. En ocasiones es implementado como una clase abstracta.
-	ConcretePrototypeN: Implementa la interfaz Prototype y hace uso del método clone para realizar el clonado de la nueva clase deseada.

## Ejemplos

1. Juan quiere comprar una bicicleta de color rojo y de rodado 22, pero luego cuando llega al lugar y la ve desea verla de color negra y que sea rodado 30.

<div align=center>
  
<img src=https://github.com/Valentina17varela/Universidad-Tecnologica-de-Pereira/blob/main/Prototype/imagenes/Imagen2.png width="350">
  
[Solucion](https://github.com/Valentina17varela/Universidad-Tecnologica-de-Pereira/tree/main/Prototype/Bicicleta)

  </div>

<br>

2. Se tiene una fábrica de camisetas, para realizar nuevos pedidos solo se modifica la talla, el color, y el estampado de la nueva camiseta.

<div align=center>
  
<img src=https://github.com/Valentina17varela/Universidad-Tecnologica-de-Pereira/blob/main/Prototype/imagenes/Imagen3.png width=350>
  
[solucion](https://github.com/Valentina17varela/Universidad-Tecnologica-de-Pereira/tree/main/Prototype/Fabrica%20camisas)

</div>
