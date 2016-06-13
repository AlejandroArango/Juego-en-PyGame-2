import pygame 
import constantes
import plataformas
import clase_nivel
from clase_nivel import Nivel

# creamos los niveles, clase por nivel
class Nivel_01(Nivel):
    """ nivel 1. """
    def remove(self, block):
      self.platform_list.remove(block)

    def __init__(self, jugador):
        """ crear nivel 1 1. """

        # llamamos al padre constructor
        Nivel.__init__(self, jugador)
 
        self.background = pygame.image.load("img/prueba.png").convert_alpha()
        self.background.set_colorkey(constantes.color_blanco)
        self.level_limit = -4000 #limite del nivel
		

		
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
                  [plataformas.suelo_laba,   2210, 569],
                  [plataformas.suelo_laba,   2262, 569],
                  [plataformas.suelo_laba,   2314, 569],
                  [plataformas.suelo_laba,   2366, 569],
                  [plataformas.suelo_laba,   2418, 569],			  
                  [plataformas.suelo_laba,   2470, 569],
                  [plataformas.suelo_laba,   2522, 569],
                  [plataformas.suelo_laba,   2574, 569],
                  [plataformas.suelo_laba,   2626, 569],
                  [plataformas.suelo_laba,   2678, 569],
                  [plataformas.suelo_laba,   2730, 569],
                  [plataformas.suelo_laba,   2782, 569],
                  ]
				  			  

############################## S U E L O ###################################
        pos_y = 600
        pos_x = -700
        while pos_x < 5400:
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
 
        # anadimos plataformas que se encuentran en level
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
        block.level = self				#anadimos a level la imagen
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
        block_e = plataformas.MovimientoPlataforma(plataformas.inicio_plat_mov)
        block_e.rect.x = 3200
        block_e.rect.y = 110
        block_e.boundary_top = 110
        block_e.boundary_bottom = 400
        block_e.change_y = 1
        block_e.jugador = self.jugador
        block_e.level = self
        self.platform_list.add(block_e)


        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 500
        goomba.rect.y = 480
        goomba.boundary_left = 500
        goomba.boundary_right = 640
        goomba.change_x = 4
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 810
        goomba.rect.y = 370
        goomba.boundary_left = 810
        goomba.boundary_right = 950
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 1460
        goomba.rect.y = 60
        goomba.boundary_left = 1460
        goomba.boundary_right = 1530
        goomba.change_x = 2
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 1160
        goomba.rect.y = 60
        goomba.boundary_left = 1160
        goomba.boundary_right = 1300
        goomba.change_x = 2
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)


        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 930
        goomba.rect.y = 60
        goomba.boundary_left = 930
        goomba.boundary_right = 1000
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 220
        goomba.rect.y = 110
        goomba.boundary_left = 220
        goomba.boundary_right = 360
        goomba.change_x = 4
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 2000
        goomba.rect.y = 480
        goomba.boundary_left = 2000
        goomba.boundary_right = 2140
        goomba.change_x = 1
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 2790
        goomba.rect.y = 480
        goomba.boundary_left = 2790
        goomba.boundary_right = 2930
        goomba.change_x = 5
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 2395
        goomba.rect.y = 380
        goomba.boundary_left = 2395
        goomba.boundary_right = 2535
        goomba.change_x = 4
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 2000
        goomba.rect.y = 280
        goomba.boundary_left = 2000
        goomba.boundary_right = 2140
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 2790
        goomba.rect.y = 280
        goomba.boundary_left = 2790
        goomba.boundary_right = 2930
        goomba.change_x = 4
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 2395
        goomba.rect.y = 180
        goomba.boundary_left = 2395
        goomba.boundary_right = 2535
        goomba.change_x = 6
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        
        
