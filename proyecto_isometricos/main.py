import pygame
import math
from libreria import *

'''
PARCIAL Crear una figura isometrica que pueda:
Traslacion (10 px hacia la izquierda y hacia la derecha) 
Escala (aumentar y regresar al tamaño) 
Rotacion (solo 5 grados aumentando y disminuyendo)
'''

#colores a usar en la figura
verde = [0,255,0]
rojo = [255,0,0]
azul = [0,0,255]
blanco = [255,255,255]
negro = [0,0,0]
turquesa = [83,166,154]
lila = [203,139,218]
naranja = [225,170,159]

#dimensiones de la ventana
ancho = 1200
alto = 800

if __name__ == "__main__":
    #inicializar la ventana
    pygame.init()
    pantalla = pygame.display.set_mode([ancho,alto])

    #DIBUJAR FIGURA
    #Vista frontal
    a = [400,300]
    b = [400,350]
    c=[450,375]
    d=[450,425]
    e=[400,400]
    f=[400,450]
    g = [550,525]
    h = [550,475]
    i = [500,450]
    j = [500,400]
    k = [550,425]
    l = [550,375]
    lista = [a,b,c,d,e,f,g,h,i,j,k,l]

    #vista lateral
    m = [650,425]
    n = [650,475]
    lista3 = [g,h,m,n]
    o = [650,325]
    p = [650,375]
    lista4 = [k,l,o,p]

    #vista superior
    lista1 = [c,d,e]
    lista2 = [i,j,k]
    q = [600,400]
    lista5 = [h,i,q,m]
    r = [500,250]
    lista6 = [o,l,a,r]
        
    pygame.draw.polygon(pantalla,naranja, lista)
    pygame.draw.polygon(pantalla,lila,lista1)
    pygame.draw.polygon(pantalla,turquesa,lista2)
    pygame.draw.polygon(pantalla,turquesa,lista3)
    pygame.draw.polygon(pantalla,turquesa,lista4)
    pygame.draw.polygon(pantalla,lila,lista5)
    pygame.draw.polygon(pantalla,lila,lista6)
    pygame.display.flip()

    fin = False
    while not fin:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:#trasladar 10px a la derecha con flecha derecha
                        pantalla.fill(negro)
                        s = [10,0] 

                        #se realizan las operaciones necesarias para trasladar todos los puntos
                        a = traslacion(a,s)
                        b = traslacion(b,s)
                        c = traslacion(c,s)
                        d = traslacion(d,s)
                        e = traslacion(e,s)
                        f = traslacion(f,s)
                        g = traslacion(g,s)
                        h = traslacion(h,s)
                        i = traslacion(i,s)
                        j = traslacion(j,s)
                        k = traslacion(k,s)
                        l = traslacion(l,s)
                        m = traslacion(m,s)
                        n = traslacion(n,s)
                        o = traslacion(o,s)
                        p = traslacion(p,s)
                        q = traslacion(q,s)
                        r = traslacion(r,s)

                        #se asignan nuevamente las variables en el orden en que van a ser dibujadas
                        lista = [a,b,c,d,e,f,g,h,i,j,k,l]
                        lista3 = [g,h,m,n]
                        lista4 = [k,l,o,p]
                        lista1 = [c,d,e]
                        lista2 = [i,j,k]
                        lista5 = [h,i,q,m]
                        lista6 = [o,l,a,r]
                        pygame.draw.polygon(pantalla,naranja, lista)
                        pygame.draw.polygon(pantalla,lila,lista1)
                        pygame.draw.polygon(pantalla,turquesa,lista2)
                        pygame.draw.polygon(pantalla,turquesa,lista3)
                        pygame.draw.polygon(pantalla,turquesa,lista4)
                        pygame.draw.polygon(pantalla,lila,lista5)
                        pygame.draw.polygon(pantalla,lila,lista6)
                        pygame.display.flip()

                    if event.key == pygame.K_LEFT:#trasladar 10px a la izquierda con flecha izq
                        pantalla.fill(negro)
                        s = [-10,0]

                        #se realizan las operaciones necesarias para trasladar todos los puntos
                        a = traslacion(a,s)
                        b = traslacion(b,s)
                        c = traslacion(c,s)
                        d = traslacion(d,s)
                        e = traslacion(e,s)
                        f = traslacion(f,s)
                        g = traslacion(g,s)
                        h = traslacion(h,s)
                        i = traslacion(i,s)
                        j = traslacion(j,s)
                        k = traslacion(k,s)
                        l = traslacion(l,s)
                        m = traslacion(m,s)
                        n = traslacion(n,s)
                        o = traslacion(o,s)
                        p = traslacion(p,s)
                        q = traslacion(q,s)
                        r = traslacion(r,s)

                        #se asignan nuevamente las variables en el orden en que van a ser dibujadas
                        lista = [a,b,c,d,e,f,g,h,i,j,k,l]
                        lista3 = [g,h,m,n]
                        lista4 = [k,l,o,p]
                        lista1 = [c,d,e]
                        lista2 = [i,j,k]
                        lista5 = [h,i,q,m]
                        lista6 = [o,l,a,r]
                        pygame.draw.polygon(pantalla,naranja, lista)
                        pygame.draw.polygon(pantalla,lila,lista1)
                        pygame.draw.polygon(pantalla,turquesa,lista2)
                        pygame.draw.polygon(pantalla,turquesa,lista3)
                        pygame.draw.polygon(pantalla,turquesa,lista4)
                        pygame.draw.polygon(pantalla,lila,lista5)
                        pygame.draw.polygon(pantalla,lila,lista6)
                        pygame.display.flip()

                    if event.key == pygame.K_UP: #rotar 5° sentido horario con la flecha arriba
                        pantalla.fill(negro)
                        angulo = 5
                        pf = r #el punto fijo va a ser la r
                        elementos = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r]#se guardan en una lista todos los puntos

                        #se hacen las operaciones necesarias para rotar con un punto fijo 
                        tr1=[]
                        for i in elementos:
                            tr1.append(traslacion(i,[-r[0],-r[1]]))
                        
                        rotado = []
                        for i in tr1:
                            rotado.append(rotacion(i,angulo))

                        fijo1 = []
                        for i in rotado:
                            fijo1.append(traslacion(i,pf))

                        #se asigna cada elemento de la lista que ya esta rotado a las variables originales
                        a = fijo1[0]
                        b = fijo1[1]
                        c = fijo1[2]
                        d = fijo1[3]
                        e = fijo1[4]
                        f = fijo1[5]
                        g = fijo1[6]
                        h = fijo1[7]
                        i = fijo1[8]
                        j = fijo1[9]
                        k = fijo1[10]
                        l = fijo1[11]
                        m = fijo1[12]
                        n = fijo1[13]
                        o = fijo1[14]
                        p = fijo1[15]
                        q = fijo1[16]
                        r = fijo1[17]

                        #se guardan las variables en el orden en que deben ser dibujadas
                        lista = [a,b,c,d,e,f,g,h,i,j,k,l]
                        lista3 = [g,h,m,n]
                        lista4 = [k,l,o,p]
                        lista1 = [c,d,e]
                        lista2 = [i,j,k]
                        lista5 = [h,i,q,m]
                        lista6 = [o,l,a,r]
                        pygame.draw.polygon(pantalla,naranja, lista)
                        pygame.draw.polygon(pantalla,lila,lista1)
                        pygame.draw.polygon(pantalla,turquesa,lista2)
                        pygame.draw.polygon(pantalla,turquesa,lista3)
                        pygame.draw.polygon(pantalla,turquesa,lista4)
                        pygame.draw.polygon(pantalla,lila,lista5)
                        pygame.draw.polygon(pantalla,lila,lista6)
                        pygame.display.flip()

                    if event.key == pygame.K_DOWN: #rotar 5° sentido antihorario con la flecha abajo
                        pantalla.fill(negro)
                        angulo = 5
                        pf = r #el punto fijo va a ser la r
                        elementos = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r]#se guardan en una lista todos los puntos

                        #se hacen las operaciones necesarias para rotar con un punto fijo 
                        tr1=[]
                        for i in elementos:
                            tr1.append(traslacion(i,[-r[0],-r[1]]))
                        
                        rotado = []
                        for i in tr1:
                            rotado.append(rotacionAH(i,angulo))

                        fijo1 = []
                        for i in rotado:
                            fijo1.append(traslacion(i,pf))

                        #se asigna cada elemento de la lista que ya esta rotado a las variables originales
                        a = fijo1[0]
                        b = fijo1[1]
                        c = fijo1[2]
                        d = fijo1[3]
                        e = fijo1[4]
                        f = fijo1[5]
                        g = fijo1[6]
                        h = fijo1[7]
                        i = fijo1[8]
                        j = fijo1[9]
                        k = fijo1[10]
                        l = fijo1[11]
                        m = fijo1[12]
                        n = fijo1[13]
                        o = fijo1[14]
                        p = fijo1[15]
                        q = fijo1[16]
                        r = fijo1[17]

                        #se guardan las variables en el orden en que deben ser dibujadas
                        lista = [a,b,c,d,e,f,g,h,i,j,k,l]
                        lista3 = [g,h,m,n]
                        lista4 = [k,l,o,p]
                        lista1 = [c,d,e]
                        lista2 = [i,j,k]
                        lista5 = [h,i,q,m]
                        lista6 = [o,l,a,r]
                        pygame.draw.polygon(pantalla,naranja, lista)
                        pygame.draw.polygon(pantalla,lila,lista1)
                        pygame.draw.polygon(pantalla,turquesa,lista2)
                        pygame.draw.polygon(pantalla,turquesa,lista3)
                        pygame.draw.polygon(pantalla,turquesa,lista4)
                        pygame.draw.polygon(pantalla,lila,lista5)
                        pygame.draw.polygon(pantalla,lila,lista6)
                        pygame.display.flip()

            if event.type == pygame.MOUSEBUTTONDOWN: #Escalar con la rueda del raton
                if event.button == 4: #Aumentar tamaño rueda arriba
                    pantalla.fill(negro)
                    s = [1.2,1.2] #escalar a 1.2
                    pf = c #el punto fijo va a ser la c
                    elementos = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r]#se guardan en una lista todos los puntos

                    #se hacen las operaciones necesarias para escalar con un punto fijo 
                    tr=[]
                    for i in elementos:
                        tr.append(traslacion(i,[-c[0],-c[1]]))

                    escalado = []
                    for i in tr:
                        escalado.append(escala(i,s))

                    fijo = []
                    for i in escalado:
                        fijo.append(traslacion(i,pf))

                    #se asigna cada elemento de la lista que ya esta escalado a las variables originales
                    a = fijo[0]
                    b = fijo[1]
                    c = fijo[2]
                    d = fijo[3]
                    e = fijo[4]
                    f = fijo[5]
                    g = fijo[6]
                    h = fijo[7]
                    i = fijo[8]
                    j = fijo[9]
                    k = fijo[10]
                    l = fijo[11]
                    m = fijo[12]
                    n = fijo[13]
                    o = fijo[14]
                    p = fijo[15]
                    q = fijo[16]
                    r = fijo[17]

                    #se guardan las variables en el orden en que deben ser dibujadas
                    lista = [a,b,c,d,e,f,g,h,i,j,k,l]
                    lista3 = [g,h,m,n]
                    lista4 = [k,l,o,p]
                    lista1 = [c,d,e]
                    lista2 = [i,j,k]
                    lista5 = [h,i,q,m]
                    lista6 = [o,l,a,r]
                    pygame.draw.polygon(pantalla,naranja, lista)
                    pygame.draw.polygon(pantalla,lila,lista1)
                    pygame.draw.polygon(pantalla,turquesa,lista2)
                    pygame.draw.polygon(pantalla,turquesa,lista3)
                    pygame.draw.polygon(pantalla,turquesa,lista4)
                    pygame.draw.polygon(pantalla,lila,lista5)
                    pygame.draw.polygon(pantalla,lila,lista6)
                    pygame.display.flip()
                    
                if event.button == 5: #Disminuir tamaño con la rueda abajo
                    pantalla.fill(negro)
                    s = [0.8,0.8]
                    pf = c #el punto fijo va a ser la c
                    elementos = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r]#se guardan en una lista todos los puntos

                    #se hacen las operaciones necesarias para escalar con un punto fijo 
                    tr=[]
                    for i in elementos:
                        tr.append(traslacion(i,[-c[0],-c[1]]))

                    escalado = []
                    for i in tr:
                        escalado.append(escala(i,s))

                    fijo = []
                    for i in escalado:
                        fijo.append(traslacion(i,pf))

                    #se asigna cada elemento de la lista que ya esta escalado a las variables originales
                    a = fijo[0]
                    b = fijo[1]
                    c = fijo[2]
                    d = fijo[3]
                    e = fijo[4]
                    f = fijo[5]
                    g = fijo[6]
                    h = fijo[7]
                    i = fijo[8]
                    j = fijo[9]
                    k = fijo[10]
                    l = fijo[11]
                    m = fijo[12]
                    n = fijo[13]
                    o = fijo[14]
                    p = fijo[15]
                    q = fijo[16]
                    r = fijo[17]

                    #se guardan las variables en el orden en que deben ser dibujadas
                    lista = [a,b,c,d,e,f,g,h,i,j,k,l]
                    lista3 = [g,h,m,n]
                    lista4 = [k,l,o,p]
                    lista1 = [c,d,e]
                    lista2 = [i,j,k]
                    lista5 = [h,i,q,m]
                    lista6 = [o,l,a,r]
                    pygame.draw.polygon(pantalla,naranja, lista)
                    pygame.draw.polygon(pantalla,lila,lista1)
                    pygame.draw.polygon(pantalla,turquesa,lista2)
                    pygame.draw.polygon(pantalla,turquesa,lista3)
                    pygame.draw.polygon(pantalla,turquesa,lista4)
                    pygame.draw.polygon(pantalla,lila,lista5)
                    pygame.draw.polygon(pantalla,lila,lista6)
                    pygame.display.flip()

    pygame.quit()




