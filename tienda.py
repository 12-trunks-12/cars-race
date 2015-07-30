#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
import perfil
from funciones import crear_carta

#====================================
#     ---------MAPA---------
#====================================
pygame.init()
def tienda(surface, fps_clock):
    imagen_fondo = pygame.image.load("imagenes/wallpaper_tienda.png")

    font_pequeña = pygame.font.Font("Xperia.TTF", 30)
    font_grande = pygame.font.Font("Xperia.TTF", 40)

   # marcador_dinero_j1 = pygame.image.load("imagenes/marcador_dinero.png")
   # marcador_dinero_j2 = pygame.transform.flip(1, 0)

    #imagen_dinero = pygame.image.load("imagenes/dinero.png")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if (event.pos[0] > 268 and event.pos[0] < 1010) and (event.pos[1] > 648 and event.pos[1] < 690) and opcion_salir == True:
                    return  # Vuelve al menú principal
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return  # Vuelve al menú principal


        pos_mouse = pygame.mouse.get_pos()
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
        surface.blit(texto_salir, texto_salir_pos)

        #------------------Cartas
        lista_coches = [(15, 1, 1.3, 6, 0.5), (18, 1.5, 1.5, 7, 1), (20, 2.5, 1.6, 7, 2), (25, 2, 1.4, 4, 4),
                        (20, 4, 1.8, 9, 2.5), (22, 3, 1.5, 6, 1.5), (20, 3.5, 2.5, 8, 3), (25, 5, 2, 10, 3)]
        lista_pos_cartas = [(75, 30), (375, 30), (675, 30), (975, 30), (75, 340), (375, 340), (675, 340), (975, 340)]
        for i in range(0, 8):
            lista_coches.append(crear_carta(surface, lista_pos_cartas[i][0], lista_pos_cartas[i][1],
                                            "imagenes/coches/"+str(i)+".png", lista_coches[i][0], lista_coches[i][1],
                                            lista_coches[i][2], lista_coches[i][3], lista_coches[i][4], False))


        #------------------Marcadores
       # surface.blit(marcador_dinero_j1, (0, ALTO_SCREEN-marcador_dinero_j1.get_rect()[3]))
      #  surface.blit(marcador_dinero_j1, (ANCHO_SCREEN-marcador_dinero_j1.get_rect()[2], ALTO_SCREEN-marcador_dinero_j1.get_rect()[3]))

        #------------------Update, FPS
        pygame.display.update()
        fps_clock.tick(FPS)



