from typing import Any
import pygame
#from pygame.sprite import _Group
import colores
import random
import sys
from fondo_limpio import *
from constantes import *
from sonidos_limpio import *
import sqlite3

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ANCHO_NAVE = 100
ALTO_NAVE = 100

ANCHO_ENEMIGO = 50
ALTO_ENEMIGO = 50

MEDIDAS_FONDO = (800,800)
#dcon esto controlo los fps fps FPS = 30
ALTO_FONDO = 800
ANCHO_FONDO = 800



fondo_guardianes = FondoPantalla("aca-guardo-el-juego/fondo-guardianes-de-la-galaxia.jpg",MEDIDAS_FONDO)
fondo_principal = FondoJuego("fondo_galaxia.png",MEDIDAS_FONDO)
posicion_fondo = 0 # Variable para rastrear la posición vertical del fondo

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego de naves")
reloj = pygame.time.Clock()
inicio_tiempo = pygame.time.get_ticks()
#20/6 MODIFIQUE LOS TIEMPOS DE ESPERA DE RELOJ PARA QUE VALLA MAS LENTO LOS WHILE

def pantalla_pricipal():
    enter_presionado = False
    fondo_guardianes.mostrar(pantalla,0,0)
    print("holas")
    dibujar_texto(pantalla, "Press start", colores.BANANA, 40, ANCHO_VENTANA // 2 - 40, 330)
    pygame.display.flip()
    bandera_tiempo_espera = True
    sonido_fondo2.play()
    while bandera_tiempo_espera:
        reloj.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not enter_presionado:
                    enter_presionado = True
                    bandera_tiempo_espera = False  

#desde aca empiezo a cambiar
def pantalla_de_opcion():
    #enter_presionado = False
    
    opciones = ["Jugar", "Opciones", "Salir"]
    opcion_seleccionada = 0
    bandera_tiempo_espera = True
    while bandera_tiempo_espera:
        reloj.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if opcion_seleccionada == 0:
                        # Acción para iniciar el juego
                        print("Iniciando el juego...")
                        bandera_tiempo_espera = False
                    elif opcion_seleccionada == 1:
                        # Acción para mostrar el menú de opciones
                        print("Mostrando el menú de opciones...")
                        """ with sqlite3.connect("aca-guardo-el-juego/bd_score.db") as conexion:
                            cursor = conexion.execute("SELECT * FROM personajes ORDER BY puntuacion DESC")
                            y = 400  # Posición vertical inicial para mostrar los puntajes
                            for fila in cursor:
                                puntaje_texto = f"Nombre: {fila[0]}"
                                puntaje_surface = pygame.font.SysFont(None, 40).render(puntaje_texto, True, colores.WHITE)
                                pantalla.blit(puntaje_surface, (ANCHO_VENTANA // 2 - puntaje_surface.get_width() // 2, 300 + i * 100))
                                y += 30  # Incrementa la posición vertical para el siguiente puntaje
                            """
                    elif opcion_seleccionada == 2:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % len(opciones)
                elif event.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % len(opciones)
            #pantalla.fill((colores.CARROT))
        fondo_principal.mostrar(pantalla,0,posicion_fondo)
        for i, opcion in enumerate(opciones):
                color = (colores.AQUA) if i == opcion_seleccionada else (colores.RASPBERRY)
                texto = pygame.font.SysFont(None, 40).render(opcion, True, color)
                pantalla.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, 300 + i * 100))
        
        pygame.display.flip()
     





#pantalla de continue
def pantalla_de_game_over():
    print("ESTOY DENTRO DE PANTALLA GAME OVER")
    #enter_presionado = False
    opciones_continuar = ["Si", "No"]
    opcion_si_o_no = 0
    tiempo_de_espera = True
    fondo_principal.mostrar(pantalla,0,posicion_fondo)
    dibujar_texto(pantalla, "GAME OVER", colores.BANANA, 50, ANCHO_VENTANA // 2, 130)
    while tiempo_de_espera:
        """fondo_principal.mostrar(pantalla,0,posicion_fondo)
        dibujar_texto(pantalla, "CONTINUE", colores.BANANA, 50, ANCHO_VENTANA // 2 , 130)"""
        reloj.tick(6)
        print("ESTOY EN TIEMPO DE ESPERA")
        for event in pygame.event.get():
            print("EVENTOS")
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return opcion_si_o_no  # Devuelve la opción seleccionada
                elif event.key == pygame.K_UP:
                    opcion_si_o_no = (opcion_si_o_no - 1) % len(opciones_continuar)
                elif event.key == pygame.K_DOWN:
                    opcion_si_o_no = (opcion_si_o_no + 1) % len(opciones_continuar)
            #pantalla.fill((colores.CARROT))
            

            fondo_principal.mostrar(pantalla,0,posicion_fondo)
            dibujar_texto(pantalla, "DESEA CONTINUAR?", colores.BANANA, 50, ANCHO_VENTANA // 2 , 130)
            print("NO ENTRE AL BUCLE ENUMERATE")
       # dibujar_texto(pantalla, "CONTINUE", colores.BANANA, 50, ANCHO_VENTANA // 2 - 40, 130)
        for i, opcion in enumerate(opciones_continuar):
                color = (colores.RED1) if i == opcion_si_o_no else (colores.WHITE)
                texto = pygame.font.SysFont(None, 40).render(opcion, True, color)
                pantalla.blit(texto, (ANCHO_VENTANA // 2 - texto.get_width() // 2, 300 + i * 100))
                print("AL FINAL DEL GAME OVER")
        pygame.display.flip()
        
def pantalla_score():
    #nueva variable agregada
    global valor_ingreso
    ingreso = ""
    ingreso_rect = pygame.Rect(300, 400, 200, 200)
    font_input = pygame.font.Font(None, 28)  # Crea una fuente con tamaño 28
    ingresar_score = True
    enter_presionados = False
    
    pygame.draw.rect(pantalla,colores.ORANGE, ingreso_rect,2)
    font_input_surface = font_input.render(ingreso,True,colores.WHITE)
    pantalla.blit(font_input_surface,(ingreso_rect.x+5, ingreso_rect.y+5))
    pygame.display.flip()
    while ingresar_score:
        reloj.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    ingreso = ingreso[:-1]
                else:
                    ingreso += event.unicode

                if event.key == pygame.K_RETURN:
                    valor_ingreso = ingreso
                    ingresar_score = False

        fondo_principal.mostrar(pantalla,0,posicion_fondo)
        dibujar_texto(pantalla, "PANTALLA SCORE", colores.BANANA, 100, ANCHO_VENTANA // 2, 130)
        dibujar_texto(pantalla, "INGRSE SU NOMBRE", colores.BANANA, 40, ANCHO_VENTANA // 2, 300)
        dibujar_texto(pantalla, "SCORE", colores.BANANA, 40, ANCHO_VENTANA // 2, 330)
        pygame.draw.rect(pantalla, colores.ORANGE, ingreso_rect, 2)
        font_input_surface = font_input.render(ingreso, True, colores.WHITE)
        pantalla.blit(font_input_surface, (ingreso_rect.x + 5, ingreso_rect.y + 5))
        pygame.display.flip()

def dibujar_texto(surface, texto, color, tamaño, x ,y):
    fuente = pygame.font.SysFont("ArcadeClassic", tamaño)#probar con LEADERSON
    texto_surface = fuente.render(texto, True, color)
    texto_rect = texto_surface.get_rect()
    texto_rect.midtop = (x,y)
    surface.blit(texto_surface, texto_rect) 



def draw_barra_de_salud(surface, x, y, porsentaje):
    barra_largo = 100
    barra_alto = 20
    llenar = (porsentaje / 100) * barra_largo
    #creo el rectangulo de la vida
    borde = pygame.Rect(x, y, barra_largo, barra_alto)
    #creo el relleno de la vida
    llenar = pygame.Rect(x, y, llenar, barra_alto)
    #dibujo el rectangulo y el borde de este
    pygame.draw.rect(surface, colores.GREEN1, llenar)
    pygame.draw.rect(surface,colores.WHITE, borde, 2)




#imagen de explocion 
# hago este funcion afuera asi depues la pongo 
# adentro de la explosion
def getSuperficies(path,filas, columnas):
    lista=[]
    superficie_imagen = pygame.image.load(path)
    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)

    for fila in range(filas):
        for columna in range(columnas):
            x = columna * fotograma_ancho
            y = fila * fotograma_alto
            #un pedacito de la imagen del sprite
            superficie_fotograma = superficie_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
            lista.append(superficie_fotograma)

    return lista

