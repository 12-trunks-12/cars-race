#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *

#====================================
#     ----------MAPA---------
#====================================
pygame.init()

class Mapa():
    grupo_tiles = []  # Combinación de números donde cada número representa un tile (1=asfalto, 2=borde vertical, 3=borde horizontal, 4=línea de meta, 5=hierba)

    def crear(self, nivel):
        """ Recoge todos los números de un archivo .txt y los almacena en una variable local """

        txt = open("mapas/nivel"+str(nivel)+(".txt"))  # Abrimos el archivo .txt
        for linea in txt:  # Leemos cada línea
            for numero in linea:  # Leemos cada número de la línea
                self.grupo_tiles.append(numero)  # Añadimos el número a la variable local
        txt.close()  # Cerramos el archivo .txt

    def dibujar(self, surface):
        """ Dibujo el nivel creado anteriormente en un surface seleccionado """

        tile_asfalto = pygame.image.load("imagenes/tile_asfalto.png")  # Número 1
        tile_borde_vertical = pygame.image.load("imagenes/tile_borde_vertical.png")  # Número 2
        tile_borde_horizontal = pygame.image.load("imagenes/tile_borde_horizontal.png")  # Número 3
        tile_meta = pygame.image.load("imagenes/tile_meta.png")  # Número 4
        tile_hierba = pygame.image.load("imagenes/tile_hierba.png")  # Número 5

        tile_pos = [0, 0]  # Coordenadas que indicarán que posición le corresponde al siguiente tile
        for tile in self.grupo_tiles:  # Leemos cada número de la variable local
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

            if tile != '\n':  # Si el tile seleccionado no es un salto de línea
                tile_pos[0] += 10  # Sumamos hacia la derecha
                if tile_pos[0] >= 1280:  # Si llegamos al final de la pantalla saltamos a la línea de abajo
                    tile_pos[0] = 0  # Volvemos a la izquierda
                    tile_pos[1] += 10  # Sumamos 10 para pasar a la siguiente línea


