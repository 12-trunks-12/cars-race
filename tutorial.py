#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
from boton import Boton
#====================================
#     ---------TUTORIAL---------
#====================================
pygame.init()

def tutorial(surface, fps_clock):
    """ Tutorial con especificaciones de como usar la tienda y de como jugar """

    contador_imagen = 0  # Contador para ir pasando de imagen
    lista_imagenes = []  # Lista con todas las imágenes para el tutorial
    for i in range(5):  # Añadimos todas las imágenes del tutorial a la lista
        lista_imagenes.append(pygame.image.load("imagenes/tutorial/"+str(i)+".png"))
    imagen_actual = lista_imagenes[0]  # Imagen que se está mostrando actualmente en el tutorial

    boton_flecha_der = Boton("boton_flecha_tutorial", (1150, 680))  # Botón para avanzar en el tutorial
    boton_flecha_izq = Boton("boton_flecha_tutorial", (82, 680)) # Botón para retroceder en el tutorial
    boton_flecha_izq.image = pygame.transform.flip(boton_flecha_izq.image, 1, 0)

    #================================BUCLE============================
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_RETURN or event.key == K_RIGHT or event.key == K_d:  # Si quiere avanzar en el tutorial
                    contador_imagen += 1  # Se suma uno a la imagen a mostrar
                    if contador_imagen > len(lista_imagenes)-1:  # Si llega al final de las imágenes
                        return
                elif event.key == K_LEFT or event.key == K_a:
                    contador_imagen -= 1
                    if contador_imagen < 0:
                        contador_imagen = 0
                elif event.key == K_ESCAPE:  # Si quiere salir del tutorial
                    return

            elif event.type == MOUSEBUTTONDOWN:
                if event.pos[0] > 80 and event.pos[0] < 130 and event.pos[1] > 678 and event.pos[1] < 703:  # Si pulsa en el botón derecho
                    contador_imagen -= 1
                    if contador_imagen < 0:  # Si el contador es menor que 0 no se le deja darle más para atrás
                        contador_imagen = 0
                elif event.pos[0] > 1149 and event.pos[0] < 1199 and event.pos[1] > 678 and event.pos[1] < 703:  # Si pulsa en el botón izquierdo
                    contador_imagen += 1
                    if contador_imagen > len(lista_imagenes)-1:  # Si llega al final de las imágenes
                        return


        imagen_actual = lista_imagenes[contador_imagen]

        #================================UPDATE============================
        surface.fill((0, 0, 0))

        #------------------Imágenes del tutorial
        surface.blit(imagen_actual, ((ANCHO_SCREEN-imagen_actual.get_rect()[2])//2, (ALTO_SCREEN-imagen_actual.get_rect()[3])//2))

        #------------------Botones
        surface.blit(boton_flecha_der.image, (boton_flecha_der.rect.x, boton_flecha_der.rect.y))
        surface.blit(boton_flecha_izq.image, (boton_flecha_izq.rect.x, boton_flecha_izq.rect.y))

        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)


