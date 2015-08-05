#====================================
#     ---------IMPORTS---------
#====================================
import pygame, sys
from pygame.locals import *
from constantes import *
from funciones import crear_imagenes_coches
#====================================
#     ---------COCHE---------
#====================================
pygame.init()
class Coche(pygame.sprite.Sprite):
    clases_coches = {0:(15, 1, 1.3, 6, 0.5), 1:(18, 1.5, 1.5, 7, 1), 2:(20, 2.5, 1.6, 7, 2), 3:(25, 2, 1.4, 4, 4), 4:(20, 4, 1.8, 9, 2.5),
                     5:(22, 3, 1.5, 6, 1.5), 6:(20, 3.5, 2.5, 8, 3), 7:(25, 5, 2, 10, 3)}  # Almacenamos cada coche con sus características

    def __init__(self, tipo_coche):
        pygame.sprite.Sprite.__init__(self)

        self.images = crear_imagenes_coches(self, str(tipo_coche))
        self.posicion_imagen = 270  # 360 posibles posiciones (arriba, abajo, izquierda, derecha y 2 diagonales en cada dirección)
        self.image = self.images[self.posicion_imagen+1]  # Imagen actual

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
        """ Calculamos su nueva posición, la ajustamos si es necesario y actualizamos la imagen"""

        #------------------Calcular datos y cambiar variables (la velocidad, la posicion del coche...)
        #--Velocidades corriendo y frenando
        if self.corriendo == True:  # Si está corriendo (hacia delante)
            self.velocidad += self.aceleracion  # Sumamos a su velocidad actual su aceleración
            if self.velocidad > self.velocidad_max:  # Si la velocidad sobrepasa la velocidad máxima
                self.velocidad = self.velocidad_max  # Limitamos la velocidad a la velocidad máxima
            if self.turbeando == True and self.velocidad > 0:  # Si está usando el turbo en movimiento (hacia delante)
                self.velocidad *= self.turbo  # Multiplicamos la velocidad por el turbo
        elif self.corriendo == False and self.velocidad > 0:  # Ir parando poco a poco
            self.velocidad -= 0.5  # Se reduce la velocidad

        if self.frenando == True:  # Si está frenando
            self.velocidad -= self.frenada  # Se le resta la velocidad su frenada
            if self.velocidad < self.velocidad_max*-1:  # Cuando la velocidad es negativa (yendo hacia atrás) y sobrepasa la velocidad máxima
                self.velocidad = self.velocidad_max*-1  # Limitamos la velocidad hacia atrás a la velocidad máxima
        elif self.frenando == False and self.velocidad < 0:  # Ir parando poco a poco
            self.velocidad += 0.5  # Se va sumando la velocidad

        if self.velocidad < 0.5 and self.velocidad > -0.5:  # Parar el coche, en caso de que al sumar o reducir queden número decimales
            self.velocidad = 0

        #--Giros del coche
        if self.velocidad != 0 and self.turbeando == False:  # Si se está moviendo y no está usando el turbo
            if self.girando == 'derecha':  # Si gira hacia la derecha
                self.posicion_imagen += self.manejo  # Se suman los grados
                if self.posicion_imagen > 359:  # Si sobrepasa los 359º
                    self.posicion_imagen = 0  # Se vuelve a poner a 0º
            elif self.girando == 'izquierda':  # Si gira hacia la izquierda
                self.posicion_imagen -= self.manejo  # Se le restan los grados
                if self.posicion_imagen < 0:  # Si los grados son menores de 0
                    self.posicion_imagen = 359  # Se ponen a 359º

        #------------------Aplicar los cambios según la imagen que toque
        # Para calcular la x se multiplica la velocidad por un decimal entre 0 y 1, dependiendo de si la imagen es mas horizontal o vertical
        # Para calcular la y se le resta a 1 la velocidad que da para x
        # Además, se añaden a parte los grados 90, 180 y 270 para que no haga ningún movimiento erróneo debido a pequeños restos que quedan (de 0.01)
        # que al final si se prolonga el movimiento termina por echarse hacia un lado el coche

        if self.posicion_imagen < 90:  # Si la imagen corresponde a 0-89º
            self.rect.x += round(self.velocidad*(self.posicion_imagen*1.111/100), 2)
            self.rect.y -= round(self.velocidad*(1-self.posicion_imagen*1.111/100), 2)
        elif self.posicion_imagen == 90:
            self.rect.x += round(self.velocidad, 2)
            self.rect.y -= 0
        elif self.posicion_imagen < 180:  # Si la imagen corresponde a 91-179º
            self.rect.x += round(self.velocidad*(1-(self.posicion_imagen-90)*1.111/100), 2)
            self.rect.y += round(self.velocidad*((self.posicion_imagen-90)*1.111/100), 2)
        elif self.posicion_imagen == 180:
            self.rect.x += 0
            self.rect.y += round(self.velocidad, 2)
        elif self.posicion_imagen < 270:  # Si la imagen corresponde a 181-269º
            self.rect.x -= round(self.velocidad*((self.posicion_imagen-180)*1.111/100), 2)
            self.rect.y += round(self.velocidad*(1-(self.posicion_imagen-180)*1.111/100), 2)
        elif self.posicion_imagen == 270:
            self.rect.x -= round(self.velocidad, 2)
            self.rect.y += 0
        elif self.posicion_imagen < 360:  # Si la imagen corresponde a 271-359º
            self.rect.x -= round(self.velocidad*(1-(self.posicion_imagen-270)*1.111/100), 2)
            self.rect.y -= round(self.velocidad*((self.posicion_imagen-270)*1.111/100), 2)

        self.image = self.images[self.posicion_imagen+1]  # Se actualiza la imagen del coche

        #------------------Ajustar la posición
        if self.rect.x < 0:  # Si choca contra la "pared" izquierda
            self.rect.x = 0
            self.velocidad = 0
        elif self.rect.x+self.image.get_rect()[2] > ANCHO_SCREEN:  # Si choca contra la "pared" derecha
            self.rect.x = ANCHO_SCREEN-self.image.get_rect()[2]
            self.velocidad = 0

        if self.rect.y < 0:  # Si choca contra el "suelo"
            self.rect.y = 0
            self.velocidad = 0
        elif self.rect.y+self.image.get_rect()[3] > ALTO_SCREEN:  # Si choca con el "techo"
            self.rect.y = ALTO_SCREEN-self.image.get_rect()[3]
            self.velocidad = 0

