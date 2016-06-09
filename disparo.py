""" 
disparos del jugador.
"""
import pygame

import constantes

from plataformas import MovimientoPlataforma
from funcion_sprites import Sprite

class DisparoJugador(pygame.sprite.Sprite):
	""" Esta clase representa los disparos del jugador. """
	
	# -- Methods
	def __init__(self, x, y, right): # donde derecha indica true si el disparo es hacia la derecha

		""" Constructor function """

		# Call the parent's constructor
		super().__init__()

		# atributos
		# velocidad del disparo
		self.velocidad = 0

		# vectores que guardan los animaciones del disparo (sprites)
		self.shot_frames = []

		# posicion y direccion del jugador
		self.direction = 0
		
		#cargamos el sprite del disparo.
		sprite_imagen = Sprite("img/disparos31x31.png")

		self.level = None
		self.lista_sprites_activos = None
		
		# cargamos el sprite del disparo DERECHA
		image = sprite_imagen.get_imagen(0, 0, 31, 31)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(31, 0, 31, 31)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(62, 0, 31, 31)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(93, 0, 31, 31)
		self.shot_frames.append(image)	
		image = sprite_imagen.get_imagen(124, 0, 31, 31)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(155, 0, 31, 31)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(186, 0, 31, 31)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(217, 0, 31, 31)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(248, 0, 31, 31)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(279, 0, 31, 31)
		self.shot_frames.append(image)

		# cargamos el sprite del personaje principal IZQUIERDA
		image = sprite_imagen.get_imagen(0, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(31, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(62, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(93, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)	
		image = sprite_imagen.get_imagen(124, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(155, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(186, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(217, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(248, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)
		image = sprite_imagen.get_imagen(279, 0, 31, 31)
		image = pygame.transform.flip(image, True, False)
		self.shot_frames.append(image)

		self.image = self.shot_frames[0]
		self.rect = self.image.get_rect()

		#en shot_frames esta la animacion del disparo y se compone de la siguiente manera
		#10 sprites disparo a la derecha de los cuales 5 son el disparo y 5 son el impacto

		posicion = (x,y)
		self.rect.x = posicion[0]
		self.rect.y = posicion[1]

		self.derecha = right
		self.contFrames = 0

		self.colision = False
		pygame.mixer.Sound("sound/laser.wav").play()
 
	def update(self):
		if self.velocidad == 0:
			if self.derecha:
				self.velocidad = 5
			else:
				self.velocidad = -5
		if not self.colision:
			self.contFrames += 1
			if self.contFrames < 10:
				if self.derecha:
					self.image = self.shot_frames[0]
				else:
					self.image = self.shot_frames[10]
			else:
				if self.contFrames < 20:
					if self.derecha:
						self.image = self.shot_frames[1]
					else:
						self.image = self.shot_frames[11]
				else:
					if self.contFrames < 30:
						if self.derecha:
							self.image = self.shot_frames[2]
						else:
							self.image = self.shot_frames[12]
					else:
						if self.contFrames < 40:
							if self.derecha:
								self.image = self.shot_frames[3]
							else:
								self.image = self.shot_frames[13]
						else:
							if self.contFrames < 50:
								if self.derecha:
									self.image = self.shot_frames[4]
								else:
									self.image = self.shot_frames[14]
							else:
								if self.contFrames > 70: #DEBO BORRAR EL DISPARO DE LA LISTA DE DISPAROS.
									self.colision = True
									self.contFrames = 0

			self.rect.x += self.velocidad

			block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
			for block in block_hit_list:
				self.colision = True
				self.contFrames = 0
				
		else:
			self.contFrames += 1
			if self.contFrames < 5:
				if self.derecha:
					self.image = self.shot_frames[5]
				else:
					self.image = self.shot_frames[15]
			else:
				if self.contFrames < 10:
					if self.derecha:
						self.image = self.shot_frames[6]
					else:
						self.image = self.shot_frames[16]
				else:
					if self.contFrames < 15:
						if self.derecha:
							self.image = self.shot_frames[7]
						else:
							self.image = self.shot_frames[17]
					else:
						if self.contFrames < 20:
							if self.derecha:
								self.image = self.shot_frames[8]
							else:
								self.image = self.shot_frames[18]
						else:
							if self.contFrames < 25:
								if self.derecha:
									self.image = self.shot_frames[9]
								else:
									self.image = self.shot_frames[19]
							else:
								if self.contFrames < 30: #DEBO BORRAR EL DISPARO DE LA LISTA DE DISPAROS.
									self.lista_sprites_activos.remove(self)

