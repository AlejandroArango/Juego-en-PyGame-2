import pygame
 
import constantes
import plataformas
 
class Nivel():
    """ aca definimos que se utilizara en cada nivel, adicionamos sub clases por nivel. """
 
    def __init__(self, jugador):
        """ Constructor. Pass in a handle to jugador. Needed for when moving plataformas
            collide with the jugador. """
 
        # lista de sprites que se usaran en el nivel
        self.platform_list = None
        self.enemy_list = None
 
        # imagen de fondo
        self.background = None
 
        # que tan lejos llega el nivel
        self.world_shift = 0
        self.level_limit = -1000 #distancia maxima
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.jugador = jugador
 
    # actualizacion de cada nivel
    def update(self):
        """ actualizacion de todas las listas."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, pantalla):
        """ clase que dibuja todo del nivel que la invoca. """
 
        # dibujamos el fondo que nos da sensacion de profundidad
        pantalla.fill(constantes.color_azul)
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
 
# creamos los niveles, clase por nivel
class Nivel_01(Nivel):
    """ nivel 1. """
 
    def __init__(self, jugador):
        """ crear nivel 1 1. """
 
        # llamamos al padre constructor
        Nivel.__init__(self, jugador)
 
        self.background = pygame.image.load("background_01.png").convert()
        self.background.set_colorkey(constantes.color_blanco)
        self.level_limit = -2500#limite del nivel
 
		#vector con los diferentes tipos de plataformas con sus respectivas posiciones X y Y para ubicarlas
        level = [ [plataformas.GRASS_LEFT, 500, 500],
                  [plataformas.GRASS_MIDDLE, 570, 500],
                  [plataformas.GRASS_RIGHT, 640, 500],
                  [plataformas.GRASS_LEFT, 800, 400],
                  [plataformas.GRASS_MIDDLE, 870, 400],
                  [plataformas.GRASS_RIGHT, 940, 400],
                  [plataformas.GRASS_LEFT, 1000, 500],
                  [plataformas.GRASS_MIDDLE, 1070, 500],
                  [plataformas.GRASS_RIGHT, 1140, 500],
                  [plataformas.STONE_PLATFORM_LEFT, 1120, 280],
                  [plataformas.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [plataformas.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
 
 
        # añadimos plataformas
        for platform in level:
            block = plataformas.Plataforma(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.jugador = self.jugador
            self.platform_list.add(block)
 
        # adicionamos una plataforma en movimiento
        block = plataformas.MovimientoPlataforma(plataformas.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.jugador = self.jugador
        block.level = self
        self.platform_list.add(block)
 
 
# creamos nivel 2
class Nivel_02(Nivel):
    """ nivel 2. """
 
    def __init__(self, jugador):
        """ crear nivel 1. """
 
        # padre constructor
        Nivel.__init__(self, jugador)
 
        self.background = pygame.image.load("background_02.png").convert()
        self.background.set_colorkey(constantes.color_blanco)
        self.level_limit = -1000
 
        #vector con los diferentes tipos de plataformas con sus respectivas posiciones X y Y para ubicarlas
        level = [ [plataformas.STONE_PLATFORM_LEFT, 500, 550],
                  [plataformas.STONE_PLATFORM_MIDDLE, 570, 550],
                  [plataformas.STONE_PLATFORM_RIGHT, 640, 550],
                  [plataformas.GRASS_LEFT, 800, 400],
                  [plataformas.GRASS_MIDDLE, 870, 400],
                  [plataformas.GRASS_RIGHT, 940, 400],
                  [plataformas.GRASS_LEFT, 1000, 500],
                  [plataformas.GRASS_MIDDLE, 1070, 500],
                  [plataformas.GRASS_RIGHT, 1140, 500],
                  [plataformas.STONE_PLATFORM_LEFT, 1120, 280],
                  [plataformas.STONE_PLATFORM_MIDDLE, 1190, 280],
                  [plataformas.STONE_PLATFORM_RIGHT, 1260, 280],
                  ]
 
 
        # añadimos plataformas
        for platform in level:
            block = plataformas.Plataforma(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.jugador = self.jugador
            self.platform_list.add(block)
 
       # adicionamos una plataforma en movimiento
        block = plataformas.MovimientoPlataforma(plataformas.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.jugador = self.jugador
        block.level = self
        self.platform_list.add(block)