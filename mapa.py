#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *

#====================================
#     ----------MAPA---------
#====================================
#tamaño tile: 10x10
pygame.init()
class Mapa():
    grupo_tiles = []

    def crear(self, nivel):
        txt = open("mapas/nivel"+str(nivel)+(".txt"))
        for linea in txt:
            for numero in linea:
                self.grupo_tiles.append(numero)
        txt.close()

    def dibujar(self, surface):
        tile_asfalto = pygame.image.load("imagenes/tile_asfalto.png")
        tile_borde_vertical = pygame.image.load("imagenes/tile_borde_vertical.png")
        tile_borde_horizontal = pygame.image.load("imagenes/tile_borde_horizontal.png")
        tile_hierba = pygame.image.load("imagenes/tile_hierba.png")
        tile_meta = pygame.image.load("imagenes/tile_meta.png")

        tile_pos = [0, 0]
        for tile in self.grupo_tiles:
            if tile == '1':
                surface.blit(tile_asfalto, tile_pos)
            elif tile == '2':
                surface.blit(tile_borde_vertical, tile_pos)
            elif tile == '3':
                surface.blit(tile_borde_horizontal, tile_pos)
            elif tile == '4':
                surface.blit(tile_meta, tile_pos)
            elif tile == '5':
                surface.blit(tile_hierba, tile_pos)
            if tile != '\n':
                tile_pos[0] += 10
                if tile_pos[0] >= 1280:  # Saltamos a la línea de abajo
                    tile_pos[0] = 0
                    tile_pos[1] += 10


