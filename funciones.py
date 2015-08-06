#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
import pygame.gfxdraw
import perfil
#====================================
#     ---------FUNCIONES---------
#====================================
def crear_carta(surface, pos_x, pos_y, imagen_coche, velocidad_max, aceleracion, turbo, manejo, frenada):
    """ Función que sirve para crear la carta que se mostrará en la tienda para cada coche """

    #------------------Rectángulos y fotos
    rect_fondo = pygame.gfxdraw.box(surface, (pos_x, pos_y, 230, 250), (30, 30, 30))  # Rectángulo negro del fondo

    rect_coches = pygame.gfxdraw.box(surface, (pos_x+10, pos_y+10, 210, 50), (120, 120, 120))  # Rectángulo gris para mostrar el coche

    coche_arriba = pygame.image.load(imagen_coche)  # Imagen del coche a 0º
    coche_derecha = pygame.transform.rotate(coche_arriba, 90)  # Imagen del coche a 90º
    coche_abajo = pygame.transform.rotate(coche_arriba, 180)  # Imagen del coche a 180º
    coche_izquierda = pygame.transform.rotate(coche_arriba, 270)  # Imagen del coche a 270º

    rect_propiedades = pygame.gfxdraw.box(surface, (pos_x+10, pos_y+80, 210, 150), (0, 150, 255))  # Rectángulo azul donde se pondrán las propiedades del coche

    #------------------Textos características
    font = pygame.font.Font("Prototype.TTF", 13)  # Font para las propiedades
    texto_velocidad_max = font.render("VELOCIDAD MÁX. : "+str(velocidad_max), True, (0, 255, 0))  # Velocidad máxima del coche
    texto_aceleracion = font.render("ACELERACIÓN : "+str(float(aceleracion)), True, (0, 255, 0))  # Aceleración del coche
    texto_turbo = font.render("TURBO : "+str(float(turbo)), True, (0, 255, 0))  # Turbo del coche
    texto_manejo = font.render("MANEJO : "+str(manejo), True, (0, 255, 0))  # Manejo del coche
    texto_frenada = font.render("FRENADA : "+str(float(frenada)), True, (0, 255, 0))  # Frenada del coche

    #================================UPDATE============================
    #------------------Imágenes coches
    surface.blit(coche_arriba, (pos_x+35, pos_y+15))
    surface.blit(coche_derecha, (pos_x+68, pos_y+25))
    surface.blit(coche_abajo, (pos_x+122.5, pos_y+15))
    surface.blit(coche_izquierda, (pos_x+155, pos_y+25))

    #------------------Textos características
    surface.blit(texto_velocidad_max, (pos_x+40, pos_y+85))
    surface.blit(texto_aceleracion, (pos_x+52, pos_y+115))
    surface.blit(texto_turbo, (pos_x+75, pos_y+145))
    surface.blit(texto_manejo, (pos_x+73, pos_y+175))
    surface.blit(texto_frenada, (pos_x+62, pos_y+205))


def iniciar_datos_jugador(jugador, tipo_coche, pos):
    """ Establecemos los datos de inicio de los jugadores (imagen, posición y velocidad) """

    # velocidad_max: Velocidad máxima a la que puede llegar a correr el coche
    # aceleracion: Cuanto más alto menos tarda en alcanzar la velocidad máxima
    # turbo: Velocidad extra
    # manejo: Capacidad para girar más en el menor tiempo posible
    # frenada: Capacidad para frenar más en menos tiempo
    jugador.velocidad_max, jugador.aceleracion, jugador.turbo, jugador.manejo, jugador.frenada = jugador.clases_coches[tipo_coche]

    jugador.posicion_imagen = 270
    jugador.images = crear_imagenes_coches(jugador, str(tipo_coche))
    jugador.rect.x, jugador.rect.y = pos
    jugador.velocidad = 0


def crear_imagenes_coches(jugador, imagen):
    """ Creamos las 360 imágenes de la imagen del coche """

    images = [pygame.image.load("imagenes/coches/"+imagen+".png")]
    for i in range(0, 360):
        images.append(pygame.transform.rotate(images[0], i*-1))  # Vamos rotando la imagen original iº y la almacenamos

    return images



