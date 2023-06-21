from typing import Any
import pygame
#from pygame.sprite import _Group
import colores
import random
import sys
from constantes import *
from item_limpio import *
from bullet_limpio import *
from sprite_group_limpio import *


class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("aca-guardo-el-juego/Galaga-enemigo1.png").convert()
        self.image.set_colorkey(colores.BLACK)
        self.image = pygame.transform.scale(self.image,(ANCHO_ENEMIGO, ALTO_ENEMIGO))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(ANCHO_VENTANA - self.rect.width)# que aparescan en cualquier lugar
        self.rect.y = random.randrange(-150,-100) #desde donde salen los enemigo osae su punto de partida
        self.velocidad_y = random.randrange(1,5) #esta es una velocidad aleatoria que caen
        self.velocidad_x = random.randrange(-5,5) # velocidad del ancho que caen
        #DE DONDE SALE LA BALA
        self.rect.centerx = ANCHO_VENTANA // 2
        #desde aca      aranqueeee   
        self.disparado = False  # Bandera para controlar el disparo


    def update(self):
        self.rect.y += self.velocidad_y    
        self.rect.x += self.velocidad_x
        #si ya salio de la ventana            o si ya salio por la izquierda o si salio por la derecha DE LA VENTANA
        if self.rect.top > ALTO_VENTANA + 10 or self.rect.left < -25 or  self.rect.right > ANCHO_VENTANA + 25:
            self.rect.y = random.randrange(-100,-40) #desde donde salen los enemigo osae su punto de partida
            self.velocidad_y = random.randrange(1,5) #esta es una velocidad aleatoria que caen
            self.velocidad_x = random.randrange(-5,5)
            self.disparado = False  # Reinicia la bandera al salir de la pantalla

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom, 10, (colores.RED1))  # proyectil para abajo
        bullet.cambiar_color() # para cambiar el color
        all_sprites.add(bullet)
        bullets.add(bullet)     # aca actualizo la clase   
        self.disparado = True  # Establece la bandera a True después del primer disparo     



##########################           ITEM BONUS
    def item_bonus(self):
        bonus = Items(self.rect.centerx, self.rect.bottom)  # proyectil para abajo
        all_sprites.add(bonus)
        bonuss.add(bonus)  

