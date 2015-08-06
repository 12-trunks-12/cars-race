#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
#====================================
#     ---------BOTON---------
#====================================
class Boton():
    def __init__(self, imagen_normal, pos, imagen_pulsada=False):
        self.image_normal = pygame.image.load("imagenes/"+imagen_normal+".png")  # Imagen cuando el botón no está pulsado
        if imagen_pulsada != False:  # Si el botón puede estar pulsado
            self.modo = False  # Indica si está pulsado o no
            self.image_pulsada = pygame.image.load("imagenes/"+imagen_normal+"_pulsado.png")  # Imagen cuando el botón está pulsado
        self.image = self.image_normal  # Imagen actual (pulsado o no pulsado)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def pulsar(self):
        """ Cambiamos la imagen actual en caso de que se pulse el botón """

        if self.image_pulsada != False:  # Si puede estar pulsada
            if self.modo == False:  # Si no está pulsada
                self.modo = True  # Pasa a ser pulsada
                self.image = self.image_pulsada

            else:  # Si está pulsada
                self.modo = False  # Pasa a ser no pulsada
                self.image = self.image_normal
