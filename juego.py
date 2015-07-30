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

#====================================
#     ---------JUEGO---------
#====================================
pygame.init()
def juego(surface, fps_clock):
    pausa = False

    jugador1 = coche.Coche(perfil.coche_j1)  # Nombre, velocidad máxima, aceleración, turbo, manejo, frenada
    jugador1.rect.x, jugador1.rect.y = (640, 35)

    jugador2 = coche.Coche(perfil.coche_j2)  # Nombre, velocidad máxima, aceleración, turbo, manejo, frenada
    jugador2.rect.x, jugador2.rect.y = (640, 75)

    mapa = Mapa()
    mapa.crear(1)

    while True:
        if pausa == True:
            pausa = False
            menu.menu_pausa(surface, fps_clock)

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


        #------------------Calculamos datos y variables
        jugador1.actualizar_movimiento()
        jugador2.actualizar_movimiento()

        #================================UPDATE============================
        surface.fill((0, 0, 0))

        #------------------Mapa
        mapa.dibujar(surface)

        #------------------Coches
        surface.blit(jugador1.image, (jugador1.rect.x, jugador1.rect.y))
        surface.blit(jugador2.image, (jugador2.rect.x, jugador2.rect.y))

        #------------------Marcadores


        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)
