from typing import Any
import pygame
#from pygame.sprite import _Group
import colores
import random
import sys
from constantes import *
from bullet_limpio import *
from sprite_group_limpio import *


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("aca-guardo-el-juego/Galaga-avion-principal.png").convert()
        #self.image.set_colorkey(colores.BLACK)
        self.image = pygame.transform.scale(self.image,(ANCHO_NAVE, ALTO_NAVE))
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO_VENTANA // 2
        self.rect.bottom = ALTO_VENTANA - 10
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.salud = 100

    def update(self):
        self.velocidad_x = 0
        self.velocidad_y = 0
        estado = pygame.key.get_pressed()
        #posicion x
        if estado[pygame.K_LEFT]:
            self.velocidad_x = -5
        if estado[pygame.K_RIGHT]:
            self.velocidad_x = 5
        self.rect.x += self.velocidad_x
        #posicion y
        if estado[pygame.K_DOWN]:
           self.velocidad_y = 5
        if estado[pygame.K_UP]:
            self.velocidad_y = -5
        self.rect.y += self.velocidad_y
        
        # limites de personaje
        if self.rect.right > ANCHO_VENTANA: #derecha
            self.rect.right = ANCHO_VENTANA
        if self.rect.left < 0:  #izquierda
            self.rect.left = 0
  
        if self.rect.bottom > ALTO_VENTANA: #abajo
            self.rect.bottom = ALTO_VENTANA
            
        if self.rect.top < 0:   #arriba
            self.rect.top = 0  

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, -10, (colores.AQUA)) #proyectil para arriba
        bullet.cambiar_color()  # para cambiar el color
        all_sprites.add(bullet)
        bullets_amigo.add(bullet)

player = Nave()     
all_sprites.add(player)   
