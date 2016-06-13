"""
enemigo Goomba.
"""
import pygame

import constantes

from plataformas import MovimientoPlataforma
from funcion_sprites import Sprite

class EnemigoGoomba(pygame.sprite.Sprite):
	# -- Methods
	def __init__(self, x, y):

		""" Constructor function """

		# Call the parent's constructor
		super().__init__()

		# atributos
		# velocidad inicial del enemigo
		self.change_y = 0
		self.velocidad = 1
		# vectores que guardan los movimientos del enemigo (sprites)
		self.walking_frames = []

		# List of sprites we can bump against
		self.level = None
		self.jugador = None
		
		#cargamos el sprite de goomba
		sprite_imagen = Sprite("img/goomba40x40.png")
		
		# cargamos el sprite de goomba
		image = sprite_imagen.get_imagen(0, 0, 40, 40)
		self.walking_frames.append(image)
		image = sprite_imagen.get_imagen(40, 0, 40, 40)
		self.walking_frames.append(image)
		image = sprite_imagen.get_imagen(80, 0, 40, 40)
		self.walking_frames.append(image)

		# cargamos el sprite de goomba inicial.
		self.image = self.walking_frames[0]

		#
		self.rect = self.image.get_rect()
		#inicialmente camina hacia la izquierda.
		self.derecha = False
		#sirve para la animacion.
		self.contFrames = 0

		self.rect.x = x
		self.rect.y = y
 
	def update(self):
		""" Move the jugador. """
		# gravedad
		self.gravedad()
		self.contFrames += 1
		# Mover izquierda/derecha
		#print(self.level.world_shift)
		if self.derecha:
			self.rect.x += self.velocidad
		else:
			self.rect.x -= self.velocidad
		if self.contFrames > 5:
			self.image = self.walking_frames[1]
			if self.contFrames >10:
				self.image = self.walking_frames[0]
				self.contFrames = 0

		# See if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if self.derecha:
				if block.rect.x == self.rect.right:
					self.derecha = False
			else:
				print (block.rect.topright)
				if block.rect.right == self.rect.x:
					print ("HOLA")
					self.derecha = True

		# Move up/down
		self.rect.y += self.change_y

		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
 
			# Reset our position based on the top/bottom of the object.
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom

			# Stop our vertical movement
			self.change_y = 0

			if isinstance(block, MovimientoPlataforma):
				self.rect.x += block.change_x
 
	def gravedad(self):
		""" calcula efecto de la gravedad. """
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .35#cuanto disminuimos cuando caemos

		# verificar si estamos en el suelo
		if self.rect.y >= constantes.alto_pantalla - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = constantes.alto_pantalla - self.rect.height