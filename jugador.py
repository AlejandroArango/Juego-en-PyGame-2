""" 
jugador.
"""
import pygame

import constantes

from plataformas import MovimientoPlataforma

from funcion_sprites import Sprite

class JugadorPrincipal(pygame.sprite.Sprite):

	# -- Methods
	def __init__(self):
	

		# Call the parent's constructor
		super(self).__init__()
		
		#salud del jugador
		self.salud = 100		
		self.var   =   0

		self.puntaje = 0
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
		""" movimiento del jugador. """

		# gravedad		
		self.gravedad()		
		
		# Mover izquierda/derecha
		
		self.rect.x += self.change_x
		pos = self.rect.x + self.level.world_shift			
		
		#print ("posicion X  " + str(pos) + "  cambio Y " + str(self.rect.y+58))
		
		if self.direction == "R":
			frame = (pos // 30) % len(self.walking_frames_r)
			self.image = self.walking_frames_r[frame]
			
		else:
			frame = (pos // 30) % len(self.walking_frames_l)
			self.image = self.walking_frames_l[frame]		
			

		# verificar si chocamos con algo que va de izquierda a derecha
		
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		
		for block in block_hit_list:
			if block.esEnemigo:
				self.salud -= 0.5
			# If we are moving right,
			# set our right side to the left side of the item we hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				# Otherwise if we are moving left, do the opposite.
				self.rect.left = block.rect.right
 
		# mover arriba / abajo
		
		self.rect.y += self.change_y

		# verifica si chocamos con algo que sube o baja
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if block.esEnemigo:
				self.salud -= 0.5
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
			self.change_y = -9#determina que tan alto llegamos cuando saltamos

	# JugadorPrincipal-control de movimientos:
	def ir_izquierda(self):
		self.change_x = -7#determina la velocidad de movimiento
		self.direction = "L"

	def ir_derecha(self):
		self.change_x = 7#determina la velocidad de movimiento
		self.direction = "R"

	def detenerse(self):
		self.change_x = 0#si nos detenemos

	def getPosicion(self): # retorna la posicion del jugador.
		return (self.rect.x, self.rect.y)

	def getDerecha(self): # retorna True si el jugador mira a la derecha
		if self.direction == "R":
			return True
		else:
			return False

	def chocar_lava_acido(self):
	
		self.salud -= 5

	def menosVida(self):

		self.salud = self.salud - 1
