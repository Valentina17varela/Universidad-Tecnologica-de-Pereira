import pygame
import math

def plano_cartesiano(p,centro):
    centro_x=centro[0]
    centro_y=centro[1]
    x=p[0]
    y=p[1]
    xp=x+centro_x
    yp=-y+centro_y
    return [xp,yp]

def escala(p,s):
    xp = p[0]*s[0]
    yp = p[1]*s[1]
    return [xp,yp]

def traslacion(p,t):
    xp=p[0]+t[0]
    yp=p[1]+t[1]
    return [xp,yp]

def rotacion(l,a):
    r=math.radians(a)
    xp=l[0]*math.cos(r)+l[1]*math.sin(r)
    yp=-l[0]*math.sin(r)+l[1]*math.cos(r)
    return[xp,yp]

def rotacionAH(l,a):
    r=math.radians(a)
    xp=l[0]*math.cos(r)-l[1]*math.sin(r)
    yp=l[0]*math.sin(r)+l[1]*math.cos(r)
    return[xp,yp]

