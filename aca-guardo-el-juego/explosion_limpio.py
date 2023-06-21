from typing import Any
import pygame
#from pygame.sprite import _Group
import colores
import random
import sys
from constantes import *
from item_limpio import *
from bullet_limpio import *
from pantallas_limpio import *

class Explosion(pygame.sprite.Sprite):
    #EXPLOSION DE 2
    def __init__(self, x, y) -> None:
        super().__init__()
        self.fotogramas = getSuperficies("aca-guardo-el-juego/Explosion-1.png",1,4)#1,9
      
        #indice de  fotograma es igual a paso1
        self.paso1 = 0
        self.animacion = self.fotogramas
        self.image = self.animacion[self.paso1]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.tiempo_animacion = 100  # Duración de cada fotograma en milisegundos
        self.tiempo_transcurrido = 0
        

    def update(self):
      self.tiempo_transcurrido += 14# valor de 10 esta bien despues para gusto colores 20 tampoco esta mal
      if self.tiempo_transcurrido >= self.tiempo_animacion:
          self.tiempo_transcurrido = 0
          self.paso1 += 1
          if self.paso1 >= len(self.fotogramas):
            self.kill() # Elimina la explosión del grupo de sprites
          else:
            self.image = self.fotogramas[self.paso1]
            self.rect = self.image.get_rect(center=self.rect.center)  