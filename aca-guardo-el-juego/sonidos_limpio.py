import pygame
import colores
from constantes import *

#ARCHIVO MP3 = MUSICA DE FONDO
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)

sonido_fondo = pygame.mixer.Sound("aca-guardo-el-juego/Blazing-star.mp3")
sonido_fondo.set_volume(0.2)

sonido_fondo2 = pygame.mixer.Sound("aca-guardo-el-juego/Rodeo-8bits.mp3")
sonido_fondo2.set_volume(0.2)

#### SONIDOS DE EFECTOS ESPECIALES
#nave
sonido_laser = pygame.mixer.Sound("aca-guardo-el-juego/sonido-laser.mp3")

#enemigo
sonido_laser_enemigo = pygame.mixer.Sound("aca-guardo-el-juego/sonido-laser-enemigo.mp3")
sonido_explosion = pygame.mixer.Sound("aca-guardo-el-juego/sonido-explosion.mp3")
#items
sonido_bonus = pygame.mixer.Sound("aca-guardo-el-juego/sonido-bonus.mp3")

