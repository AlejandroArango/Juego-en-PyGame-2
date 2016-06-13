import pygame 
import constantes
import plataformas
import clase_nivel
from clase_nivel import Nivel

# creamos nivel 3
class Nivel_03(Nivel):
    """ nivel 3 """
    def remove(self, block):
      self.platform_list.remove(block)
      
    def __init__(self, jugador):
        """ crear nivel 3. """
 
        # padre constructor
        Nivel.__init__(self, jugador)
 
        self.background = pygame.image.load("img/desierto.jpg").convert_alpha()
        self.background.set_colorkey(constantes.color_negro)
        self.level_limit = -9000
		
		#vector con los diferentes tipos de plataformas con sus respectivas posiciones X y Y para ubicarlas
        level = [ 
                  [plataformas.bloque_desierto,   -700, 530],
				  [plataformas.bloque_desierto,   -700, 460],
                  [plataformas.bloque_desierto,   -700, 390],		
                  [plataformas.bloque_desierto,   -700, 320],
                  [plataformas.bloque_desierto,   -700, 250],				  
                  [plataformas.bloque_desierto,   -700, 180],		
				  [plataformas.bloque_desierto,   -700, 110],
                  [plataformas.bloque_desierto,   -700,  40],
                  [plataformas.bloque_desierto,   -700, -30],

                  [plataformas.desierto_centro,        -630, 290],
                  [plataformas.desierto_der_curva_a,   -560, 290],		
				  
                  [plataformas.desierto_izq_curva_a,   -490, 410],
                  [plataformas.desierto_der_curva_a,   -420, 410],	

                  [plataformas.desierto_izq_curva_a,   -350, 530],
                  [plataformas.desierto_der_curva_a,   -280, 530],	

				  [plataformas.desierto_izq_plano_a,    0, 500],
                  [plataformas.desierto_cen_plano_a,   70, 500],
                  [plataformas.desierto_cen_plano_a,  140, 500],
                  [plataformas.desierto_cen_plano_a,  210, 500],
                  [plataformas.desierto_cen_plano_a,  280, 500],
                  [plataformas.desierto_cen_plano_a,  350, 500],				  
                  [plataformas.desierto_der_plano_a,  420, 500],
		
                  [plataformas.bloque_desierto,   620, 430],
                  [plataformas.bloque_desierto,   620, 360],
                  [plataformas.bloque_desierto,   620, 290],
                  [plataformas.bloque_desierto,   620, 220],
                  [plataformas.bloque_desierto,   620, 150],
                  [plataformas.bloque_desierto,   620,  80],
                  [plataformas.bloque_desierto,   620,  10],
                  [plataformas.bloque_desierto,   620, -60],				  
				  
                  [plataformas.desierto_cen_plano_a,  690, 460],
                  [plataformas.desierto_cen_plano_a,  760, 460],
                  [plataformas.desierto_cen_plano_a,  830, 460],
                  [plataformas.desierto_cen_plano_a,  900, 460],
                  [plataformas.desierto_cen_plano_a,  970, 460],				  
                  [plataformas.desierto_cen_plano_a, 1040, 460],			
                  [plataformas.desierto_der_plano_a, 1110, 460],

                  [plataformas.desierto_izq_plano_a,  790, 320],
                  [plataformas.desierto_cen_plano_a,  860, 320],
                  [plataformas.desierto_cen_plano_a,  930, 320],
                  [plataformas.desierto_cen_plano_a, 1000, 320],
                  [plataformas.desierto_cen_plano_a, 1070, 320],				  
                  [plataformas.desierto_cen_plano_a, 1140, 320],			
                  [plataformas.desierto_cen_plano_a, 1210, 320],				  
				  
                  [plataformas.desierto_cen_plano_a,  690, 180],
                  [plataformas.desierto_cen_plano_a,  760, 180],
                  [plataformas.desierto_cen_plano_a,  830, 180],
                  [plataformas.desierto_cen_plano_a,  900, 180],
                  [plataformas.desierto_cen_plano_a,  970, 180],				  
                  [plataformas.desierto_cen_plano_a, 1040, 180],			
                  [plataformas.desierto_der_plano_a, 1110, 180],	 

				  [plataformas.desierto_esqui_izq,   1250, 560],
				  [plataformas.desierto_esqui_der,    690, 420],
				  [plataformas.desierto_esqui_izq,   1250, 280],
				  
				  
                  [plataformas.bloque_desierto,  1280, 530],		
                  [plataformas.bloque_desierto,  1280, 460],
                  [plataformas.bloque_desierto,  1280, 390],
                  [plataformas.bloque_desierto,  1280, 320],
                  [plataformas.bloque_desierto,  1280, 250],
                  [plataformas.bloque_desierto,  1280, 180],				  
                  [plataformas.bloque_desierto,  1280, 110],
                  [plataformas.bloque_desierto_arriba,  1280, 70],			

				  [plataformas.desierto_izq_plano_a, 1800, 500],
                  [plataformas.desierto_cen_plano_a, 1870, 500],
                  [plataformas.desierto_cen_plano_a, 1940, 500],
                  [plataformas.desierto_cen_plano_a, 2010, 500],
                  [plataformas.desierto_cen_plano_a, 2080, 500],
                  [plataformas.desierto_cen_plano_a, 2150, 500],				  
                  [plataformas.desierto_der_plano_a, 2220, 500],

#############################posicion X 3500 piensa rapido
				  
                  [plataformas.bloque_desierto,  3500, 390],
                  [plataformas.bloque_desierto,  3500, 320],
                  [plataformas.bloque_desierto,  3500, 250],
                  [plataformas.bloque_desierto,  3500, 180],				  
                  [plataformas.bloque_desierto,  3500, 110],
                  [plataformas.bloque_desierto_arriba,  3500, 70],	

                  [plataformas.bloque_desierto,  3800, 460],
                  [plataformas.bloque_desierto,  3800, 390],
                  [plataformas.bloque_desierto,  3800, 320],
                  [plataformas.bloque_desierto,  3800, 250],
                  [plataformas.bloque_desierto,  3800, 180],				  
                  [plataformas.bloque_desierto,  3800, 110],
                  [plataformas.bloque_desierto_arriba,  3800, 70],		

				  [plataformas.desierto_esqui_izq,   3770, 490],
				  [plataformas.desierto_esqui_der,   3570, 390],		
				  [plataformas.desierto_esqui_izq,   3770, 290],
				  [plataformas.desierto_esqui_der,   3570, 190],	  
				  
#############################posicion X 2300 sube y baja extremo
				  
                  ]
				  
				  
############################## S U E L O ###################################
        pos_y = 600
        pos_x = -700
        while pos_x < 5000:
        #if pos_x <= 3990:
			# adicionamos suelo
            suelod = plataformas.MovimientoPlataforma(plataformas.suelo_desierto)
            suelod.rect.x = pos_x
            suelod.rect.y = pos_y
            pos_x += 70
            suelod.jugador = self.jugador
            suelod.level = self
            self.platform_list.add(suelod)
        print ("H O L A ! ! ! ")
		
############################################################################

        # anadimos plataformas que se encuentran en level
        for platform in level:
            block = plataformas.Plataforma(platform[0])#imagen x y
            block.rect.x = platform[1]				   #ancho
            block.rect.y = platform[2]				   #alto
            block.jugador = self.jugador
            self.platform_list.add(block)			

#######################################################posicionX 1400
		
        # adicionamos una plataforma en movimiento 1
        block_desierto_a = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_a.rect.x = 1400
        block_desierto_a.rect.y = 500
        block_desierto_a.boundary_left = 1400
        block_desierto_a.boundary_right = 1700
        block_desierto_a.change_x = 3
        block_desierto_a.jugador = self.jugador
        block_desierto_a.level = self
        self.platform_list.add(block_desierto_a)	
		
#######################################################posicionX 2300

        # adicionamos una plataforma en movimiento 2
        block_desierto_b = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_b.rect.x = 3170
        block_desierto_b.rect.y = 430
        block_desierto_b.boundary_left = 2300
        block_desierto_b.boundary_right = 3170
        block_desierto_b.change_x = 4
        block_desierto_b.jugador = self.jugador
        block_desierto_b.level = self
        self.platform_list.add(block_desierto_b)
		
        # adicionamos una plataforma en movimiento 3
        block_desierto_c = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_c.rect.x = 3170
        block_desierto_c.rect.y = 300
        block_desierto_c.boundary_left = 2300
        block_desierto_c.boundary_right = 3170
        block_desierto_c.change_x = 2
        block_desierto_c.jugador = self.jugador
        block_desierto_c.level = self
        self.platform_list.add(block_desierto_c)
		
		
        # adicionamos una plataforma en movimiento 4
        block_desierto_d = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_d.rect.x = 3170
        block_desierto_d.rect.y = 130
        block_desierto_d.boundary_left = 2300
        block_desierto_d.boundary_right = 3170
        block_desierto_d.change_x = 3
        block_desierto_d.jugador = self.jugador
        block_desierto_d.level = self
        self.platform_list.add(block_desierto_d)		
		
#######################################################posicionX 2300

       # adicionamos una plataforma en movimiento 1
        block_desierto_e = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_e.rect.x = 2300
        block_desierto_e.rect.y = 110
        block_desierto_e.boundary_top = 110
        block_desierto_e.boundary_bottom = 500
        block_desierto_e.change_y = 1
        block_desierto_e.jugador = self.jugador
        block_desierto_e.level = self
        self.platform_list.add(block_desierto_e)
		
       # adicionamos una plataforma en movimiento 2
        block_desierto_f = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_f.rect.x = 2500
        block_desierto_f.rect.y = 110
        block_desierto_f.boundary_top = 110
        block_desierto_f.boundary_bottom = 500
        block_desierto_f.change_y = 2
        block_desierto_f.jugador = self.jugador
        block_desierto_f.level = self
        self.platform_list.add(block_desierto_f)

       # adicionamos una plataforma en movimiento 3
        block_desierto_g = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_g.rect.x = 2700
        block_desierto_g.rect.y = 110
        block_desierto_g.boundary_top = 110
        block_desierto_g.boundary_bottom = 500
        block_desierto_g.change_y = 1
        block_desierto_g.jugador = self.jugador
        block_desierto_g.level = self
        self.platform_list.add(block_desierto_g)

       # adicionamos una plataforma en movimiento 4
        block_desierto_h = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_h.rect.x = 2900
        block_desierto_h.rect.y = 110
        block_desierto_h.boundary_top = 110
        block_desierto_h.boundary_bottom = 500
        block_desierto_h.change_y = 4
        block_desierto_h.jugador = self.jugador
        block_desierto_h.level = self
        self.platform_list.add(block_desierto_h)

       # adicionamos una plataforma en movimiento 5
        block_desierto_i = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_i.rect.x = 3100
        block_desierto_i.rect.y = 110
        block_desierto_i.boundary_top = 110
        block_desierto_i.boundary_bottom = 500
        block_desierto_i.change_y = 3
        block_desierto_i.jugador = self.jugador
        block_desierto_i.level = self
        self.platform_list.add(block_desierto_i)		

#######################################################posicionX 3300

        # adicionamos una plataforma en movimiento 4
        block_desierto_j = plataformas.MovimientoPlataforma(plataformas.desierto_plataforma)
        block_desierto_j.rect.x = 3250
        block_desierto_j.rect.y = 540
        block_desierto_j.boundary_left = 3250
        block_desierto_j.boundary_right = 4000
        block_desierto_j.change_x = 1
        block_desierto_j.jugador = self.jugador
        block_desierto_j.level = self
        self.platform_list.add(block_desierto_j)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = -630
        goomba.rect.y = 240
        goomba.boundary_left = -630
        goomba.boundary_right = -560
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = -490
        goomba.rect.y = 360
        goomba.boundary_left = -490
        goomba.boundary_right = -420
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = -350
        goomba.rect.y = 480
        goomba.boundary_left = -350
        goomba.boundary_right = -280
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 0
        goomba.rect.y = 450
        goomba.boundary_left = 0
        goomba.boundary_right = 500
        goomba.change_x = 5
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 690
        goomba.rect.y = 410
        goomba.boundary_left = 690
        goomba.boundary_right = 1110
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 790
        goomba.rect.y = 270
        goomba.boundary_left = 790
        goomba.boundary_right = 1210
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 690
        goomba.rect.y = 130
        goomba.boundary_left = 690
        goomba.boundary_right = 1110
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

        # adicionamos una plataforma en movimiento 1
        goomba = plataformas.MovimientoPlataforma(plataformas.goomba1)
        goomba.rect.x = 1800
        goomba.rect.y = 450
        goomba.boundary_left = 1800
        goomba.boundary_right = 2220
        goomba.change_x = 3
        goomba.jugador = self.jugador
        goomba.level = self        #anadimos a level la imagen
        self.platform_list.add(goomba)

		