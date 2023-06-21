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
from primer_personaje import FondoJuego
from primer_personaje import FondoPantalla
from constantes import *
import sqlite3
import traceback #nose para qu es



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


pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Juego de naves")
reloj = pygame.time.Clock()
inicio_tiempo = pygame.time.get_ticks()
#20/6 MODIFIQUE LOS TIEMPOS DE ESPERA DE RELOJ PARA QUE VALLA MAS LENTO LOS WHILE

def pantalla_pricipal():
    enter_presionado = False
    #pantalla.blit(fondo_principal, [0,0])
    fondo_guardianes.mostrar(pantalla,0,0)
    print("holas")
    #dibujar_texto(pantalla, "GALAGA 2.0", colores.BANANA, 120, ANCHO_VENTANA // 2, 130)
    #dibujar_texto(pantalla, "intrucciones van aqui", colores.BANANA, 40, ANCHO_VENTANA // 2, 300)
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

        """ bandera_tiempo_espera = True   
    while bandera_tiempo_espera:
        reloj.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if player.salud == 0:    
                    if event.key == pygame.K_BACKSPACE:     #nuevo agredado
                        ingreso = ingreso[0:-1]
                else:
                    ingreso += event.unicode
                    enter_presionados = True
                    bandera_tiempo_espera = False 
"""


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
#agrege el cambiar color y le agrege un parametro color y un self color
# $ son lo agregado
#fecha 16/6 desde aca termine el item
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

    #NUEVO DISPARO
    """def shoot2(self):
        bullet = Bullet(self.rect.centerx, self.rect.bottom)
        all_sprites.add(bullet)
        bullets.add(bullet)     
"""
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

###################################################################################   


#ARCHIVO MP3 = MUSICA DE FONDO
pygame.mixer.music.set_volume(0.1)

sonido_fondo = pygame.mixer.Sound("aca-guardo-el-juego/Blazing-star.mp3")
sonido_fondo.set_volume(0.2)

sonido_fondo2 = pygame.mixer.Sound("aca-guardo-el-juego/Rodeo-8bits.mp3")
sonido_fondo2.set_volume(0.2)
#pygame.mixer.music.set_volume(0.1)
#pygame.mixer.music.play(0,100,3000)#fuera del loop principal
#pygame.mixer_music.play(0,1000)

#### SONIDOS DE EFECTOS ESPECIALES
#nave
sonido_laser = pygame.mixer.Sound("aca-guardo-el-juego/sonido-laser.mp3")

#enemigo
sonido_laser_enemigo = pygame.mixer.Sound("aca-guardo-el-juego/sonido-laser-enemigo.mp3")
sonido_explosion = pygame.mixer.Sound("aca-guardo-el-juego/sonido-explosion.mp3")
#items
sonido_bonus = pygame.mixer.Sound("aca-guardo-el-juego/sonido-bonus.mp3")




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


"""#creo VARIOS ENEMIGOS 8
for i in range(2):
    enemigos = Enemigos()
    all_sprites.add(enemigos)
    enemigos_lista.add(enemigos)
"""

########################        MAIN        ########################



## Puntaje   
score = 0

#Musica fondo
#(0,18)el primer valor establce el numero de veces que se repite la musica
#el 18 indica en el segundo que se reproduce osea en el segundo 18 de la cancion
#pygame.mixer.music.play(1,1)
#sonido_fondo.play(1,10000) 
#sonido_fondo.play() 
#tiempo= osea (repeticion, 10 segundos) 



"""# Detiene la reproducción de la primera música con un fundido gradual de 2 segundos
pygame.mixer.music.fadeout(10000)

# Carga la segunda música
pygame.mixer.music.load("kiss-in-the-dark.mp3")
pygame.mixer.music.set_volume(0.5)

# Reproduce la segunda música
pygame.mixer.music.play()
"""

"""fondo_guardianes = pygame.image.load("aca-guardo-el-juego/fondo-guardianes-de-la-galaxia.jpg")
fondo_guardianes = pygame.transform.scale(fondo_guardianes,(ANCHO_VENTANA, ALTO_VENTANA))"""



fondo_guardianes = FondoPantalla("aca-guardo-el-juego/fondo-guardianes-de-la-galaxia.jpg",MEDIDAS_FONDO)
fondo_principal = FondoJuego("fondo_galaxia.png",MEDIDAS_FONDO)
posicion_fondo = 0 # Variable para rastrear la posición vertical del fondo


#tiempo para mostrar ----------------------------}}}}}}}}}}}}}}
"""font = pygame.font.SysFont("Arial", 30)
tiempo = font.render("TIEMPO: {0}".format(SEGUNDOS), True, colores.RED1)
pantalla.blit(tiempo,(10,10))
TIEMPO += 1
if TIEMPO == 8:
    TIEMPO = 0
    SEGUNDOS -= 1
    """
reproducir_segundo_sonido = False
salto_de_cuadro = True
game_over = True
#inicio = pygame.time.get_ticks() otro tiempo
correr = True
bandera_tiempo = True
valor_ingreso = ""
"""#nueva variable agregada
ingreso = ""
ingreso_rect = pygame.Rect(100, 200, 100, 200)
font_input = pygame.font.Font(None, 28)  # Crea una fuente con tamaño 28
ingresar_score = True"""
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
        """ if player.salud == 0:
            pantalla_de_game_over()"""
        #if sonido_fondo == :
          ## Puntaje   
        """   score = 0
        if score >= 3000:
            sonido_fondo.stop()  """
        #sonido_fondo2.play() 
        #print("hola")
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

    """  for enemigo in enemigos_lista:
        if random.random() < 0.01:  # Ajusta este valor para controlar la frecuencia de disparo de las naves enemigas
            enemigo.shoot()
    """

    """#tiempo 
        tiempo_transcurrido = pygame.time.get_ticks() - inicio

        # Si han pasado 10 segundos, cambia a la segunda música
        if tiempo_transcurrido >= 10000:
            pygame.mixer.music.stop()
            
            # Carga y reproduce la segunda música
            pygame.mixer.music("kiss-in-the-dark.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
            #break    


"""
#cambiar velocidad del bonus no olvidarw

    #colision entre mi LASER - y Enemigo - final Explosion
    colisiones = pygame.sprite.groupcollide(enemigos_lista, bullets_amigo, True, True)
    for colision in colisiones:
        score += 10
        """  if score >= 3000 and not reproducir_segundo_sonido:
                reproducir_segundo_sonido = True
        if reproducir_segundo_sonido:
                sonido_fondo.stop()
                sonido_fondo2.play()
                reproducir_segundo_sonido = False"""
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
        #bonuss.kill()

            # all_sprites.add
        """  x = colision.rect.centerx  
            y = colision.rect.centery
            bonus = Items(x,y)
            all_sprites.add(bonus)
            player.salud -= 25
            enemigo = Enemigos()
            all_sprites.add(enemigo)
            enemigos_lista.add(enemigo)"""




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
        #x_nave = colision.rect.centerx
        #y_nave = colision.rect.centery
        """ explosion_nave = Explosion(x_nave,y_nave)
        all_sprites.add(explosion_nave)
        if explosion_nave.paso1 >= len(explosion_nave.fotogramas):
            explosion_nave.kill()"""

        """     nave_amiga = Nave()
            all_sprites.add(nave_amiga)
            lista_nave_amiga.add(nave_amiga)        
                
        """
        enemigo = Enemigos()
        all_sprites.add(enemigo)
        enemigos_lista.add(enemigo)
        enemigo.disparado = False 
        """ if score >= 3000:
            sonido_fondo.stop()  
            sonido_fondo2.play()
            """
    

          
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



    #font = pygame.font.SysFont("Arial", 30)
    #tiempo = font.render("TIEMPO: {0}".format(SEGUNDOS), True, colores.RED1)
    #pantalla.blit(tiempo,(10,10))
    #tiempo en pantalla
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
    #SEGUNDOS = 0    
    """ if game_over == True:
            TIEMPO == 0"""
    #bandera_tiempo = False

    #texto score
    dibujar_texto(pantalla, "score",colores.BANANA,35, ANCHO_VENTANA // 2, 5)   
    dibujar_texto(pantalla, str(score), colores.WHITE, 35,ANCHO_VENTANA // 2, 30) #40 queda bien
    #dibujar_texto(pantalla, "Bienvenidos Al Juego",50,ANCHO_VENTANA  // 2, 400)  

    #barra de salud
    draw_barra_de_salud(pantalla, 5, 775, player.salud)
 
    #pygame.display.flip()

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
        #if pantalla_de_game_over == 1:   
           # pantalla_score()
        """pygame.draw.rect(pantalla,colores.ORANGE, ingreso_rect,2)
        font_input_surface = font_input.render(ingreso,True,colores.WHITE)
        pantalla.blit(font_input_surface,(ingreso_rect.x+5, ingreso_rect.y+5))"""
        print("pase la pantalla game over")

        
    pygame.display.flip()

    """with sqlite3.connect("aca-guardo-el-juego/bd_score.db") as conexion:
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

        #INSERT:

        try:
            conexion.execute("INSERT INTO personajes (nombre, puntuacion) VALUES (?, ?)", (valor_ingreso, score))
            conexion.commit()# Actualiza los datos realmente en la tabla
            print("datos guardados")
        except:
            print("Error")"""

    """ with sqlite3.connect("aca-guardo-el-juego/bd_score.db") as conexion:
        try:    
            sentencia = '''
                        CREATE TABLE IF NOT EXISTS personajes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT,
                        puntuacion INTEGER
                        )
            
                        '''
            conexion.execute(sentencia)
            print("Se creo la tabla personajes") 
        except sqlite3.OperationalError:
		        print("La tabla personajes ya existe")
                    
        
        #INSERT:
        try:
            conexion.execute("INSERT INTO personajes (nombre, puntuacion) VALUES (?, ?)", (ingreso, puntuacion_jugador))
            conexion.commit()#actualiza base de datos
            print("Datos guardados en la base de datos")
        except:
            print("Error al guardar los datos")"""
    """if score == 3000:
            sonido_fondo.stop()  """
                
    #sonido_fondo2.play()   

pygame.quit()



"""
EXPLOCION DE UNA FUEGO
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.fotogramas = getSuperficies("Explosion-1.png",1,8)#1,9
      
        #indice de  fotograma es igual a paso1
        self.paso1 = 2
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

"""