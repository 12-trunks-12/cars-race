#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import perfil
from boton import Boton
from funciones import crear_carta

import time
#====================================
#     ---------MAPA---------
#====================================
pygame.init()
def tienda(surface, fps_clock):
    """ Hace funcionar la tienda, donde se puede seleccionar el coche que se quiera para jugar """

    imagen_fondo = pygame.image.load("imagenes/wallpaper_tienda.png")  # Imagen del fondo de la tienda

    font_pequeña = pygame.font.Font("Xperia.TTF", 30)  # Font para cuando la opción de salir al menú principal no esté seleccionada
    font_grande = pygame.font.Font("Xperia.TTF", 40)  # Font para cuando la opción de salir al menú principal esté seleccionada

   # marcador_dinero_j1 = pygame.image.load("imagenes/marcador_dinero.png")  # Cantidad de dinero del J1
   # marcador_dinero_j2 = pygame.transform.flip(1, 0)  # Cantidad de dinero del J2
   # imagen_dinero = pygame.image.load("imagenes/dinero.png")  # Imagen de una moneda

    #--Propiedades de cada coche y la posición de la carta de cada uno
    lista_prop_coches = [(15, 1, 1.3, 6, 0.5), (18, 1.5, 1.5, 7, 1), (20, 2.5, 1.6, 7, 2), (25, 2, 1.4, 4, 4),
                        (20, 4, 1.8, 9, 2.5), (22, 3, 1.5, 6, 1.5), (20, 3.5, 2.5, 8, 3), (25, 5, 2, 10, 3)]  # Propiedades de cada coche
    lista_pos_cartas = [(75, 30), (375, 30), (675, 30), (975, 30), (75, 340), (375, 340), (675, 340), (975, 340)]  # Posición de cada carta

    #------------------Lista con todos los botones para asignar los coches y la posición de cada uno
    lista_botones_asig_coche = {}  # Lista con todos los botones de asignar el coche
    lista_pos_botones_asig_coche = [(305, 124), (305, 189), (605, 124), (605, 189), (905, 124), (905, 189), (1205, 124), (1205, 189),
        (305, 434), (305, 499), (605, 434), (605, 499), (905, 434), (905, 499), (1205, 434), (1205, 499)]  # Posición de cada boton de asignar coche

    for i in range(16):  # Creamos los 16 botones (1 por jugador para cada coche)
        boton = Boton("boton_asignar_coche", lista_pos_botones_asig_coche[i], "boton_asignar_coche_pulsado")
        lista_botones_asig_coche[str(i)] = boton

    coche_asignado_j1 = perfil.coche_j1  # Coche asignado actualmente para el J1
    lista_botones_asig_coche[str(coche_asignado_j1*2)].pulsar()  # Lo marcamos como asignado

    coche_asignado_j2 = perfil.coche_j2  # Coche asignado actualmente para el J2
    lista_botones_asig_coche[str(coche_asignado_j2*2+1)].pulsar()  # Lo marcamos como asignado

    #================================BUCLE============================
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if (event.pos[0] > 268 and event.pos[0] < 1010) and (event.pos[1] > 648 and event.pos[1] < 690) and opcion_salir == True:
                    return  # Vuelve al menú principal

                #------------------Botones asignar coches
                for i in range(16):  # Recorremos cada botón viendo si el ratón ha pulsado dentro de cada uno, si es así, lo marcamos como asignado
                    if (event.pos[0] > lista_pos_botones_asig_coche[i][0] and event.pos[0] < lista_pos_botones_asig_coche[i][0]+35) and (event.pos[1] > lista_pos_botones_asig_coche[i][1] and event.pos[1] < lista_pos_botones_asig_coche[i][1]+63):
                        lista_botones_asig_coche[str(i)].pulsar()  # Pulsamos el botón, tanto si está como asignado o como si está normal
                        if i%2 == 0:
                            lista_botones_asig_coche[str(coche_asignado_j1*2)].pulsar()  # Desasignamos el coche que tenía asignado el J1
                            perfil.coche_j1 = int(i/2)  # Asignamos el coche a J1
                            coche_asignado_j1 = perfil.coche_j1  # Guardamos el coche asignado
                        else:
                            lista_botones_asig_coche[str(coche_asignado_j2*2+1)].pulsar()  # Desasignamos el coche que tenía asignado el J2
                            perfil.coche_j2 = int(i/2-0.5)  # Asignamos el coche a J2
                            coche_asignado_j2 = perfil.coche_j2  # Guardamos el coche asignado


            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return  # Vuelve al menú principal


        pos_mouse = pygame.mouse.get_pos()
        #------------------Texto volver al menú
        if (pos_mouse[0] > 362 and pos_mouse[0] < 918) and (pos_mouse[1] > 658 and pos_mouse[1] < 691):
             texto_salir = font_grande.render("VOLVER AL MENU PRINCIPAL", True, (255, 255, 255))
             texto_salir_pos = (((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, ALTO_SCREEN-texto_salir.get_rect()[3]-30))
             opcion_salir = True
        elif (pos_mouse[0] < 268 or pos_mouse[0] > 1010) or (pos_mouse[1] < 648 or pos_mouse[1] > 690):
            texto_salir = font_pequeña.render("VOLVER AL MENU PRINCIPAL", True, (255, 255, 255))
            texto_salir_pos = ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, ALTO_SCREEN-texto_salir.get_rect()[3]-30)
            opcion_salir = False


        #================================UPDATE============================
        surface.blit(imagen_fondo, (0, 0))

        #------------------Texto volver al menú principal
        surface.blit(texto_salir, texto_salir_pos)

        #------------------Cartas
        #--Cartas de los coches disponibles
        for i in range(0, 8):  # Dibujamos en el surface cada carta
            crear_carta(surface, lista_pos_cartas[i][0], lista_pos_cartas[i][1],"imagenes/coches/"+str(i)+".png",
                        lista_prop_coches[i][0], lista_prop_coches[i][1],lista_prop_coches[i][2], lista_prop_coches[i][3], lista_prop_coches[i][4])

        #--Botones de coches asignados
        i = 0
        for boton in lista_botones_asig_coche.values():  # Dibujamos en el surface cada botón
            surface.blit(boton.image, (boton.rect.x, boton.rect.y))
            i += 1

        #------------------Marcadores
     #   surface.blit(marcador_dinero_j1, (0, ALTO_SCREEN-marcador_dinero_j1.get_rect()[3]))
     #   surface.blit(marcador_dinero_j1, (ANCHO_SCREEN-marcador_dinero_j1.get_rect()[2], ALTO_SCREEN-marcador_dinero_j1.get_rect()[3]))

        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)



