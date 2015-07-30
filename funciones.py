#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
import pygame.gfxdraw
#====================================
#     ---------FUNCIONES---------
#====================================
def crear_carta(surface, pos_x, pos_y, imagen_coche, velocidad_max, aceleracion, turbo, manejo, frenada, activado):
    #------------------Rectángulos y fotos
    rect_fondo = pygame.gfxdraw.box(surface, (pos_x, pos_y, 230, 250), (30, 30, 30))

    rect_coches = pygame.gfxdraw.box(surface, (pos_x+10, pos_y+10, 210, 50), (120, 120, 120))

    coche_arriba = pygame.image.load(imagen_coche)
    coche_derecha = pygame.transform.rotate(coche_arriba, 90)
    coche_abajo = pygame.transform.rotate(coche_arriba, 180)
    coche_izquierda = pygame.transform.rotate(coche_arriba, 270)

    rect_propiedades = pygame.gfxdraw.box(surface, (pos_x+10, pos_y+80, 210, 150), (0, 150, 255))

    #------------------Textos características
    font = pygame.font.Font("Prototype.TTF", 13)
    texto_velocidad_max = font.render("VELOCIDAD MÁX. : "+str(velocidad_max), True, (0, 255, 0))
    texto_aceleracion = font.render("ACELERACIÓN : "+str(float(aceleracion)), True, (0, 255, 0))
    texto_turbo = font.render("TURBO : "+str(float(turbo)), True, (0, 255, 0))
    texto_manejo = font.render("MANEJO : "+str(manejo), True, (0, 255, 0))
    texto_frenada = font.render("FRENADA : "+str(float(frenada)), True, (0, 255, 0))

    #================================UPDATE============================
    #------------------Imágenes coches
    surface.blit(coche_arriba, (pos_x+35, pos_y+15))
    surface.blit(coche_derecha, (pos_x+65, pos_y+25))
    surface.blit(coche_abajo, (pos_x+122.5, pos_y+15))
    surface.blit(coche_izquierda, (pos_x+155, pos_y+25))

    #------------------Textos características
    surface.blit(texto_velocidad_max, (pos_x+40, pos_y+85))
    surface.blit(texto_aceleracion, (pos_x+52, pos_y+115))
    surface.blit(texto_turbo, (pos_x+75, pos_y+145))
    surface.blit(texto_manejo, (pos_x+73, pos_y+175))
    surface.blit(texto_frenada, (pos_x+62, pos_y+205))



