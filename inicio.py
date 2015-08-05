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
fps_clock = pygame.time.Clock()  # Contador de los FPS a los que correrá el juego

#====================================
#     -----------LOOP-----------
#====================================
while True:  # Bucle del programa, cuando se le das a jugar en el menú de inicio (JUGAR), se rompe la función y pasa al juego y viceversa
    #---------------Menú
    menu.menu_inicio(DISPLAYSURF, fps_clock)

    #---------------Juego
    juego.juego(DISPLAYSURF, fps_clock)
