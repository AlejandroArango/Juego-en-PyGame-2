""" 
tomar sprites individuales de una imagen de sprite
"""
import pygame
 
import constantes
 
class Sprite(object):
    """Clase para tomar imágenes de una imagen de sprites """
 
    def __init__(self, archivo):
        """ Constructor. le llega el nombre de la imagen de sprites. """
 
        # cargar sprites
        self.sprite_imagen = pygame.image.load(archivo).convert()
 
 
    def get_imagen(self, x, y, width, height):
        """ para tomar un sprite de una imagen de sprites, llega x,y,ancho,alto. """
 
        # crea una imagen en blanco
        image = pygame.Surface([width, height]).convert()
 
        # toma un sprite de una imagen de sprites
        image.blit(self.sprite_imagen, (0, 0), (x, y, width, height))
 
        # determina el colo de la tranparencia
        image.set_colorkey(constantes.color_negro)
 
        # retorna la imagen
        return image