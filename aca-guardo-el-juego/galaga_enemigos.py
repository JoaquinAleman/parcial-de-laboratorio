"""import pygame
import colores
def crear_nave(x,y,ancho,alto):
    #nave
    imagen_naveg = pygame.image.load("Galaga-avion-principal.png")
    imagen_naveg = pygame.transform.scale(imagen_naveg,(ancho,alto))
    rect_naveg = imagen_naveg.get_rect() #rec por defecto
    rect_naveg.x = x
    rect_naveg.y = y

    #guardar la imagen y el rect en un diccionario IMPORTANTE
    dict_naveg = {}
    dict_naveg["imagen"] = imagen_naveg
    dict_naveg["rect"] = rect_naveg
    dict_naveg["visible"] = True

    return dict_naveg


def crear_lista_naves(cantidad):
    lista_naveg = []
    for i in range(cantidad):# 0+i*50 es un acumulador para poner las posiciones de la naves
        lista_naveg.append(crear_nave(0+(i * 50),230,30,30))
    return lista_naveg #             xacumulador,y,ancho_nave,largo_imagen

def actualizar_pantalla(lista_naveg, pantalla, rect_messi, score):
    for e_naveg in lista_naveg:
        if e_naveg["visible"] == True and rect_messi.colliderect(e_naveg["rect"]):
            e_naveg["visible"] = False
            score = score + 100 #puntuacion por cada vez que coma uno
        
        if e_naveg["visible"] == True:
            pygame.draw.rect(pantalla, colores.RED1, e_naveg["rect"])
            pantalla.blit(e_naveg["imagen"], e_naveg["rect"])
    
    return score            
"""
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
from primer_personaje import Fondo

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

ANCHO_NAVE = 100
ALTO_NAVE = 100

ANCHO_ENEMIGO = 50
ALTO_ENEMIGO = 50

MEDIDAS_FONDO = (800,800)
#dcon esto controlo los fps fps FPS = 30




pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Shoteer")
reloj = pygame.time.Clock()


def dibujar_texto(surface, texto, color, tamaño, x ,y):
    fuente = pygame.font.SysFont("ArcadeClassic", tamaño)
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
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.image = pygame.image.load("aca-guardo-el-juego/disparo.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.velocidady = -10

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
    
    def update(self):
        self.rect.y += self.velocidad_y    
        self.rect.x += self.velocidad_x
        #si ya salio de la ventana            o si ya salio por la izquierda o si salio por la derecha DE LA VENTANA
        if self.rect.top > ALTO_VENTANA + 10 or self.rect.left < -25 or  self.rect.right > ANCHO_VENTANA + 25:
            self.rect.y = random.randrange(-100,-40) #desde donde salen los enemigo osae su punto de partida
            self.velocidad_y = random.randrange(1,5) #esta es una velocidad aleatoria que caen
            self.velocidad_x = random.randrange(-5,5)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y) -> None:
        super().__init__()
        self.fotogramas = getSuperficies("Explosion-1.png",1,4)#12
      
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
"""    def dibujar(self, pantalla):
        self.imagen = self.animacion[self.paso1]
        pantalla.blit(self.imagen, self.rect)
"""

pygame.mixer.music.set_volume(0.1)
inicio_tiempo = pygame.time.get_ticks()
cambio_de_tema = 1000

sonido_fondo = pygame.mixer.Sound("aca-guardo-el-juego/kiss-in-the-dark.mp3")
sonido_fondo.set_volume(0.2)

sonido_fondo2 = pygame.mixer.Sound("aca-guardo-el-juego/Rodeo-8bits.mp3")
sonido_fondo.play() 
if pygame.time.get_ticks() - inicio_tiempo > cambio_de_tema:
    sonido_fondo.stop()
    sonido_fondo2.play()

#nave
all_sprites = pygame.sprite.Group()

#enemigos
enemigos_lista = pygame.sprite.Group()

#disparos
bullets = pygame.sprite.Group()

#NAVE_LISTA
lista_nave_amiga = pygame.sprite.Group()


#llamo a la nave
player = Nave()
#explosion
#explosion = Explosion(x,y)

all_sprites.add(player)


#creo VARIOS ENEMIGOS 8
for i in range(10):
    enemigos = Enemigos()
    all_sprites.add(enemigos)
    enemigos_lista.add(enemigos)


########################        MAIN        ########################

## Puntaje   
score = 0

#Musica fondo
#(0,18)el primer valor establce el numero de veces que se repite la musica
#el 18 indica en el segundo que se reproduce osea en el segundo 18 de la cancion
#pygame.mixer.music.play(1,1)





"""# Detiene la reproducción de la primera música con un fundido gradual de 2 segundos
pygame.mixer.music.fadeout(10000)

# Carga la segunda música
pygame.mixer.music.load("kiss-in-the-dark.mp3")
pygame.mixer.music.set_volume(0.5)

# Reproduce la segunda música
pygame.mixer.music.play()
"""


fondo_principal = Fondo("fondo_galaxia.png",MEDIDAS_FONDO)
posicion_fondo = 0 # Variable para rastrear la posición vertical del fondo


game_over = True
inicio = pygame.time.get_ticks()
correr = True
while correr:
    #loop
    if game_over:
        game_over = False
        #nave
        all_sprites = pygame.sprite.Group()
        #enemigos
        enemigos_lista = pygame.sprite.Group()
        #disparos
        bullets = pygame.sprite.Group()
        #colisiones_mi_nave
        lista_nave_amiga = pygame.sprite.Group()
        #llamo a la nave
        player = Nave()
        #explosion
        all_sprites.add(player)
        #creo VARIOS ENEMIGOS 8
        for i in range(10):
            enemigos = Enemigos()
            all_sprites.add(enemigos)
            enemigos_lista.add(enemigos)
            ## Puntaje   
            score = 0

    reloj.tick(30)   #lo tenia en 60 pero lo pase a 30 para que valla mas lento abajo lo que hacia era reducir el doble osea 30
    #dt = reloj.tick(60)  # Calcula el tiempo transcurrido desde el último cuadro en milisegundos
    
    
    for event in pygame.event.get():
        #evento
        if event.type == pygame.QUIT:
            correr = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()
    

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


    #colisiones enemigo - laser
    colisiones = pygame.sprite.groupcollide(enemigos_lista, bullets, True, True)
    for colision in colisiones:
        score += 10

        x = colision.rect.centerx
        y = colision.rect.centery
        explosion = Explosion(x,y)
        all_sprites.add(explosion)
        if explosion.paso1 >= len(explosion.fotogramas):
            explosion.kill()


        enemigo = Enemigos()
        all_sprites.add(enemigo)
        enemigos_lista.add(enemigo)
       
  ########################################################################### 
    all_sprites.update()  # Pasa el tiempo transcurrido a todos los sprites para actualizar la animación
    #NUEVA LISTA AGREGADA
     #calisiones mi Nave - laser
    colisiones_mi_nave = pygame.sprite.groupcollide(lista_nave_amiga, bullets, True, True)
           
    for colision in colisiones_mi_nave:
        score += 100

        x_nave = colision.rect.centerx
        y_nave = colision.rect.centery
        explosion_nave = Explosion(x_nave,y_nave)
        all_sprites.add(explosion_nave)
        if explosion_nave.paso1 >= len(explosion_nave.fotogramas):
            explosion_nave.kill()

        nave_amiga = Nave()
        all_sprites.add(nave_amiga)
        lista_nave_amiga.add(nave_amiga)        
                
            
       


          
	# Colisiones jugador - enemigo
    colisiones = pygame.sprite.spritecollide(player, enemigos_lista, True)
    for colision in colisiones:
        player.salud -= 25
        enemigo = Enemigos()
        all_sprites.add(enemigo)
        enemigos_lista.add(enemigo)
        if player.salud <= 0:    
            #correr = False # con esta me va directo a sacar del juego cuando me quede sin vida
            game_over = True  #lo cambio a true por que lo inicialize asi y ase que no termine el juego que valla a la pantalla gameover
    #print(reloj.tick(FPS)) con esto controlo los fps
    posicion_fondo += 0.4 # Aumenta la posición vertical del fondo
    #fondo
    #pantalla.blit(imagen_fondo,[0,0])
    fondo_principal.mostrar(pantalla,0,posicion_fondo)

    all_sprites.draw(pantalla)


    #texto score
    dibujar_texto(pantalla, "score",colores.BANANA,35, ANCHO_VENTANA // 2, 5)   
    dibujar_texto(pantalla, str(score), colores.WHITE, 35,ANCHO_VENTANA // 2, 30) #40 queda bien
    #dibujar_texto(pantalla, "Bienvenidos Al Juego",50,ANCHO_VENTANA  // 2, 400)  

    #barra de salud
    draw_barra_de_salud(pantalla, 5, 775, player.salud)


    pygame.display.flip()

pygame.quit()
'''
DEFINICIONES:
#########     self.rect.bottom = ALTO_VENTANA -10       ############

si el objeto es un enemigo, podría utilizarse para inicializar 
su posición en la parte superior de la pantalla, 
dejando un espacio de 10 píxeles desde el borde inferior.
 Esto aseguraría que los enemigos aparezcan 

 ############## DT = delta time


#NUEVA LISTA AGREGADA
    colisiones_mi_nave =pygame.sprite.groupcollide(player, bullets, True, True)
           
    for colisiones_mi_nave in colisiones:
        score += 10

        x_nave = colision.rect.centerx
        y_nave = colision.rect.centery
        explosion_nave = Explosion(x,y)
        all_sprites.add(explosion_nave)
        if explosion_nave.paso1 >= len(explosion_nave.fotogramas):
            explosion_nave.kill()

        nave_amiga = Nave()
        all_sprites.add(nave_amiga)
        enemigos_lista.add(nave_amiga)        
                
        
        
 

'''