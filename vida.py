import pygame
import sys
import random
import constantes
from pygame.locals import *


class Vida(pygame.sprite.Sprite):

	def Vida(self, pantalla, numero):
	
		pygame.sprite.Sprite.__init__(self)
		self.bien = constantes.color_verde
		self.mal  = constantes.color_red
		if numero>50:
			pygame.draw.rect(pantalla, self.bien, [10, 10, (numero*2), 20])
		else:
			pygame.draw.rect(pantalla, self.mal, [10, 10, (numero*2), 20])
