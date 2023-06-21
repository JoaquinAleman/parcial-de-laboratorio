import pygame
from pygame.locals import *
import sys
#constantes
ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ANCHO_NAVE = 100
ALTO_NAVE = 100

ANCHO_ENEMIGO = 50
ALTO_ENEMIGO = 50
FPS = 60

MEDIDAS_FONDO = (800,800)
flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.init()
reloj = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = reloj.tick(FPS)        




    pygame.display.flip()

