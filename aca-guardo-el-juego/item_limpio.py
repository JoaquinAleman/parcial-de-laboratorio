from typing import Any
import pygame
#from pygame.sprite import _Group
import colores
import random
import sys
from constantes import *

class Items(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load("aca-guardo-el-juego/bonus-item.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.velocidady = 10     # 10 para abajo. -10 para arriba .

    def update(self):
        self.rect.y += self.velocidady   
        if self.rect.bottom < 0:
            self.kill()