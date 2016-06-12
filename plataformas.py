""" 
administrar la plataforma, aca ira todo el diseño de obstaculos
"""
import pygame
 
from funcion_sprites import Sprite
 
# variables que se tomaran para pintar las plataformas
#nombre objeto		     x	  y	  xtam/ytam

#################################  nivel 1

suelo_inicio           = (140,  0, 70, 40)

cuerda_a			   = (420, 70, 70, 70)
cuerda_b			   = (350,840, 70, 70)

inicio_izq_a           = (140,420, 70, 70)
inicio_der_a           = (140,280, 70, 70)

inicio_izq_b           = (140, 70, 70, 40)
inicio_cen_b           = (140,  0, 70, 40)
inicio_der_b           = ( 70,840, 70, 40)

bloque_muro_a		   = (140,560, 70, 70)
bloque_muro_b	 	   = (140,630, 70, 40)
bloque_muro_c	 	   = (140,600, 70, 30)

inicio_izquierdo       = (140,350, 70, 70)
inicio_centro          = ( 70,420, 70, 70)
inicio_derecho         = (140,210, 70, 70)

inicio_plat_mov        = (140,140, 70, 40)

#################################  nivel 2

suelo_bosque           = (560,280, 70, 40)

agua				   = (420,560, 70, 70)

bosque_izq_a           = (560,700, 70, 70)
bosque_der_a           = (560,560, 70, 70)

bosque_izq_b           = (560,350, 70, 40)
bosque_cen_b           = (560,280, 70, 40)
bosque_der_b           = (560,210, 70, 40)

bloque_bosque_a		   = (560,840, 70, 70)
bloque_bosque_b	 	   = (630,  0, 70, 40)
bloque_bosque_c	 	   = (560,840, 70, 30)

bosque_izquierdo       = (560,630, 70, 70)
bosque_centro          = (490,560, 70, 70)
bosque_derecho         = (560,490, 70, 70)

bosque_plat_mov        = (560,420, 70, 40)

#################################  nivel 3

suelo_desierto         = (350,280, 70, 40)

lava				   = (420,770, 70, 70)

desierto_izq_curva_a   = (350,700, 70, 70)
desierto_der_curva_a   = (350,560, 70, 70)

desierto_izq_curva_b   = (350,630, 70, 70)
desierto_der_curva_b   = (350,490, 70, 70)

desierto_centro        = (280,560, 70, 70)#sirve para curva a o b

desierto_completo_izq  = (280,530, 70, 70)
desierto_completo_der  = (280,490, 70, 70)

desierto_izq_plano_a   = (350,350, 70, 40)
desierto_cen_plano_a   = (350,280, 70, 40)
desierto_der_plano_a   = (350,210, 70, 40)


desierto_plat_madera   = (280,740, 70, 30)
desierto_plataforma    = (350,420, 70, 40)

bloque_desierto    	   = (560,840, 70, 70)
bloque_desierto_arriba = (350,770, 70, 40)


desierto_esqui_izq     = (350,350, 30, 40)
desierto_esqui_der 	   = (390,210, 30, 40)
	
class Plataforma(pygame.sprite.Sprite):
    """ Plataforma que se usa para saltar en ella """
 
    def __init__(self, sprite_imagen_data):

        super().__init__()
 
        sprite_imagen = Sprite("img/tiles_spritesheet.png")
        # toma la imagen para la plataforma
        self.image = sprite_imagen.get_imagen(sprite_imagen_data[0],#pos x
                                              sprite_imagen_data[1],#pos y
                                              sprite_imagen_data[2],#ancho
                                              sprite_imagen_data[3])#alto
 
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