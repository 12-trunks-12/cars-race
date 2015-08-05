#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import FPS
import coche
import menu
from mapa import Mapa
import perfil
from funciones import iniciar_datos_jugador

import time
#====================================
#     ---------JUEGO---------
#====================================
pygame.init()
def juego(surface, fps_clock):
    """ Hace funcionar el juego en si, empezando la carrera"""

    jugador1 = coche.Coche(perfil.coche_j1)  # Nombre, velocidad máxima, aceleración, turbo, manejo, frenada
    jugador2 = coche.Coche(perfil.coche_j2)  # Nombre, velocidad máxima, aceleración, turbo, manejo, frenada

    iniciar_datos_jugador(jugador1, str(perfil.coche_j1), (640, 35))
    iniciar_datos_jugador(jugador2, str(perfil.coche_j2), (640, 75))

    pausa = False  # Indica si el juego está en pausa o no

    mapa = Mapa()
    mapa.crear(1)  # Creamos el mapa según el nivel seleccionado

    #================================BUCLE============================
    while True:
        if pausa == True:  # Si el juego está en pausa
            pausa = False  # False para que una vez cerrada la función de menu_pausa el juego no siga en pausa
            jugador1.corriendo, jugador1.frenando, jugador1.girando, jugador1.turbeando = False, False, False, False
            jugador2.corriendo, jugador2.frenando, jugador2.girando, jugador2.turbeando = False, False, False, False
            salir = menu.menu_pausa(surface, fps_clock)  # Activamos el menú de pausa, que devuelve True si se le da a salir
            if salir == True:  # Si volvió al menú principal
                iniciar_datos_jugador(jugador1, str(perfil.coche_j1), (640, 35))
                iniciar_datos_jugador(jugador2, str(perfil.coche_j2), (640, 75))

        for event in pygame.event.get():
            tecla_pulsada = pygame.key.get_pressed()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                #------------------Jugador 1
                if event.key == K_UP:
                    jugador1.corriendo = True
                elif event.key == K_DOWN:
                    jugador1.frenando = True
                    jugador1.turbeando = False
                elif event.key == K_KP0:
                    jugador1.turbeando = True

                elif event.key == K_RIGHT:
                    jugador1.girando = 'derecha'
                elif event.key == K_LEFT:
                    jugador1.girando = 'izquierda'

                #------------------Jugador 2
                elif event.key == K_w:
                    jugador2.corriendo = True
                elif event.key == K_s:
                    jugador2.frenando = True
                    jugador2.turbeando = False
                elif event.key == K_SPACE:
                    jugador2.turbeando = True

                elif event.key == K_d:
                    jugador2.girando = 'derecha'
                elif event.key == K_a:
                    jugador2.girando = 'izquierda'

                #--Menu de pausa
                elif event.key == K_p:
                    pausa = True

            elif event.type == KEYUP:
                #------------------Jugador 1
                if event.key == K_UP:
                    jugador1.corriendo = False
                    jugador1.turbeando = False
                    if tecla_pulsada[K_DOWN]:
                        jugador1.frenando = True
                elif event.key == K_DOWN:
                    jugador1.frenando = False
                    if tecla_pulsada[K_UP]:
                        jugador1.corriendo = True
                elif event.key == K_KP0:
                    jugador1.turbeando = False

                elif event.key == K_RIGHT:
                    jugador1.girando = False
                    if tecla_pulsada[K_LEFT]:
                        jugador1.girando = 'izquierda'
                elif event.key == K_LEFT:
                    jugador1.girando =  False
                    if tecla_pulsada[K_RIGHT]:
                        jugador1.girando = 'derecha'

                #------------------Jugador 2
                elif event.key == K_w:
                    jugador2.corriendo = False
                    jugador2.turbeando = False
                    if tecla_pulsada[K_s]:
                        jugador2.frenando = True
                elif event.key == K_s:
                    jugador2.frenando = False
                    if tecla_pulsada[K_w]:
                        jugador2.corriendo = True
                elif event.key == K_SPACE:
                    jugador2.turbeando = False

                elif event.key == K_d:
                    jugador2.girando = False
                    if tecla_pulsada[K_a]:
                        jugador2.girando = 'izquierda'
                elif event.key == K_a:
                    jugador2.girando = False
                    if tecla_pulsada[K_d]:
                        jugador2.girando = 'derecha'


        #------------------Calculamos datos y variables (actualizamos la posición de cada jugador, la ajustamos si es necesario y cambiamos la imagen)
        jugador1.actualizar_movimiento()
        jugador2.actualizar_movimiento()

        #================================UPDATE============================
        #------------------Mapa
        mapa.dibujar(surface)  # Dibujamos el mapa en el surface

        #------------------Coches
        surface.blit(jugador1.image, (jugador1.rect.x, jugador1.rect.y))
        surface.blit(jugador2.image, (jugador2.rect.x, jugador2.rect.y))

        #------------------Marcadores


        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)
