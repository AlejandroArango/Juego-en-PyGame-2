"""
administrar la plataforma, aca ira todo el diseño de obstaculos
"""
import pygame
 
from funcion_sprites import Sprite
 
# variables que se tomaran para pintar las plataformas
 
GRASS_LEFT            = (576, 720, 70, 70)
GRASS_RIGHT           = (576, 576, 70, 70)
GRASS_MIDDLE          = (504, 576, 70, 70)
STONE_PLATFORM_LEFT   = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT  = (792, 648, 70, 40)
 
class Plataforma(pygame.sprite.Sprite):
    """ Plataforma que se usa para saltar en ella """
 
    def __init__(self, sprite_imagen_data):
        """ constructor de la Plataforma. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        sprite_imagen = Sprite("tiles_spritesheet.png")
        # toma la imagen para la plataforma
        self.image = sprite_imagen.get_imagen(sprite_imagen_data[0],
                                              sprite_imagen_data[1],
                                              sprite_imagen_data[2],
                                              sprite_imagen_data[3])
 
        self.rect = self.image.get_rect()
 
 
class MovimientoPlataforma(Plataforma):
    """ clase que determina los movimientos de la plataforna. """
 
    def __init__(self, sprite_imagen_data):
 
        super().__init__(sprite_imagen_data)
 
        self.change_x = 0
        self.change_y = 0
 
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0
 
        self.level = None
        self.jugador = None
 
    def update(self):
        """ actualiza para ver la interaccion del jugador con la plataforma en movimiento. """
 
 
        # mover izquierda/derecha
        self.rect.x += self.change_x
 
        # ver si colisiono con el jugador
        hit = pygame.sprite.collide_rect(self, self.jugador)
        if hit:
			#si vamos a la derecha verifica con el lado izquierdo de la plataforma
            if self.change_x < 0:
                self.jugador.rect.right = self.rect.left
            else:
                # lo contrario
                self.jugador.rect.left = self.rect.right
 
        # mover arriba/abajo
        self.rect.y += self.change_y
 
        # verifica si choco con el jugador
        hit = pygame.sprite.collide_rect(self, self.jugador)
        if hit:
            # igual que el de izquierda/derecha, solo que este recrea la posicion
            # original, dezplasandolo arriba o abajo
            if self.change_y < 0:
                self.jugador.rect.bottom = self.rect.top
            else:
                self.jugador.rect.top = self.rect.bottom
 
        # verifica el limite para invertir la direccion
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
 
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1