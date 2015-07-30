#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import menu
import juego

#====================================
#    ----------INICIO----------
#====================================
#------------------Initialize
pygame.init()
DISPLAYSURF = pygame.display.set_mode((ANCHO_SCREEN, ALTO_SCREEN))
pygame.display.set_caption("Cars Race")
fps_clock = pygame.time.Clock()

#====================================
#     -----------LOOP-----------
#====================================
while True:
    #---------------Menú
    menu.menu_inicio(DISPLAYSURF, fps_clock)

    #---------------Juego
    juego.juego(DISPLAYSURF, fps_clock)
