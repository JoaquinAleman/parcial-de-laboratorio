"""
import pygame
import colores

 
def getSuperficies(path,filas,columnas):
        lista= []
        superficie_imagen = pygame.image.load(path)
        fotograma_ancho = int(superficie_imagen.get_width()/columnas)
        fotograma_alto = int(superficie_imagen.get_height()/filas)

        for fila in range(filas):
            for columna in range(columnas):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                superficie_fotograma = superficie_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
                lista.append(superficie_fotograma)
        
        return lista        


class Personaje: 
        def __init__(self) -> None:                   #nombre,cantidad de fotos
            self.caminar = getSuperficies("nombre del sprite",1,3)
            self.paso1 = 0
            self.score = 0
            self.animacion = self.caminar
            self.imagen = self.animacion[self.paso1]
            self.rect = self.imagen.get_rect()
            self.rect.y = 500

        def actualizar(self):
            #paso los fotogramas del movimiento caminar
            if(self.paso1 < len(self.animacion)-1):
                self.paso1 += 1
            else:
                self.paso1 = 0    
        
        def dibujar(self, pantalla):
            self.imagen = self.animacion[self.paso1]
            pantalla.blit(self.imagen, self.rect)



"""
"""
#PARA CONVERTIR IMAGENES A PNG = https://pixlr.com/es/x/#editor

 TAMBIEN ESTA LA QUE PASO EL PROFE LA LISTA DE COLORES
 $$$$$$$$$$$$   PARA LOS COLORESS   $$$$$$$$$$$$$$
https://www.w3schools.com/colors/colors_rgb.asp

#########    SONIDOS     ##################
http://www.sonidosmp3gratis.com/download.php?id=895&sonido=pelota%20tenis
"""
###########     CLASE POR PRFE YANI     ###########
import pygame
import colores
from constantes import *

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

class Personaje:
    def __init__(self) -> None:
        self.caminar = getSuperficies("l2.png",1,6)#12
        """ self.escala = 1.5 # Define el factor de escala deseado

        self.caminar = [pygame.transform.scale(fotograma, (fotograma.get_width() * self.escala, fotograma.get_height() * self.escala)) for fotograma in self.caminar]
        """
        self.paso1 = 0
        self.score = 0
        self.animacion = self.caminar
        self.imagen = self.animacion[self.paso1]
        self.rect = self.imagen.get_rect()
        self.rect.y = 400
        #self.rect.x -= 19 #con esto manejo
        

    def actualizar(self):
        #paso los fotogramas del movimiento caminar
        if(self.paso1 < len(self.animacion)-1):
            self.paso1 += 1 
        else:
            self.paso1 = 0

    def dibujar(self, pantalla):
        self.imagen = self.animacion[self.paso1]
        pantalla.blit(self.imagen, self.rect)


    def dibujar_rectangulo(self, pantalla):
        pygame.draw.rect(pantalla, colores.RED1, self.rect, 2)

#es el que se mueve
class FondoJuego:
    def __init__(self, ruta, medidas) -> None:
       self.imagen = pygame.image.load(ruta)
       self.imagen = pygame.transform.scale(self.imagen, medidas)
       self.rect = self.imagen.get_rect()

    def mostrar(self, pantalla, x, y):
        y_relativa = y % self.rect.height
        pantalla.blit(self.imagen,(x, y_relativa - self.rect.height))
        if y_relativa < pantalla.get_rect().height:
            pantalla.blit(self.imagen, (x, y_relativa))
        y += 1



#es el que esta quieto lo uso para Start-opciones
class FondoPantalla:
    def __init__(self, ruta, medidas) -> None:
       self.imagen = pygame.image.load(ruta)
       self.imagen = pygame.transform.scale(self.imagen, medidas)
       self.rect = self.imagen.get_rect()
       self.rect.y = POS_TOP_BOTON
       self.rect.x = POST_LEFT_BOTON

    def mostrar(self, pantalla, x, y):
        pantalla.blit(self.imagen, (x, y))
    
           
#tranfomarciaoi de scala = https://www.pygame.org/docs/ref/transform.html#pygame.transform.flip
