#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import tienda
import tutorial
#====================================
#     ---------MENÚS---------
#====================================
pygame.init()

def menu_inicio(surface, fps_clock):
    """ Menú que hay al inicio del juego (menú principal) """
    imagen_fondo = pygame.image.load("imagenes/wallpaper.png")  # Fondo del menú principal

    opcion_menu = 0  # Contador para saber que opción se está seleccionado (JUGAR, TIENDA, SALIR)
    font_pequeña = pygame.font.Font("Xperia.TTF", 60)  # Font para las opciones no seleccionadas
    font_grande = pygame.font.Font("Xperia.TTF", 90)  # Font para la opción seleccionada

    #================================BUCLE============================
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:  # Ir seleccionando la opción del menú
                if event.key == K_UP or event.key == K_w:  # Si le da a una tecla de subir
                    opcion_menu -= 1
                    if opcion_menu < 0:
                        opcion_menu = 3
                elif event.key == K_DOWN or event.key == K_s:  # Si le da a una tecla de bajar
                    opcion_menu += 1
                    if opcion_menu > 3:
                        opcion_menu = 0
                elif event.key == K_RETURN:  # Si le da a la tecla enter
                    if opcion_menu == 0:  # Si está seleccionando la opción de jugar
                        return  # Cierra el menu y en inicio.py pasa a juego.py
                    elif opcion_menu == 1:  # Si está seleccionando la opción de ir a la tienda
                        tienda.tienda(surface, fps_clock)
                    elif opcion_menu == 2:
                        tutorial.tutorial(surface, fps_clock)
                    else:  # Si está seleccionado la opción de salir
                        pygame.quit()
                        sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if (event.pos[0] > 157 and event.pos[0] < 538) and (event.pos[1] > 53 and event.pos[1] < 120) and opcion_menu == 0:  # Opción jugar
                    return  # Cierra el menu y en inicio.py pasa a juego.py
                elif (event.pos[0] > 157 and event.pos[0] < 555) and (event.pos[1] > 130 and event.pos[1] < 195) and opcion_menu == 1:  # Opción tienda
                    tienda.tienda(surface, fps_clock)
                elif (event.pos[0] > 157 and event.pos[0] < 724) and (event.pos[1] > 184 and event.pos[1] < 250) and opcion_menu == 2:  # Opción tutorial
                    tutorial.tutorial(surface, fps_clock)
                elif (event.pos[0] > 157 and event.pos[0] < 42391) and (event.pos[1] > 240 and event.pos[1] < 306) and opcion_menu == 3:  # Opción salir
                    pygame.quit()
                    sys.exit()


        pos_mouse = pygame.mouse.get_pos()
        if pos_mouse[0] > 95 and pos_mouse[0] < 353 and pos_mouse[1] > 49 and pos_mouse[1] < 98:  # Opción jugar
            opcion_menu = 0
        elif (pos_mouse[0] > 95 and pos_mouse[0] < 360) and ((pos_mouse[1] > 153 and pos_mouse[1] < 196 and opcion_menu == 0) or (pos_mouse[1] > 108 and pos_mouse[1] < 151 and (opcion_menu == 2 or opcion_menu == 3))):  # Opción tienda
            opcion_menu = 1
        elif (pos_mouse[0] > 95 and pos_mouse[0] < 470) and ((pos_mouse[1] > 209 and pos_mouse[1] < 251 and opcion_menu == 0) or (pos_mouse[1] > 229 and pos_mouse[1] < 271 and opcion_menu == 1) or (pos_mouse[1] > 164 and pos_mouse[1] < 208 and opcion_menu == 3)):  # Opción tutorial
            opcion_menu = 2
        elif (pos_mouse[0] > 95 and pos_mouse[0] < 317) and ((pos_mouse[1] > 264 and pos_mouse[1] < 306 and opcion_menu == 0) or (pos_mouse[1] > 284 and pos_mouse[1] < 326 and (opcion_menu == 1 or opcion_menu == 2))):  # Opción salir
            opcion_menu = 3

        #------------------Definir el tamaño y la posición de cada opción del menú dependiendo de que opción esté seleccionada
        if opcion_menu == 0:  # Opción jugar
            texto_jugar, texto_jugar_pos = font_grande.render("JUGAR", True, (255, 255, 255)), (150, 50)
            texto_tienda, texto_tienda_pos = font_pequeña.render("TIENDA", True, (200, 200, 200)), (90, 150)
            texto_tutorial, texto_tutorial_pos = font_pequeña.render("TUTORIAL", True, (200, 200, 200)), (90, 205)
            texto_salir, texto_salir_pos = font_pequeña.render("SALIR", True, (200, 200, 200)), (90, 260)

        elif opcion_menu == 1:  # Opción tienda
            texto_jugar, texto_jugar_pos = font_pequeña.render("JUGAR", True, (200, 200, 200)), (90, 50)
            texto_tienda, texto_tienda_pos = font_grande.render("TIENDA", True, (255, 255, 255)), (150, 125)
            texto_tutorial, texto_tutorial_pos = font_pequeña.render("TUTORIAL", True, (200, 200, 200)), (90, 225)
            texto_salir, texto_salir_pos = font_pequeña.render("SALIR", True, (200, 200, 200)), (90, 280)

        elif opcion_menu == 2:  # Opción tutorial
            texto_jugar, texto_jugar_pos = font_pequeña.render("JUGAR", True, (200, 200, 200)), (90, 50)
            texto_tienda, texto_tienda_pos = font_pequeña.render("TIENDA", True, (200, 200, 200)), (90, 105)
            texto_tutorial, texto_tutorial_pos = font_grande.render("TUTORIAL", True, (255, 255, 255)), (150, 180)
            texto_salir, texto_salir_pos = font_pequeña.render("SALIR", True, (200, 200, 200)), (90, 280)

        else:  # Opción salir
            texto_jugar, texto_jugar_pos = font_pequeña.render("JUGAR", True, (200, 200, 200)), (90, 50)
            texto_tienda, texto_tienda_pos = font_pequeña.render("TIENDA", True, (200, 200, 200)), (90, 105)
            texto_tutorial, texto_tutorial_pos = font_pequeña.render("TUTORIAL", True, (200, 200, 200)), (90, 160)
            texto_salir, texto_salir_pos = font_grande.render("SALIR", True, (255, 255, 255)), (90, 235)


        #================================UPDATE============================
        surface.blit(imagen_fondo, (0, 0))

        #------------------Menú
        surface.blit(texto_jugar, texto_jugar_pos)
        surface.blit(texto_tienda, texto_tienda_pos)
        surface.blit(texto_tutorial, texto_tutorial_pos)
        surface.blit(texto_salir, texto_salir_pos)

        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)



def menu_pausa(surface, fps_clock):
    """ Menú que hay cuando pausas el juego estando en medio de una carrera """
    imagen_fondo = pygame.image.load("imagenes/wallpaper_pausa.png")  # Imagen de fondo del menú

    opcion_menu = 0  # Contador que dice si estás marcando REANUDAR o SALIR
    font_pequeña = pygame.font.Font("Xperia.TTF", 60)  # Font para la opción seleccionada
    font_grande = pygame.font.Font("Xperia.TTF", 90)  # Font para la opción no seleccionada

    #================================BUCLE============================
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:  # Ir seleccionando la opción del menú
                if event.key == K_UP or event.key == K_w:  # Si le da a una tecla de bajar
                    opcion_menu -= 1
                    if opcion_menu < 0:
                        opcion_menu = 1
                elif event.key == K_DOWN or event.key == K_s:  # Si le da a una tecla de subir
                    opcion_menu += 1
                    if opcion_menu > 1:
                        opcion_menu = 0
                elif event.key == K_RETURN:  # Si le da al enter
                    if opcion_menu == 0:  # Si la opción es reanudar
                        return  # Cierra el menú y eanuda el juego
                    else:  # Si la opción es salir
                        menu_inicio(surface, fps_clock)
                        return  True # Devuelve a juego.py el dato de que ha salido, así se sabe que si se vuelve a iniciar juego.py hay que reiniciar los datos

            elif event.type == MOUSEBUTTONDOWN:
                if (event.pos[0] > 331 and event.pos[0] < 949) and (event.pos[1] > 249 and event.pos[1] < 342) and opcion_menu == 0:  # Opción reanudar
                    return  # Reanuda el juego
                elif (event.pos[0] > 469 and event.pos[0] < 811) and (event.pos[1] > 379 and event.pos[1] < 472) and opcion_menu == 1:  # Opción salir
                    menu_inicio(surface, fps_clock)
                    return  True # Devuelve a juego.py el dato de que ha salido, así se sabe que si se vuelve a iniciar juego.py hay que reiniciar los datos


        pos_mouse = pygame.mouse.get_pos()
        if (pos_mouse[0] > 433 and pos_mouse[0] < 846) and (pos_mouse[1] > 249 and pos_mouse[1] < 312):  # Opción reanudar
            opcion_menu = 0
        elif (pos_mouse[0] > 526 and pos_mouse[0] < 754) and (pos_mouse[1] > 379 and pos_mouse[1] < 442):  # Opción salir
            opcion_menu = 1

        #------------------Definir el tamaño y la posición de cada opción del menú dependiendo de la opción seleccionada
        if opcion_menu == 0:  # Opción reanudar
            texto_reanudar = font_grande.render("REANUDAR", True, (255, 255, 255))
            texto_reanudar_pos = ((ANCHO_SCREEN-texto_reanudar.get_rect()[2])//2, 250)

            texto_salir = font_pequeña.render("SALIR", True, (200, 200, 200))
            texto_salir_pos = ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 380)

        else:  # Opción salir
            texto_reanudar = font_pequeña.render("REANUDAR", True, (200, 200, 200))
            texto_reanudar_pos = ((ANCHO_SCREEN-texto_reanudar.get_rect()[2])//2, 250)

            texto_salir = font_grande.render("SALIR", True, (255, 255, 255))
            texto_salir_pos = ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 380)

        #================================UPDATE============================
        surface.blit(imagen_fondo, (0, 0))

        #------------------Menú
        surface.blit(texto_reanudar, texto_reanudar_pos)
        surface.blit(texto_salir, texto_salir_pos)

        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)