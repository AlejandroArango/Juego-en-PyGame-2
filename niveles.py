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
 
# creamos los niveles, clase por nivel
class Nivel_01(Nivel):
    """ nivel 1. """
 
    def __init__(self, jugador):
        """ crear nivel 1 1. """

        # llamamos al padre constructor
        Nivel.__init__(self, jugador)
 
        self.background = pygame.image.load("img/prueba.png").convert_alpha()
        self.background.set_colorkey(constantes.color_blanco)
        self.level_limit = -50#-5000 #limite del nivel
		

		
		#vector con los diferentes tipos de plataformas con sus respectivas posiciones X y Y para ubicarlas
        level = [ 
                  [plataformas.bloque_muro_a,   -700, 530],
				  [plataformas.bloque_muro_a,   -700, 460],
                  [plataformas.bloque_muro_a,   -700, 390],		
                  [plataformas.bloque_muro_a,   -700, 320],
                  [plataformas.bloque_muro_a,   -700, 250],				  
                  [plataformas.bloque_muro_a,   -700, 180],		
				  [plataformas.bloque_muro_c,   -700, 150],
                  [plataformas.bloque_muro_b,   -700, 110],		
		
		
#############################posicion X 0 guantes, botas	
				  [plataformas.inicio_izquierdo,500, 530],
                  [plataformas.inicio_centro,   570, 530],
                  [plataformas.inicio_derecho,  640, 530],
				  
                  [plataformas.inicio_izquierdo,810, 420],
                  [plataformas.inicio_centro,   880, 420],
                  [plataformas.inicio_derecho,  950, 420],

                  [plataformas.inicio_izq_a,   1460, 110],
                  [plataformas.inicio_der_a,   1530, 110],
				  
                  [plataformas.inicio_izq_b,   1160, 110],
                  [plataformas.inicio_cen_b,   1230, 110],
                  [plataformas.inicio_der_b,   1300, 110],				  

                  [plataformas.inicio_izq_a,    930, 110],
                  [plataformas.inicio_der_a,   1000, 110],	

                  [plataformas.inicio_izq_a,    220, 160],
                  [plataformas.inicio_centro,   290, 160],
                  [plataformas.inicio_der_a,    360, 160],		
				  
                  [plataformas.cuerda_a,        1850,  0],
                  [plataformas.cuerda_b,        1850, 70],
                  [plataformas.cuerda_b,        1850,140],	
                  [plataformas.cuerda_b,        1850,210],				  
				  
#############################posicion X 1700 casco

                  [plataformas.inicio_izquierdo,2000, 530],
                  [plataformas.inicio_centro,   2070, 530],
				  [plataformas.inicio_derecho,  2140, 530],
				  
                  [plataformas.inicio_izquierdo,2790, 530],
				  [plataformas.inicio_centro,   2860, 530],
                  [plataformas.inicio_derecho,  2930, 530],
				  
                  [plataformas.inicio_izquierdo,2395, 430],
				  [plataformas.inicio_centro,   2465, 430],
                  [plataformas.inicio_derecho,  2535, 430],				  
				  
                  [plataformas.inicio_izquierdo,2000, 330],
                  [plataformas.inicio_centro,   2070, 330],
				  [plataformas.inicio_derecho,  2140, 330],
				  
                  [plataformas.inicio_izquierdo,2790, 330],
				  [plataformas.inicio_centro,   2860, 330],
                  [plataformas.inicio_derecho,  2930, 330],	

                  [plataformas.inicio_izquierdo,2395, 230],
				  [plataformas.inicio_centro,   2465, 230],
                  [plataformas.inicio_derecho,  2535, 230],	
				  
#############################posicion X 3000 boss	



                  [plataformas.bloque_muro_a,   3400, 530],#muro campo boss
				  [plataformas.bloque_muro_a,   3400, 460],
                  [plataformas.bloque_muro_a,   3400, 390],		
                  [plataformas.bloque_muro_a,   3400, 320],
                  [plataformas.bloque_muro_a,   3400, 250],				  
                  [plataformas.bloque_muro_a,   3400, 180],
				  [plataformas.bloque_muro_c,   3400, 150],
                  [plataformas.bloque_muro_b,   3400, 110],			  
                  ]
				  			  
 
############################## S U E L O ###################################
        '''pos_y = 600
        pos_x = -700
        while pos_x < 8050:
        #if pos_x <= 3990:
			# adicionamos suelo
            suelo = plataformas.MovimientoPlataforma(plataformas.suelo_inicio)
            suelo.rect.x = pos_x
            suelo.rect.y = pos_y
            pos_x += 70
            suelo.jugador = self.jugador
            suelo.level = self
            self.platform_list.add(suelo)
        print ("H O L A ! ! ! ")		'''
############################################################################			
 
        # añadimos plataformas 1
        for platform in level:
            block = plataformas.Plataforma(platform[0])#imagen x y
            block.rect.x = platform[1]				   #ancho
            block.rect.y = platform[2]				   #alto
            block.jugador = self.jugador
            self.platform_list.add(block)			
 
        # adicionamos una plataforma en movimiento 1
        block = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block.rect.x = 1220
        block.rect.y = 420
        block.boundary_left = 1120
        block.boundary_right = 1400
        block.change_x = 3
        block.jugador = self.jugador
        block.level = self				#añadimos a level la imagen
        self.platform_list.add(block)	
 
        # adicionamos una plataforma en movimiento 2
        block_b = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_b.rect.x = 1470
        block_b.rect.y = 420
        block_b.boundary_left = 1470
        block_b.boundary_right = 1600
        block_b.change_x = 7
        block_b.jugador = self.jugador
        block_b.level = self
        self.platform_list.add(block_b)
 
       # adicionamos una plataforma en movimiento 3
        block_c = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_c.rect.x = 1700
        block_c.rect.y = 110
        block_c.boundary_top = 110
        block_c.boundary_bottom = 380
        block_c.change_y = 1
        block_c.jugador = self.jugador
        block_c.level = self
        self.platform_list.add(block_c)

        # adicionamos una plataforma en movimiento 4
        block_d = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_d.rect.x = 630
        block_d.rect.y = 110
        block_d.boundary_left = 630
        block_d.boundary_right = 780
        block_d.change_x = 3
        block_d.jugador = self.jugador
        block_d.level = self
        self.platform_list.add(block_d)		

################## posicion X 1700

       # adicionamos una plataforma en movimiento 5
        block_c = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_c.rect.x = 3200
        block_c.rect.y = 110
        block_c.boundary_top = 110
        block_c.boundary_bottom = 400
        block_c.change_y = 1
        block_c.jugador = self.jugador
        block_c.level = self
        self.platform_list.add(block_c)	




		
# creamos nivel 2
class Nivel_02(Nivel):
    """ nivel 2. """
 
    def __init__(self, jugador):
        """ crear nivel 1. """
 
        # padre constructor
        Nivel.__init__(self, jugador)
 
        self.background = pygame.image.load("img/background_02.png").convert_alpha()
        #self.background.set_colorkey(constantes.color_negro)
        self.level_limit = -1000
 
		#vector con los diferentes tipos de plataformas con sus respectivas posiciones X y Y para ubicarlas
        level = [ 
                  [plataformas.bloque_muro_a,   -700, 530],
				  [plataformas.bloque_muro_a,   -700, 460],
                  [plataformas.bloque_muro_a,   -700, 390],		
                  [plataformas.bloque_muro_a,   -700, 320],
                  [plataformas.bloque_muro_a,   -700, 250],				  
                  [plataformas.bloque_muro_a,   -700, 180],		
				  [plataformas.bloque_muro_c,   -700, 150],
                  [plataformas.bloque_muro_b,   -700, 110],		
		
		
#############################posicion X 0 guantes, botas	
				  [plataformas.inicio_izquierdo,500, 530],
                  [plataformas.inicio_centro,   570, 530],
                  [plataformas.inicio_derecho,  640, 530],
				  
                  [plataformas.inicio_izquierdo,810, 420],
                  [plataformas.inicio_centro,   880, 420],
                  [plataformas.inicio_derecho,  950, 420],

                  [plataformas.inicio_izq_a,   1460, 110],
                  [plataformas.inicio_der_a,   1530, 110],
				  
                  [plataformas.inicio_izq_b,   1160, 110],
                  [plataformas.inicio_cen_b,   1230, 110],
                  [plataformas.inicio_der_b,   1300, 110],				  

                  [plataformas.inicio_izq_a,    930, 110],
                  [plataformas.inicio_der_a,   1000, 110],	

                  [plataformas.inicio_izq_a,    220, 160],
                  [plataformas.inicio_centro,   290, 160],
                  [plataformas.inicio_der_a,    360, 160],		
				  
                  [plataformas.cuerda_a,        1850,  0],
                  [plataformas.cuerda_b,        1850, 70],
                  [plataformas.cuerda_b,        1850,140],	
                  [plataformas.cuerda_b,        1850,210],				  
				  
#############################posicion X 1700 casco

                  [plataformas.inicio_izquierdo,2000, 530],
                  [plataformas.inicio_centro,   2070, 530],
				  [plataformas.inicio_derecho,  2140, 530],
				  
                  [plataformas.inicio_izquierdo,2790, 530],
				  [plataformas.inicio_centro,   2860, 530],
                  [plataformas.inicio_derecho,  2930, 530],
				  
                  [plataformas.inicio_izquierdo,2395, 430],
				  [plataformas.inicio_centro,   2465, 430],
                  [plataformas.inicio_derecho,  2535, 430],				  
				  
                  [plataformas.inicio_izquierdo,2000, 330],
                  [plataformas.inicio_centro,   2070, 330],
				  [plataformas.inicio_derecho,  2140, 330],
				  
                  [plataformas.inicio_izquierdo,2790, 330],
				  [plataformas.inicio_centro,   2860, 330],
                  [plataformas.inicio_derecho,  2930, 330],	

                  [plataformas.inicio_izquierdo,2395, 230],
				  [plataformas.inicio_centro,   2465, 230],
                  [plataformas.inicio_derecho,  2535, 230],	
				  
#############################posicion X 3000 boss	



                  [plataformas.bloque_muro_a,   3400, 530],#muro campo boss
				  [plataformas.bloque_muro_a,   3400, 460],
                  [plataformas.bloque_muro_a,   3400, 390],		
                  [plataformas.bloque_muro_a,   3400, 320],
                  [plataformas.bloque_muro_a,   3400, 250],				  
                  [plataformas.bloque_muro_a,   3400, 180],
				  [plataformas.bloque_muro_c,   3400, 150],
                  [plataformas.bloque_muro_b,   3400, 110],			  
                  ]
 
 
############################## S U E L O ###################################
        '''pos_y = 600
        pos_x = -700
        while pos_x < 8050:
        #if pos_x <= 3990:
			# adicionamos suelo
            suelo = plataformas.MovimientoPlataforma(plataformas.suelo_inicio)
            suelo.rect.x = pos_x
            suelo.rect.y = pos_y
            pos_x += 70
            suelo.jugador = self.jugador
            suelo.level = self
            self.platform_list.add(suelo)
        print ("H O L A ! ! ! ")		'''
############################################################################			
 
        # añadimos plataformas 1
        for platform in level:
            block = plataformas.Plataforma(platform[0])#imagen x y
            block.rect.x = platform[1]				   #ancho
            block.rect.y = platform[2]				   #alto
            block.jugador = self.jugador
            self.platform_list.add(block)			
 
        # adicionamos una plataforma en movimiento 1
        block = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block.rect.x = 1220
        block.rect.y = 420
        block.boundary_left = 1120
        block.boundary_right = 1400
        block.change_x = 3
        block.jugador = self.jugador
        block.level = self				#añadimos a level la imagen
        self.platform_list.add(block)	
 
        # adicionamos una plataforma en movimiento 2
        block_b = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_b.rect.x = 1470
        block_b.rect.y = 420
        block_b.boundary_left = 1470
        block_b.boundary_right = 1600
        block_b.change_x = 7
        block_b.jugador = self.jugador
        block_b.level = self
        self.platform_list.add(block_b)
 
       # adicionamos una plataforma en movimiento 3
        block_c = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_c.rect.x = 1700
        block_c.rect.y = 110
        block_c.boundary_top = 110
        block_c.boundary_bottom = 380
        block_c.change_y = 1
        block_c.jugador = self.jugador
        block_c.level = self
        self.platform_list.add(block_c)

        # adicionamos una plataforma en movimiento 4
        block_d = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_d.rect.x = 630
        block_d.rect.y = 110
        block_d.boundary_left = 630
        block_d.boundary_right = 780
        block_d.change_x = 3
        block_d.jugador = self.jugador
        block_d.level = self
        self.platform_list.add(block_d)		

################## posicion X 1700

       # adicionamos una plataforma en movimiento 5
        block_c = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_c.rect.x = 3200
        block_c.rect.y = 110
        block_c.boundary_top = 110
        block_c.boundary_bottom = 400
        block_c.change_y = 1
        block_c.jugador = self.jugador
        block_c.level = self
        self.platform_list.add(block_c)	