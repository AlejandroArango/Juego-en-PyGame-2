import pygame 
 
import constantes
import jugador
from jugador import JugadorPrincipal
import plataformas

# definimos pantalla
tamano_pantalla = [constantes.ancho_pantalla, constantes.alto_pantalla]
pantalla = pygame.display.set_mode(tamano_pantalla)
 
class Nivel():
 
    def __init__(self, jugador):
        """ Constructor"""
 
        # lista de sprites que se usaran en el nivel
        self.platform_list = None
        self.enemy_list = None
		
        self.barra_salud = None
		
        # imagen de fondo
        self.background = None
 
        # que tan lejos llega el nivel
        self.world_shift = 0
        self.level_limit = -1000 #distancia maxima
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
		
        self.barra_salud = pygame.sprite.Group()	
		
        self.jugador = jugador
 
    # actualizacion de cada nivel
    def update(self):
        """ actualizacion de todas las listas."""
        self.barra_salud.update()		
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, pantalla):
        """ clase que dibuja todo del nivel que la invoca. """
 
        # dibujamos el fondo que nos da sensacion de profundidad
        pantalla.fill(constantes.color_blanco)
        pantalla.blit(self.background,(self.world_shift // 3,0))
 
        # dibujamos todas las listas que tenemos guardadas
        self.platform_list.draw(pantalla)
        self.enemy_list.draw(pantalla)

 
    def shift_world(self, shift_x):
        """ aca determinamos si el jugador se mueve derecha/izquierda para mover todo el entorno: """
 
        # vamos guardando cuando se ha movido
        self.world_shift += shift_x
		
        # vamos determinando todas las listas de sprites
        for platform in self.platform_list:
            platform.rect.x += shift_x
            
        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
			
			
			
			