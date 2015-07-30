#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
#====================================
#     ---------COCHE---------
#====================================
pygame.init()
class Coche(pygame.sprite.Sprite):
    clases_coches = {0:(15, 1, 1.3, 6, 0.5), 1:(18, 1.5, 1.5, 7, 1), 2:(20, 2.5, 1.6, 7, 2), 3:(25, 2, 1.4, 4, 4), 4:(20, 4, 1.8, 9, 2.5),
                     5:(22, 3, 1.5, 6, 1.5), 6:(20, 3.5, 2.5, 8, 3), 7:(25, 5, 2, 10, 3)}

    def __init__(self, tipo_coche):
        pygame.sprite.Sprite.__init__(self)

        self.image_base = pygame.image.load("imagenes/coches/"+str(tipo_coche)+".png")
        self.images = []
        for i in range(0, 360):
            self.images.append(pygame.transform.rotate(self.image_base, i*-1))
        self.posicion_imagen = 270  # 360 posibles posiciones (arriba, abajo, izquierda, derecha y 2 diagonales en cada dirección)
        self.image = self.images[self.posicion_imagen]

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.corriendo = False  # Cuando 'aprieta el acelerador'
        self.frenando = False  # Cuando está frenando o yendo hacia atrás
        self.girando = False  # Cuando estás girando
        self.turbeando = False  # Verbo inventado xD, y significa que se está usando el turbo


        # velocidad_max: Velocidad máxima a la que puede llegar a correr el coche
        # aceleracion: Cuanto más alto menos tarda en alcanzar la velocidad máxima
        # turbo: Velocidad extra
        # manejo: Capacidad para girar más en el menor tiempo posible
        # frenada: Capacidad para frenar más en menos tiempo
        self.velocidad_max, self.aceleracion, self.turbo, self.manejo, self.frenada = self.clases_coches[tipo_coche]
        self.velocidad = 0  # Velocidad a la que está corriendo el coche

    def actualizar_movimiento(self):
        #------------------Calcular datos y cambiar variables (la velocidad, la posicion del coche...)
        #--Velocidades corriendo y frenando
        if self.corriendo == True:
            self.velocidad += self.aceleracion
            if self.velocidad > self.velocidad_max:
                self.velocidad = self.velocidad_max
            if self.turbeando == True and self.velocidad > 0:
                self.velocidad *= self.turbo
        elif self.corriendo == False and self.velocidad > 0:  # Ir parando poco a poco
            self.velocidad -= 0.5

        if self.frenando == True:
            self.velocidad -= self.frenada
            if self.velocidad < self.velocidad_max*-1:  # Cuando la velocidad es negativa (yendo hacia atrás)
                self.velocidad = self.velocidad_max*-1
        elif self.frenando == False and self.velocidad < 0:  # Ir parando poco a poco
            self.velocidad += 0.5

        if self.velocidad < 0.5 and self.velocidad > -0.5:  # Por si quedan números 'raros' al usar el turbo
            self.velocidad = 0

        #--Giros del coche
        if self.velocidad != 0 and self.turbeando == False:
            if self.girando == 'derecha':
                self.posicion_imagen += self.manejo
                if self.posicion_imagen > 359:
                    self.posicion_imagen = 0
            elif self.girando == 'izquierda':
                self.posicion_imagen -= self.manejo
                if self.posicion_imagen < 0:
                    self.posicion_imagen = 359

        #------------------Aplicar los cambios según la imagen que toque (se calcula la velocidad * un número entre 0 y 1)
        if self.posicion_imagen < 91:
            self.rect.x += round(self.velocidad*(self.posicion_imagen*1.111/100), 2)
            self.rect.y -= round(self.velocidad*(1-self.posicion_imagen*1.111/100), 2)
        elif self.posicion_imagen < 181:
            self.rect.x += round(self.velocidad*(1-(self.posicion_imagen-90)*1.111/100), 2)
            self.rect.y += round(self.velocidad*((self.posicion_imagen-90)*1.111/100), 2)
        elif self.posicion_imagen < 271:
            self.rect.x -= round(self.velocidad*((self.posicion_imagen-180)*1.111/100), 2)
            self.rect.y += round(self.velocidad*(1-(self.posicion_imagen-180)*1.111/100), 2)
        elif self.posicion_imagen < 361:
            self.rect.x -= round(self.velocidad*(1-(self.posicion_imagen-270)*1.111/100), 2)
            self.rect.y -= round(self.velocidad*((self.posicion_imagen-270)*1.111/100), 2)

        self.image = self.images[self.posicion_imagen]

        #------------------Ajustar la posición
        if self.rect.x < 0:
            self.rect.x = 0
            self.velocidad = 0
        elif self.rect.x+self.image.get_rect()[2] > ANCHO_SCREEN:
            self.rect.x = ANCHO_SCREEN-self.image.get_rect()[2]
            self.velocidad = 0

        if self.rect.y < 0:
            self.rect.y = 0
            self.velocidad = 0
        elif self.rect.y+self.image.get_rect()[3] > ALTO_SCREEN:
            self.rect.y = ALTO_SCREEN-self.image.get_rect()[3]
            self.velocidad = 0

