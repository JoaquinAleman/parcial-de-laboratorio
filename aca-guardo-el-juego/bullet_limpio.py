from typing import Any
import pygame
#from pygame.sprite import _Group
import colores
import random
import sys
from constantes import *
#BULLETS ES EL GRUPO DE SPRITE POR ESO LO AGREGE AHI A LOS BULLET(DISPARO)
#AHORA VAMOS A PROBAR SI FUNCIONA EN UN GRUPO DE 2
#hasta aca llege tengo que hacer otro grupo de sprite para el bullet de los enemigos
#y shot enemigo lo tengo despues lo tengo que poner en las variables disaparo
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad, color) -> None:
        super().__init__()
        self.original_image = pygame.image.load("aca-guardo-el-juego/disparo.png")
        self.image = self.original_image.copy() 
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (6, 30))
        self.rect.y = y
        self.rect.centerx = x
        self.velocidady = velocidad     # 10 para abajo. -10 para arriba .
        self.color = color  #$
    def update(self):
        self.rect.y += self.velocidady   
        if self.rect.bottom < 0:
            self.kill()
    def cambiar_color(self):     #$
        self.image.fill(self.color)     #$