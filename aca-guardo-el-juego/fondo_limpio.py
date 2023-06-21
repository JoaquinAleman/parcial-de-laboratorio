import pygame
import colores
from constantes import *

#es el que se mueve
class FondoJuego:
    def __init__(self, ruta, medidas) -> None:
       self.imagen = pygame.image.load(ruta)
       self.imagen = pygame.transform.scale(self.imagen, medidas)
       self.rect = self.imagen.get_rect()

    def mostrar(self, pantalla, x, y):
        y_relativa = y % self.rect.height
        pantalla.blit(self.imagen,(x, y_relativa - self.rect.height))
        if y_relativa < pantalla.get_rect().height:
            pantalla.blit(self.imagen, (x, y_relativa))
        y += 1



#es el que esta quieto lo uso para Start-opciones
class FondoPantalla:
    def __init__(self, ruta, medidas) -> None:
       self.imagen = pygame.image.load(ruta)
       self.imagen = pygame.transform.scale(self.imagen, medidas)
       self.rect = self.imagen.get_rect()
       self.rect.y = POS_TOP_BOTON
       self.rect.x = POST_LEFT_BOTON

    def mostrar(self, pantalla, x, y):
        pantalla.blit(self.imagen, (x, y))
    
           
#tranfomarciaoi de scala = https://www.pygame.org/docs/ref/transform.html#pygame.transform.flip
