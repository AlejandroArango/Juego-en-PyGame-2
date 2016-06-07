""" 
jugador.
"""
import pygame

import constantes

from plataformas import MovimientoPlataforma
from funcion_sprites import Sprite

class JugadorPrincipal(pygame.sprite.Sprite):
	""" This class represents the bar at the bottom that the jugador
	controls. """
  
	# -- Methods
	def __init__(self):

		""" Constructor function """

		# Call the parent's constructor
		super().__init__()

		# atributos
		# velocidad inicial del jugador
		self.change_x = 0
		self.change_y = 0

		# vectores que guardan los movimientos del jugador (sprites)
		self.walking_frames_l = []
		self.walking_frames_r = []

		# posicion inicial del jugador
		self.direction = "R"

		# List of sprites we can bump against
		self.level = None
		
		#cargamos el sprite del personaje principal
		sprite_imagen = Sprite("img/mega1.png")
		
		# cargamos el sprite del personaje principal DERECHA
		image = sprite_imagen.get_imagen(0, 0, 56, 58)
		self.walking_frames_r.append(image)
		image = sprite_imagen.get_imagen(56, 0, 56, 58)
		self.walking_frames_r.append(image)
		image = sprite_imagen.get_imagen(112, 0, 56, 58)
		self.walking_frames_r.append(image)
		image = sprite_imagen.get_imagen(168, 0, 56, 58)
		self.walking_frames_r.append(image)	
		image = sprite_imagen.get_imagen(224, 0, 56, 58)
		self.walking_frames_r.append(image)
		image = sprite_imagen.get_imagen(280, 0, 56, 58)
		self.walking_frames_r.append(image)

		# cargamos el sprite del personaje principal IZQUIERDA
		image = sprite_imagen.get_imagen(0, 0, 56, 58)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_imagen.get_imagen(56, 0, 56, 58)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_imagen.get_imagen(112, 0, 56, 58)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_imagen.get_imagen(168, 0, 56, 58)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_imagen.get_imagen(224, 0, 56, 58)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)
		image = sprite_imagen.get_imagen(280, 0, 56, 58)
		image = pygame.transform.flip(image, True, False)
		self.walking_frames_l.append(image)


		# cargamos el sprite del personaje principal mirando DERECHA
		self.image = self.walking_frames_r[0]

		#
		self.rect = self.image.get_rect()
 
	def update(self):
		""" Move the jugador. """
		# gravedad
		self.gravedad()

		# Mover izquierda/derecha
		self.rect.x += self.change_x
		pos = self.rect.x + self.level.world_shift
		if self.direction == "R":
			frame = (pos // 30) % len(self.walking_frames_r)
			self.image = self.walking_frames_r[frame]
		else:
			frame = (pos // 30) % len(self.walking_frames_l)
			self.image = self.walking_frames_l[frame]

		# See if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# If we are moving right,
			# set our right side to the left side of the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right
 
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

	def saltar(self):
		"""funcion saltar. """

		# interaccion con plataformas en movimiento
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2

		# saltar
		if len(platform_hit_list) > 0 or self.rect.bottom >= constantes.alto_pantalla:
			self.change_y = -10#determina que tan alto llegamos cuando saltamos

	# JugadorPrincipal-control de movimientos:
	def ir_izquierda(self):
		self.change_x = -7#determina la velocidad de movimiento
		self.direction = "L"

	def ir_derecha(self):
		self.change_x = 7#determina la velocidad de movimiento
		self.direction = "R"

	def detenerse(self):
		self.change_x = 0#si nos detenemos