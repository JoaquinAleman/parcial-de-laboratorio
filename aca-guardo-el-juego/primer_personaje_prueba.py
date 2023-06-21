import pygame
import colores

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

           