"""import pygame
import colores
import random
#from pydub import AudioSegment


##########  JUEGO COMPLETO   #########
#PARA CONVERTIR IMAGENES A PNG = https://pixlr.com/es/x/#editor
#remover marca de agua = https://www.watermarkremover.io/es/upload
#CONVERTIDOR DE AUDIO = Y2mate
# layerss = https://www.gamedevmarket.net/category/2d/characters?orderby=recent&pricing=free&genre=
# TAMBIEN ESTA LA QUE PASO EL PROFE LA LISTA DE COLORES
# $$$$$$$$$$$$   PARA LOS COLORESS   $$$$$$$$$$$$$$
#https://www.w3schools.com/colors/colors_rgb.asp

#######

COLOR_NEGRO = (7,0,25)
COLOR_CELESTE = (135,206,235)
COLOR_AMARILLO = (255,255,0)
COLOR_BLANCO = (255,255,255)
COLOR_GRIS = (128,128,128)
ANCHO_VENTANA  = 900
ALTO_VENTANA = 700 
RADIO = 80
RADIO_MESSI = 0
#NAVE
ANCHO_NAVE = 100
ALTURA_NAVE = 100
#ESTE ES EL DE PRUEBA
DISPARO_NAVE = 10
#ESTE ES EL REAL
ANCHO_DISPARO = 5
ALTURA_DISPARO = 10

ANCHO_ENEMIGO = 50
ALTURA_ENEMIGO = 50

pygame.init()   #abre el promgrama

pygame.mixer.init() # abre programa de sonido

#horizontal, Vertical, Ancho, Alto
posicion_rectangulo = (150,5,5,15)

#posicion en la pantalla x- , y|
posicion_nave = [400,600] # la posicion desde donde arranca la nave
posicion_enemigo =[400,100]

#POSICION DEL DISPARO NAVE
posicion_disparo_nave = None
disparos_nave = []
#horizontal, Vertical, Ancho, Alto
posicion_rectangulo = (150,5,5,15)

disparar = False

#FONDO PRINCIPAL
fondo_principal = pygame.image.load("galaxia-fondo.png")
fondo_principal_redimensionado = pygame.transform.scale(fondo_principal,(ANCHO_VENTANA,ALTO_VENTANA))#

#IMAGEN DE NAVE PRINCIPAL
imagen_nave_principal = pygame.image.load("Galaga-avion-principal.png")
imagen_nave_principal_redimensionada = pygame.transform.scale(imagen_nave_principal,(ANCHO_NAVE,ALTURA_NAVE))#tamño de imagen le digo cuanto quiero que mida
imagen_enemigo_1 = pygame.image.load("Galaga-enemigo1.png")
imagen_enemigo_1_redimensionada = pygame.transform.scale(imagen_enemigo_1,(ANCHO_ENEMIGO,ALTURA_ENEMIGO))





#TEXTO
fuente = pygame.font.SysFont("Arial", 25)
texto = fuente.render("HIGH SCORE", True, colores.RED1)



# set_mode acepta tuplas y listas
                                    #(ancho,altura)
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) #display es la pantalla y marca la altura y largo
pygame.display.set_caption("Mi primer Juego GALAGA")  #titulo


#ARCHIVO MP3 = MUSICA
sonido_fondo =pygame.mixer.Sound("Rodeo-8bits.mp3")
pygame.mixer.music.set_volume(0.1)

#pygame.time.wait(int(sonido_fondo.get_length() * 10)) #esto es para poner una pausa

#sonido_fondo.play()
#sonido_fondo.play() #empieza #el sonido
#

# TIEMPO
tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick,500)
tiempo = 0

flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for e_evento in lista_eventos: #va ir guardando cada uno de los eventos que pasan
        if e_evento.type == pygame.QUIT:
            flag_correr = False 
            #funcion tick
        if e_evento.type == tick:
            tiempo += 1  # va invrementar el tiempo cada segundo
            #DISPAROS ESTO FUNCIONA
        if e_evento.type == pygame.KEYDOWN:
            if e_evento.key == pygame.K_SPACE:
                disparos = pygame.Rect(posicion_nave[0] + (ANCHO_NAVE // 2) - (ANCHO_DISPARO // 2), posicion_nave[1], ANCHO_DISPARO, ALTURA_DISPARO)
                disparos_nave.append(disparos)
                print("disparos")   
    
###############      MOVIMIENTO DE NAVE     ####################
   

    #pygame.time.wait(int(sonido_fondo.get_length() * 10)) #ase que repita en bucle

    lista_teclas = pygame.key.get_pressed()    
    if True in lista_teclas:
        if lista_teclas[pygame.K_RIGHT]:
            posicion_nave[0] = posicion_nave[0] + 1
        elif lista_teclas[pygame.K_LEFT]:
            posicion_nave[0] = posicion_nave[0] - 1
        
        if lista_teclas[pygame.K_UP]:
            posicion_nave[1] = posicion_nave[1] - 1
        elif lista_teclas[pygame.K_DOWN]:
            posicion_nave[1] = posicion_nave[1] + 1




##############      DISPARO DE LA NAVE      #####################
       if pygame.K_SPACE and (lista_teclas[pygame.K_UP] or lista_teclas[pygame.K_DOWN]) and lista_teclas[pygame.K_LEFT]:
            disparar = True
        else:
            disparar = False

       

 #  establce la pósiccion inicial del disparo
    #actualizar disparo
    for disparos in disparos_nave:
        disparos.y -= 4 #mueve el disparo hacia arriba en el eje "y"(velocidad del disparo)
    
            
            

#############     PARA QUE NO SALGA DE LA VENTANA    ##################            
        if posicion_nave[0] > ANCHO_VENTANA-10:
            posicion_nave[0] = -90 
            print(posicion_nave)
        elif posicion_nave[0] < -90:
            posicion_nave[0] = ANCHO_VENTANA-10
            print(posicion_nave)

        if posicion_nave[1] > ALTO_VENTANA-10:
            posicion_nave[1] = -90 
        elif posicion_nave[1] < -90:
            posicion_nave[1] = ALTO_VENTANA-10


#############    CREAR VARIOS DE ENEMIGOS  ENEMIGOS        #######################
    posicion_varios_enemigos = []
    espacio_entre_enemigos = 10
    for i in range(10):
        x = 200 + i * (ANCHO_ENEMIGO + espacio_entre_enemigos)
        y = 100
        posicion_varios_enemigos.append((x, y))


    
##### FILL= PONE EL COLOR A LA PANTALLA Y DE ACA PARA ABAJO IMPRIME $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    #pantalla.fill(COLOR_NEGRO)
 
    pantalla.blit(fondo_principal_redimensionado,(0,0))
#disparo
    for disparos in disparos_nave:
        pygame.draw.rect(pantalla,COLOR_BLANCO,(disparos))

    #FUNDIR IMAGENES/TEXTOS EN LA PANTALLA   
    for posicion in posicion_varios_enemigos:
        pantalla.blit(imagen_enemigo_1_redimensionada, posicion)
    pantalla.blit(imagen_nave_principal_redimensionada,(posicion_nave))

 
    pantalla.blit(texto,(370,10))
     #MOSTRAR los cambios de la pantalla SIEMPRE ponerlo alfinal para que actualize
    pygame.display.flip()

pygame.quit() 
"""



#POO


import pygame
import colores
from galaga_enemigos import Nave

ANCHO_VENTANA = 600
ALTO_VENTANA = 600

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("Mi primer POo")
reloj = pygame.time.Clock()

imagen_galaxia = pygame.image.load("galaxia-fondo.png")
imagen_galaxia = pygame.transform.scale(imagen_galaxia,(ANCHO_VENTANA, ALTO_VENTANA))



#Creacion de mi personaje (constructor)
personaje1 = Nave()


flag_correr = True
while flag_correr:
    lista_evento = pygame.event.get()
    for evento in lista_evento:
        if evento.type == pygame.QUIT:
            flag_correr = False

        """  keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            personaje1.rect.x = personaje1.rect.x + 4
            personaje1.actualizar()
        if keys[pygame.K_LEFT]:
            personaje1.rect.x = personaje1.rect.x - 4
            personaje1.actualizar()
        if keys[pygame.K_DOWN]:
            personaje1.rect.y = personaje1.rect.y + 4
            personaje1.actualizar()
        if keys[pygame.K_UP]:
            personaje1.rect.y = personaje1.rect.y - 4
            personaje1.actualizar()"""

    milis = reloj.tick(8) #cada 8 miliss da una vuelta al while(60)valor
    pantalla.blit(imagen_galaxia,imagen_galaxia.get_rect())
    #dibujar mi personaje
    personaje1.dibujar(pantalla)
    #personaje1.dibujar_rectangulo(pantalla)

    pygame.display.flip()

pygame.quit