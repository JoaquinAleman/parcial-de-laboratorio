#PARA CONVERTIR IMAGENES A PNG = https://pixlr.com/es/x/#editor
#remover marca de agua = https://www.watermarkremover.io/es/upload
#CONVERTIDOR DE AUDIO = Y2mate
# layerss = https://www.gamedevmarket.net/category/2d/characters?orderby=recent&pricing=free&genre=
# TAMBIEN ESTA LA QUE PASO EL PROFE LA LISTA DE COLORES
# $$$$$$$$$$$$   PARA LOS COLORESS   $$$$$$$$$$$$$$
#https://www.w3schools.com/colors/colors_rgb.asp

#########    SONIDOS     ##################
#http://www.sonidosmp3gratis.com/download.php?id=895&sonido=pelota%20tenis
############  CORTADOR DE AUDIOS  ###############
#https://vocalremover.org/es/cutter
# POO
from typing import Any
import pygame
#from pygame.sprite import _Group
import colores
import random
import sys
from constantes import *
#################      BIBLIOTTECASSS             ############################
from pantallas_limpio import *
from fondo_limpio import *
from sonidos_limpio import *
#clases
from nave_limpio import *
from item_limpio import *
from bullet_limpio import *
from explosion_limpio import *
from sprite_group_limpio import *
from enemigo_limpio import *

#from constantes import *
import sqlite3
import traceback #nose para qu es

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ANCHO_NAVE = 100
ALTO_NAVE = 100

ANCHO_ENEMIGO = 50
ALTO_ENEMIGO = 50

MEDIDAS_FONDO = (800,800)

ALTO_FONDO = 800
ANCHO_FONDO = 800


pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego de naves")
reloj = pygame.time.Clock()
inicio_tiempo = pygame.time.get_ticks()
#20/6 MODIFIQUE LOS TIEMPOS DE ESPERA DE RELOJ PARA QUE VALLA MAS LENTO LOS WHILE


#BULLETS ES EL GRUPO DE SPRITE POR ESO LO AGREGE AHI A LOS BULLET(DISPARO)
#AHORA VAMOS A PROBAR SI FUNCIONA EN UN GRUPO DE 2
#hasta aca llege tengo que hacer otro grupo de sprite para el bullet de los enemigos
#y shot enemigo lo tengo despues lo tengo que poner en las variables disaparo




###################################################################################   

"""
#nave
all_sprites = pygame.sprite.Group()

#enemigos
enemigos_lista = pygame.sprite.Group()

#disparos
bullets_amigo = pygame.sprite.Group()

bullets = pygame.sprite.Group()
#NAVE_LISTA
lista_nave_amiga = pygame.sprite.Group()

#Items-Bonus
bonuss = pygame.sprite.Group()



 
#llamo a la nave
player = Nave()
#explosion
#explosion = Explosion(x,y)

all_sprites.add(player)
"""
########################        MAIN        ########################

## Puntaje  
#all_sprites.add(player)  
score = 0


fondo_guardianes = FondoPantalla("aca-guardo-el-juego/fondo-guardianes-de-la-galaxia.jpg",MEDIDAS_FONDO)
fondo_principal = FondoJuego("fondo_galaxia.png",MEDIDAS_FONDO)
posicion_fondo = 0 # Variable para rastrear la posición vertical del fondo

reproducir_segundo_sonido = False
salto_de_cuadro = True
game_over = True
#inicio = pygame.time.get_ticks() otro tiempo
correr = True
bandera_tiempo = True
valor_ingreso = ""

font_puntaje = pygame.font.Font(None, 28)
while correr:
    
    #18/6 ahora voy hacer la pantalla principal y el menu de opciones
    if salto_de_cuadro:
    #loop
        pantalla_pricipal()

        salto_de_cuadro = False
        
        pantalla_de_opcion()

    if game_over:

        #pantalla_pricipal()
        #pantalla de game over
        #hasta aca llegue
        sonido_fondo2.stop()
        sonido_fondo.play() 

        game_over = False
        #nave
        all_sprites = pygame.sprite.Group()
        #enemigos
        enemigos_lista = pygame.sprite.Group()
        #disparos
        bullets = pygame.sprite.Group()
        bullets_amigo = pygame.sprite.Group()
        #colisiones_mi_nave
        lista_nave_amiga = pygame.sprite.Group()
        #Items-Bonus
        bonuss = pygame.sprite.Group()

        #llamo a la nave
        player = Nave()
        #explosion
        all_sprites.add(player)
        #creo VARIOS ENEMIGOS 8
        for i in range(4):
            enemigos = Enemigos()
            all_sprites.add(enemigos)
            enemigos_lista.add(enemigos)
            ## Puntaje   
            score = 0
        """  if score >= 3000:
            sonido_fondo.stop()  
            sonido_fondo2.play() 
            """   
    
    reloj.tick(30)   #lo tenia en 60 pero lo pase a 30 para que valla mas lento abajo lo que hacia era reducir el doble osea 30
    #dt = reloj.tick(60)  # Calcula el tiempo transcurrido desde el último cuadro en milisegundos
  

    for event in pygame.event.get():
        #evento
        if event.type == pygame.QUIT:
            correr = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                sonido_laser.play()
                sonido_laser.set_volume(0.1)
            """  if player.salud == 0:    
                if event.key == pygame.K_BACKSPACE:     #nuevo agredado
                    ingreso = ingreso[0:-1]
                else:
                    ingreso += event.unicode      """

    all_sprites.update()


#cambiar velocidad del bonus no olvidarw

    #colision entre mi LASER - y Enemigo - final Explosion
    colisiones = pygame.sprite.groupcollide(enemigos_lista, bullets_amigo, True, True)
    for colision in colisiones:
        score += 10
      
        sonido_explosion.play()   
        sonido_explosion.set_volume(0.1) 
        x = colision.rect.centerx  
        y = colision.rect.centery
        explosion = Explosion(x,y)
        all_sprites.add(explosion)
       
        bonus = Items(x,y)          #bonus
        all_sprites.add(bonus)
        bonuss.add(bonus)
        if explosion.paso1 >= len(explosion.fotogramas):
            explosion.kill()
            #if  == True:
             #   bonus.kill()

        enemigo = Enemigos()
        all_sprites.add(enemigo)
        enemigos_lista.add(enemigo)
        enemigo.disparado = False  # Restablecer la bandera "disparado" a False
       
#esto fue lo ultimo que le agrege
        #colision entre mi Nave - y el BONUS
    colisiones_upgrade = pygame.sprite.spritecollide(player, bonuss, True)
    for colision_bonus in colisiones_upgrade:
        sonido_bonus.play()
        sonido_bonus.set_volume(0.2) 
        score += 500


  ########################################################################### 
    all_sprites.update()  # Pasa el tiempo transcurrido a todos los sprites para actualizar la animación
    
    
    #DISPAROS DE ENEMIGO
    for enemigo in enemigos_lista:
        if random.random() < 0.01:  # Ajusta este valor para controlar la frecuencia de disparo de las naves enemigas
            enemigo.shoot()
            sonido_laser_enemigo.play()   
            sonido_laser_enemigo.set_volume(0.2)#depues si quiero pasalo a(0.1) pero esta buena la sensacion de escuchar mejor el disparo del enemigo 
            
    
    #NUEVA LISTA AGREGADA
     #colision entre mi Nave - con Laser Enemigo
    colisiones_mi_nave = pygame.sprite.spritecollide(player, bullets, True)
           
    for colision in colisiones_mi_nave:
        player.salud -= 25
        enemigo = Enemigos()
        all_sprites.add(enemigo)
        enemigos_lista.add(enemigo)
        if player.salud <= 0:    
            #correr = False # con esta me va directo a sacar del juego cuando me quede sin vida
            game_over = True  #lo cambio a true por que lo inicialize asi y ase que no termine el juego que valla a la pantalla gameover
   
        enemigo = Enemigos()
        all_sprites.add(enemigo)
        enemigos_lista.add(enemigo)
        enemigo.disparado = False 

          
	# Colision entre mi Nave jugador -  con enemigo
    colisiones = pygame.sprite.spritecollide(player, enemigos_lista, True)
    for colision in colisiones:
        player.salud -= 25
        enemigo = Enemigos()
        all_sprites.add(enemigo)
        enemigos_lista.add(enemigo)

        #explosion
        x = colision.rect.centerx
        y = colision.rect.centery
        explosion = Explosion(x,y)
        all_sprites.add(explosion)
        if explosion.paso1 >= len(explosion.fotogramas):
            explosion.kill()


        if player.salud <= 0:    
            #correr = False # con esta me va directo a sacar del juego cuando me quede sin vida
            game_over = True  #lo cambio a true por que lo inicialize asi y ase que no termine el juego que valla a la pantalla gameover
    #print(reloj.tick(FPS)) con esto controlo los fps
    posicion_fondo += 0.4 # Aumenta la posición vertical del fondo
    #fondo
    #pantalla.blit(imagen_fondo,[0,0])
    fondo_principal.mostrar(pantalla,0,posicion_fondo)

    all_sprites.draw(pantalla)

    dibujar_texto(pantalla, "timer",colores.BANANA, 35, 35, 10)
    dibujar_texto(pantalla, str(SEGUNDOS), colores.WHITE, 35, 35, 35)   
  
    TIEMPO += 1
    #if bandera_tiempo == True:
    if TIEMPO == 30: #simula que pasa un segundo
        TIEMPO = 0
        SEGUNDOS -= 1
    if SEGUNDOS <= 0:
        player.salud -= 1 
        if player.salud <= 0:
            game_over = True    

    #texto score
    dibujar_texto(pantalla, "score",colores.BANANA,35, ANCHO_VENTANA // 2, 5)   
    dibujar_texto(pantalla, str(score), colores.WHITE, 35,ANCHO_VENTANA // 2, 30) #40 queda bien
    #dibujar_texto(pantalla, "Bienvenidos Al Juego",50,ANCHO_VENTANA  // 2, 400)  

    #barra de salud
    draw_barra_de_salud(pantalla, 5, 775, player.salud)
 
    #
    #esto ya son claves de seguridad que suseden una vez termina el juego o si game over se ejecuta
    if game_over == True:
        sonido_fondo.stop()
        SEGUNDOS = 60   

    if player.salud == 0:
        #game_over = True
        #pantalla.fill(colores.BLACK)
        print("ESTOY DENTRO DEL BUCLE")
        #pantalla_de_game_over()
        opcion = pantalla_de_game_over()
        if opcion == 0:
            print("volvio al juego")
        elif opcion == 1:
            pantalla_score()
            reloj.tick(30)#esto se puede sacar
            
            with sqlite3.connect("aca-guardo-el-juego/bd_score.db") as conexion:
                try:
                    sentencia = ''' create  table personajes
                    (
                    id integer primary key autoincrement,
                    nombre text,
                    puntuacion real
                
                    )
                    '''
                    conexion.execute(sentencia)
                    print("Se creo la tabla personajes")                       
                except sqlite3.OperationalError:
                    print("La tabla personajes ya existe")

                #INSERT: carga los valores
                #valor_ingreso es el nombre
                try:
                    conexion.execute("INSERT INTO personajes (nombre, puntuacion) VALUES (?, ?)", (valor_ingreso, score))
                    conexion.commit()# Actualiza los datos realmente en la tabla
                    print("datos guardados")
                except:
                    print("Error")

                #SELECT: imprime los datos que se insertaron
                cursor=conexion.execute("SELECT * FROM personajes order by puntuacion desc")
                y = 400
                for fila in cursor:
                    print(fila)
                """     puntaje_texto = f"Nombre: {fila[1]}, Puntuación: {fila[2]}"
                    puntaje_surface = font_puntaje.render(puntaje_texto, True, colores.WHITE)
                    pantalla.blit(puntaje_surface, (300, y))
                    y += 30 """



            salto_de_cuadro = True
        print(opcion)    
       
        print("pase la pantalla game over")

        
    pygame.display.flip()


pygame.quit()
