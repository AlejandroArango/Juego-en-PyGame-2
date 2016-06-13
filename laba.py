""" 
administrar la plataforma, aca ira todo el diseno de obstaculos
"""
import pygame
 
from funcion_sprites import Sprite

class EnemigoLaba(pygame.sprite.Sprite):
 
    def __init__(self, sprite_imagen_data):

        super().__init__()
 
        sprite_imagen = Sprite("img/laba.png")

        self.image = sprite_imagen.get_imagen(sprite_imagen_data[0],#pos x
                                              sprite_imagen_data[1],#pos y
                                              sprite_imagen_data[2],#ancho
                                              sprite_imagen_data[3])#alto
 
        self.rect = self.image.get_rect()
 
 
class EnemigoLabaMov(Plataforma):
 
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
            self.jugador.salud -= 1
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
            self.jugador.salud -= 1
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