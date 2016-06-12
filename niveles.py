import pygame 
import constantes
import plataformas
import clase_nivel
from clase_nivel import Nivel


# creamos los niveles, clase por nivel
class Nivel_01(Nivel):
    """ nivel 1. """
 
    def __init__(self, jugador):
        """ crear nivel 1 1. """

        # llamamos al padre constructor
        Nivel.__init__(self, jugador)
 
        self.background = pygame.image.load("img/prueba.png").convert_alpha()
        self.background.set_colorkey(constantes.color_blanco)
        self.level_limit = -9000 #limite del nivel
		

		
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
				  			  
'''
############################## S U E L O ###################################
        pos_y = 600
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
        print ("H O L A ! ! ! ")		
############################################################################			
 
        # añadimos plataformas que se encuentran en level
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
        self.platform_list.add(block_c)	'''




	
# creamos nivel 2
class Nivel_02(Nivel):
    """ nivel 2. """
 
    def __init__(self, jugador):
        """ crear nivel 2. """
 
        # padre constructor
        Nivel.__init__(self, jugador)
 
        self.background = pygame.image.load("img/background_02.png").convert_alpha()
        #self.background.set_colorkey(constantes.color_negro)
        self.level_limit = -9000
 
		#vector con los diferentes tipos de plataformas con sus respectivas posiciones X y Y para ubicarlas
        level = [ 
                  [plataformas.bloque_bosque_a,   -700, 530],
				  [plataformas.bloque_bosque_a,   -700, 460],
                  [plataformas.bloque_bosque_a,   -700, 390],		
                  [plataformas.bloque_bosque_a,   -700, 320],
                  [plataformas.bloque_bosque_a,   -700, 250],				  
                  [plataformas.bloque_bosque_a,   -700, 180],		
				  [plataformas.bloque_bosque_c,   -700, 150],
                  [plataformas.bloque_bosque_b,   -700, 110],		
		
		
#############################posicion X 0 Zona de lava	
				  [plataformas.bosque_izquierdo, 500, 530],
                  [plataformas.bosque_centro,    570, 530],
                  [plataformas.bosque_derecho,   640, 530],
				  
                  [plataformas.bosque_izq_b,     810, 410],
                  [plataformas.bosque_der_b,     880, 410],
				  
                  [plataformas.bosque_plat_mov, 1870, 410],
		  			  
                  [plataformas.bosque_plat_mov, 1940, 450],

                  [plataformas.bosque_plat_mov, 2010, 490],
			  				  
				  #[plataformas.bosque_izquierdo,2080, 530],se comentan para caminar de seguido y mirar el diseno
                  #[plataformas.bosque_centro,   2150, 530],
                  #[plataformas.bosque_derecho,  2220, 530],
				  
#############################posicion X 2500 Zona gemela

                  [plataformas.bosque_izq_b,    2500, 410],
                  [plataformas.bosque_cen_b,    2570, 410],				  
                  [plataformas.bosque_cen_b,    2640, 410],
                  [plataformas.bosque_cen_b,    2710, 410],
                  [plataformas.bosque_cen_b,    2780, 410],
                  [plataformas.bosque_cen_b,    2850, 410],
                  [plataformas.bosque_cen_b,    2920, 410],				  
                  [plataformas.bosque_der_b,    2990, 410],
				  
				  [plataformas.bosque_izq_b,    3300, 410],
                  [plataformas.bosque_cen_b,    3370, 410],				  
                  [plataformas.bosque_cen_b,    3440, 410],
                  [plataformas.bosque_cen_b,    3510, 410],
                  [plataformas.bosque_cen_b,    3580, 410],
                  [plataformas.bosque_cen_b,    3650, 410],
                  [plataformas.bosque_cen_b,    3720, 410],				  
                  [plataformas.bosque_der_b,    3790, 410],

#############################posicion X 4000 Zona de lava 2	

				  [plataformas.bosque_izquierdo, 4200, 530],
                  [plataformas.bosque_centro,    4270, 530],
                  [plataformas.bosque_derecho,   4340, 530],
				  
                  [plataformas.bosque_izq_b,     4440, 410],
                  [plataformas.bosque_der_b,     4510, 410],
				  
                  [plataformas.bosque_plat_mov, 5600, 410],
		  			  
                  [plataformas.bosque_plat_mov, 5670, 450],

                  [plataformas.bosque_plat_mov, 5740, 490],
			  				  
				  #[plataformas.bosque_izquierdo,5810, 530],
                  #[plataformas.bosque_centro,   5880, 530],
                  #[plataformas.bosque_derecho,  5950, 530],
				  
#############################posicion X 6200 Zona gemela 2

                  [plataformas.bosque_izq_b,    6200, 410],
                  [plataformas.bosque_cen_b,    6270, 410],				  
                  [plataformas.bosque_cen_b,    6340, 410],
                  [plataformas.bosque_cen_b,    6410, 410],
                  [plataformas.bosque_cen_b,    6480, 410],
                  [plataformas.bosque_cen_b,    6550, 410],
                  [plataformas.bosque_cen_b,    6620, 410],				  
                  [plataformas.bosque_der_b,    6690, 410],
				  
				  [plataformas.bosque_izq_b,    7000, 410],
                  [plataformas.bosque_cen_b,    7070, 410],
                  [plataformas.bosque_cen_b,    7140, 410],
                  [plataformas.bosque_cen_b,    7210, 410],
                  [plataformas.bosque_cen_b,    7280, 410],
                  [plataformas.bosque_cen_b,    7350, 410],
                  [plataformas.bosque_cen_b,    7420, 410],
                  [plataformas.bosque_der_b,    7490, 410],

                  [plataformas.bloque_bosque_a,   7900, 530],
				  [plataformas.bloque_bosque_a,   7900, 460],
                  [plataformas.bloque_bosque_a,   7900, 390],		
                  [plataformas.bloque_bosque_a,   7900, 320],
                  [plataformas.bloque_bosque_a,   7900, 250],				  
                  [plataformas.bloque_bosque_a,   7900, 180],		
				  [plataformas.bloque_bosque_c,   7900, 150],
                  [plataformas.bloque_bosque_b,   7900, 110],		  
                  ]
 
 
############################## S U E L O ###################################
        '''pos_y = 600
        pos_x = -700
        while pos_x < 8050:
        #if pos_x <= 3990:
			# adicionamos suelo
            suelob = plataformas.MovimientoPlataforma(plataformas.suelo_bosque)
            suelob.rect.x = pos_x
            suelob.rect.y = pos_y
            pos_x += 70
            suelob.jugador = self.jugador
            suelob.level = self
            self.platform_list.add(suelob)
        print ("H O L A ! ! ! ")'''
		
############################################################################			
 
        # añadimos plataformas que se encuentran en level
        for platform in level:
            block = plataformas.Plataforma(platform[0])#imagen x y
            block.rect.x = platform[1]				   #ancho
            block.rect.y = platform[2]				   #alto
            block.jugador = self.jugador
            self.platform_list.add(block)			

######################################################################################			
			
       # adicionamos una plataforma en movimiento 1
        '''block_bosque_a = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_a.rect.x = 1100
        block_bosque_a.rect.y = 110
        block_bosque_a.boundary_top = 110
        block_bosque_a.boundary_bottom = 440
        block_bosque_a.change_y = 1
        block_bosque_a.jugador = self.jugador
        block_bosque_a.level = self
        self.platform_list.add(block_bosque_a)
		
       # adicionamos una plataforma en movimiento 2
        block_bosque_b = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_b.rect.x = 1300
        block_bosque_b.rect.y = 110
        block_bosque_b.boundary_top = 110
        block_bosque_b.boundary_bottom = 440
        block_bosque_b.change_y = 2
        block_bosque_b.jugador = self.jugador
        block_bosque_b.level = self
        self.platform_list.add(block_bosque_b)

       # adicionamos una plataforma en movimiento 3
        block_bosque_c = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_c.rect.x = 1500
        block_bosque_c.rect.y = 110
        block_bosque_c.boundary_top = 110
        block_bosque_c.boundary_bottom = 440
        block_bosque_c.change_y = 3
        block_bosque_c.jugador = self.jugador
        block_bosque_c.level = self
        self.platform_list.add(block_bosque_c)

       # adicionamos una plataforma en movimiento 4
        block_bosque_d = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_d.rect.x = 1700
        block_bosque_d.rect.y = 110
        block_bosque_d.boundary_top = 110
        block_bosque_d.boundary_bottom = 440
        block_bosque_d.change_y = 4
        block_bosque_d.jugador = self.jugador
        block_bosque_d.level = self
        self.platform_list.add(block_bosque_d)		

######################################################################################		

       # adicionamos una plataforma en movimiento 5
        block_bosque_e = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_e.rect.x = 4730
        block_bosque_e.rect.y = 110
        block_bosque_e.boundary_top = 110
        block_bosque_e.boundary_bottom = 440
        block_bosque_e.change_y = 1
        block_bosque_e.jugador = self.jugador
        block_bosque_e.level = self
        self.platform_list.add(block_bosque_e)
		
       # adicionamos una plataforma en movimiento 6
        block_bosque_f = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_f.rect.x = 4930
        block_bosque_f.rect.y = 110
        block_bosque_f.boundary_top = 110
        block_bosque_f.boundary_bottom = 440
        block_bosque_f.change_y = 3
        block_bosque_f.jugador = self.jugador
        block_bosque_f.level = self
        self.platform_list.add(block_bosque_f)

       # adicionamos una plataforma en movimiento 7
        block_bosque_g = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_g.rect.x = 5130
        block_bosque_g.rect.y = 110
        block_bosque_g.boundary_top = 110
        block_bosque_g.boundary_bottom = 440
        block_bosque_g.change_y = 4
        block_bosque_g.jugador = self.jugador
        block_bosque_g.level = self
        self.platform_list.add(block_bosque_g)

       # adicionamos una plataforma en movimiento 8
        block_bosque_h = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_h.rect.x = 5330
        block_bosque_h.rect.y = 110
        block_bosque_h.boundary_top = 110
        block_bosque_h.boundary_bottom = 440
        block_bosque_h.change_y = 3
        block_bosque_h.jugador = self.jugador
        block_bosque_h.level = self
        self.platform_list.add(block_bosque_h)	

       # adicionamos una plataforma en movimiento 9
        block_bosque_i = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_i.rect.x = 5530
        block_bosque_i.rect.y = 110
        block_bosque_i.boundary_top = 110
        block_bosque_i.boundary_bottom = 440
        block_bosque_i.change_y = 2
        block_bosque_i.jugador = self.jugador
        block_bosque_i.level = self
        self.platform_list.add(block_bosque_i)	'''

       # adicionamos una plataforma en movimiento 9
        block_bosque_j = plataformas.MovimientoPlataforma(plataformas.bosque_plat_mov)
        block_bosque_j.rect.x = 7700
        block_bosque_j.rect.y = 110
        block_bosque_j.boundary_top = 110
        block_bosque_j.boundary_bottom = 600
        block_bosque_j.change_y = 1
        block_bosque_j.jugador = self.jugador
        block_bosque_j.level = self
        self.platform_list.add(block_bosque_j)		