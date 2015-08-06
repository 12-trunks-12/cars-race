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

#====================================
#     ---------JUEGO---------
#====================================
pygame.mixer.pre_init(22050, -16, 10, 4096)
pygame.init()

def juego(surface, fps_clock):
    """ Hace funcionar el juego en si, empezando la carrera"""

    #-Creamos los jugadores e inicializamos los datos
    jugador1 = coche.Coche(perfil.coche_j1)  # Nombre, velocidad máxima, aceleración, turbo, manejo, frenada
    jugador2 = coche.Coche(perfil.coche_j2)  # Nombre, velocidad máxima, aceleración, turbo, manejo, frenada

    iniciar_datos_jugador(jugador1, perfil.coche_j1, (640, 35))
    iniciar_datos_jugador(jugador2, perfil.coche_j2, (640, 75))

    #-Creamos el mapa
    mapa = Mapa()
    mapa.crear(1)  # Creamos el mapa según el nivel seleccionado

    tiles_hierba = mapa.dibujar(surface)

    #-Cargamos la música
    sonido_motor_j1 = pygame.mixer.Sound("Sonidos/Sonido Motor.wav")  # Cargamos el sonido de un motor
    sonido_motor_j1.play()
    sonido_motor_j1.set_volume(0)  # Ponemos el volumen a 0, pues está condicionado por la velocidad del coche (empieza a 0)

    sonido_motor_j2 = pygame.mixer.Sound("Sonidos/Sonido Motor.wav")  # Cargamos el sonido de un motor
    sonido_motor_j2.play()
    sonido_motor_j2.set_volume(0)  # Ponemos el volumen a 0, pues está condicionado por la velocidad del coche (empieza a 0)

    #-Creamos algunas variables
    pausa = False  # Indica si el juego está en pausa o no

    #================================BUCLE============================
    while True:
        if pausa == True:  # Si el juego está en pausa
            sonido_motor_j1.stop()
            sonido_motor_j2.stop()

            pausa = False  # False para que una vez cerrada la función de menu_pausa el juego no siga en pausa
            jugador1.corriendo, jugador1.frenando, jugador1.girando, jugador1.turbeando = False, False, False, False
            jugador2.corriendo, jugador2.frenando, jugador2.girando, jugador2.turbeando = False, False, False, False

            salir = menu.menu_pausa(surface, fps_clock)  # Activamos el menú de pausa, que devuelve True si se le da a salir
            if salir == True:  # Si volvió al menú principal
                iniciar_datos_jugador(jugador1, perfil.coche_j1, (640, 35))
                iniciar_datos_jugador(jugador2, perfil.coche_j2, (640, 75))
            else:
                sonido_motor_j1.play()
                sonido_motor_j2.play()

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


        #------------------Calculamos datos y variables y aplicamos sonidos (actualizamos la posición de cada jugador, la ajustamos si es necesario y cambiamos la imagen)
        #-Jugador 1
        jugador1.actualizar_movimiento(tiles_hierba)  # Actualizamos los datos
        if jugador1.velocidad > 0:  # Si la velocidad es mayor que 0
            sonido_motor_j1.set_volume(jugador1.velocidad/100)
        else:  # Si la velocidad es menor que 0
            sonido_motor_j1.set_volume(jugador1.velocidad*-1/100)

        #-Jugador 2
        jugador2.actualizar_movimiento(tiles_hierba)  # Actualizamos los datos
        if jugador2.velocidad > 0:  # Si la velocidad es mayor que 0
            sonido_motor_j2.set_volume(jugador2.velocidad/100)
        else:  # Si la velocidad es menor que 0
            sonido_motor_j2.set_volume(jugador2.velocidad*-1/100)

        #================================UPDATE============================
        #------------------Mapa
        mapa.dibujar(surface)  # Dibujamos el mapa en el surface

        #------------------Coches
        surface.blit(jugador1.image, (jugador1.rect.x, jugador1.rect.y))
        surface.blit(jugador2.image, (jugador2.rect.x, jugador2.rect.y))

        #------------------Marcadores
        # Para la versión 2.0

        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)
