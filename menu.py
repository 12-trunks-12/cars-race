#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import tienda

#====================================
#     ---------MENÚS---------
#====================================
pygame.init()

def menu_inicio(surface, fps_clock):
    imagen_fondo = pygame.image.load("imagenes/wallpaper.png")

    opcion_menu = 0
    font_pequeña = pygame.font.Font("Xperia.TTF", 60)
    font_grande = pygame.font.Font("Xperia.TTF", 90)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    opcion_menu -= 1
                    if opcion_menu < 0:
                        opcion_menu = 2
                elif event.key == K_DOWN or event.key == K_s:
                    opcion_menu += 1
                    if opcion_menu > 2:
                        opcion_menu = 0
                elif event.key == K_RETURN:
                    if opcion_menu == 0:
                        return  # Cierra el menu y en inicio.py pasa a juego.py
                    elif opcion_menu == 1:
                        tienda.tienda(surface, fps_clock)
                    else:
                        pygame.quit()
                        sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if (event.pos[0] > 149 and event.pos[0] < 546) and (event.pos[1] > 49 and event.pos[1] < 142) and opcion_menu == 0:
                    return  # Cierra el menu y en inicio.py pasa a juego.py
                elif (event.pos[0] > 149 and event.pos[0] < 564) and (event.pos[1] > 124 and event.pos[1] < 217) and opcion_menu == 1:
                    tienda.tienda(surface, fps_clock)
                elif (event.pos[0] > 149 and event.pos[0] < 491) and (event.pos[1] > 179 and event.pos[1] < 272) and opcion_menu == 2:
                    pygame.quit()
                    sys.exit()


        pos_mouse = pygame.mouse.get_pos()
        if ((pos_mouse[0] > 89 and pos_mouse[0] < 353) and (pos_mouse[1] > 49 and pos_mouse[1] < 112)):
            opcion_menu = 0
        elif ((pos_mouse[0] > 89 and pos_mouse[0] < 366) and (pos_mouse[1] > 149 and pos_mouse[1] < 212)) or ((pos_mouse[0] > 89 and pos_mouse[0] < 366) and (pos_mouse[1] > 104 and pos_mouse[1] < 167)):
            opcion_menu = 1
        elif ((pos_mouse[0] > 89 and pos_mouse[0] < 317) and (pos_mouse[1] > 204 and pos_mouse[1] < 267)) or ((pos_mouse[0] > 89 and pos_mouse[0] < 317) and (pos_mouse[1] > 224 and pos_mouse[1] < 287)):
            opcion_menu = 2

        #------------------Definir el tamaño y la posición de cada opción del menú
        if opcion_menu == 0:
            texto_jugar, texto_jugar_pos = font_grande.render("JUGAR", True, (255, 255, 255)), (150, 50)
            texto_tienda, texto_tienda_pos = font_pequeña.render("TIENDA", True, (200, 200, 200)), (90, 150)
            texto_salir, texto_salir_pos = font_pequeña.render("SALIR", True, (200, 200, 200)), (90, 205)

        elif opcion_menu == 1:
            texto_jugar, texto_jugar_pos = font_pequeña.render("JUGAR", True, (200, 200, 200)), (90, 50)
            texto_tienda, texto_tienda_pos = font_grande.render("TIENDA", True, (255, 255, 255)), (150, 125)
            texto_salir, texto_salir_pos = font_pequeña.render("SALIR", True, (200, 200, 200)), (90, 225)

        else:
            texto_jugar, texto_jugar_pos = font_pequeña.render("JUGAR", True, (200, 200, 200)), (90, 50)
            texto_tienda, texto_tienda_pos = font_pequeña.render("TIENDA", True, (200, 200, 200)), (90, 105)
            texto_salir, texto_salir_pos = font_grande.render("SALIR", True, (255, 255, 255)), (150, 180)


        #================================UPDATE============================
        surface.blit(imagen_fondo, (0, 0))

        #------------------Menú
        surface.blit(texto_jugar, texto_jugar_pos)
        surface.blit(texto_tienda, texto_tienda_pos)
        surface.blit(texto_salir, texto_salir_pos)

        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)



def menu_pausa(surface, fps_clock):
    imagen_fondo = pygame.image.load("imagenes/wallpaper_pausa.png")

    opcion_menu = 0  # Si estás marcando REANUDAR, TIENDA O SALIR
    font_pequeña = pygame.font.Font("Xperia.TTF", 60)
    font_grande = pygame.font.Font("Xperia.TTF", 90)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    opcion_menu -= 1
                    if opcion_menu < 0:
                        opcion_menu = 1
                elif event.key == K_DOWN or event.key == K_s:
                    opcion_menu += 1
                    if opcion_menu > 1:
                        opcion_menu = 0
                elif event.key == K_RETURN:
                    if opcion_menu == 0:
                        return  # Reanuda el juego
                    else:
                        menu_inicio(surface, fps_clock)
                        return  # Para que cuando se cierre el menu inicio no siga este abierto

            elif event.type == MOUSEBUTTONDOWN:
                if (event.pos[0] > 331 and event.pos[0] < 949) and (event.pos[1] > 249 and event.pos[1] < 342) and opcion_menu == 0:
                    return  # Reanuda el juego
                elif (event.pos[0] > 469 and event.pos[0] < 811) and (event.pos[1] > 379 and event.pos[1] < 472) and opcion_menu == 1:
                    menu_inicio(surface, fps_clock)
                    return  # Para que cuando se cierre el menu inicio no siga este abierto


        pos_mouse = pygame.mouse.get_pos()
        if (pos_mouse[0] > 433 and pos_mouse[0] < 846) and (pos_mouse[1] > 249 and pos_mouse[1] < 312):
            opcion_menu = 0
        elif (pos_mouse[0] > 526 and pos_mouse[0] < 754) and (pos_mouse[1] > 379 and pos_mouse[1] < 442):
            opcion_menu = 1

        #------------------Definir el tamaño y la posición de cada opción del menú
        if opcion_menu == 0:
            texto_reanudar = font_grande.render("REANUDAR", True, (255, 255, 255))
            texto_reanudar_pos = ((ANCHO_SCREEN-texto_reanudar.get_rect()[2])//2, 250)

            texto_salir = font_pequeña.render("SALIR", True, (200, 200, 200))
            texto_salir_pos = ((ANCHO_SCREEN-texto_salir.get_rect()[2])//2, 380)

        else:
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