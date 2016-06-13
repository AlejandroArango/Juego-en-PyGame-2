import pygame 

import constantes

from goomba import EnemigoGoomba

import nivel_1
import nivel_2
import nivel_3

import textos_1
import textos_1_boss

import jugador
from jugador import JugadorPrincipal 

import vida
from vida import Vida

from disparo import DisparoJugador

ancho_pantalla  = 900
alto_pantalla = 640
 
def main():
    """ Main del Programa """
    contador = 0	
    variable = 1
    variable1= 1
    variable2= 1	
    puntaje	 = 0
    pygame.init()
 
    # definimos pantalla
    tamano_pantalla = [constantes.ancho_pantalla, constantes.alto_pantalla]
    pantalla = pygame.display.set_mode(tamano_pantalla)

    #Menu principal del juego:
    ########################################################################################

    fondo = pygame.image.load("img/fondo-negro.jpg").convert()
    fondoPausa = pygame.image.load("img/pause.png").convert_alpha()
    fondoAyuda = pygame.image.load("img/fondo-ayuda.jpg").convert()
    fondoCreditos = pygame.image.load("img/fondo-creditos.jpg").convert()
    Titulo = pygame.font.Font("fuentes/Abduction.TTF", 100)
    Opcion = pygame.font.Font("fuentes/Bitsumishi.TTF", 80)

    Pos = 1
    opcion1 = Opcion.render("*  Jugar", True, constantes.color_red)

    titulo = Titulo.render("BIENVENIDO", True, constantes.color_blanco)
    titulo_rect = titulo.get_rect()
    titulo_x = ancho_pantalla/2 - titulo_rect.width/2
    titulo_y = 100

    opcion1 = Opcion.render("*  Jugar", True, constantes.color_blanco)
    opcion1_x = 40
    opcion1_y = 250

    opcion2 = Opcion.render("*  Ayuda", True, constantes.color_blanco)
    opcion2_x = 40
    opcion2_y = 350

    opcion3 = Opcion.render("*  Creditos", True, constantes.color_blanco)
    opcion3_x = 40
    opcion3_y = 450
    terminar = False
    while not terminar:
        if Pos < 1:
            Pos = 3
        if Pos > 3:
            Pos = 1
        opcion1 = Opcion.render("*  Jugar", True, constantes.color_blanco)
        opcion2 = Opcion.render("*  Ayuda", True, constantes.color_blanco)
        opcion3 = Opcion.render("*  Creditos", True, constantes.color_blanco)
        if Pos == 1:
            opcion1 = Opcion.render("*  Jugar", True, constantes.color_red)
        if Pos == 2:
            opcion2 = Opcion.render("*  Ayuda", True, constantes.color_red)
        if Pos == 3:
            opcion3 = Opcion.render("*  Creditos", True, constantes.color_red)

        pantalla.blit(fondo, (0, 0))
        pantalla.blit(titulo, [titulo_x, titulo_y])
        pantalla.blit(opcion1, [opcion1_x, opcion1_y])
        pantalla.blit(opcion2, [opcion2_x, opcion2_y])
        pantalla.blit(opcion3, [opcion3_x, opcion3_y])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                    terminar = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Pos -= 1
                if event.key == pygame.K_DOWN:
                    Pos += 1
                if event.key == pygame.K_SPACE:
                    if Pos == 1:
                        terminar = True
                    if Pos == 2:
                        terminar1 = False
                        while not terminar1:
                            pantalla.blit(fondoAyuda, (0, 0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        terminar1 = True
                                    if event.type == pygame.QUIT: 
                                        terminar1 = True
                    if Pos == 3:
                        terminar2 = False
                        while not terminar2:
                            pantalla.blit(fondoCreditos, (0, 0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_ESCAPE:
                                        terminar2 = True
                                    if event.type == pygame.QUIT: 
                                        terminar2 = True
	
######################################################################################## 
	#fuentes de texto
    fuente_texto   = pygame.font.Font("Bitsumishi.TTF", 18)
    fuente_puntaje = pygame.font.Font("Bitsumishi.TTF", 36)
######################################################################################## 	

    pygame.display.set_caption("Planeswalker")
 
    # creamos jugador
    jugador = JugadorPrincipal()
 
    # creamos niveles uno a uno
    level_list = []
    level_list.append(nivel_1.Nivel_01(jugador))
    level_list.append(nivel_2.Nivel_02(jugador))
    level_list.append(nivel_3.Nivel_03(jugador))
	
    # definimos nivel inicial coloque nivel actual -1
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    lista_sprites_activos = pygame.sprite.Group()
    jugador.level = current_level
 
######################################################################################## 
 
    jugador.rect.x = -550#posicion inicial del jugador
    jugador.rect.y = 0#constantes.alto_pantalla - jugador.rect.height
    lista_sprites_activos.add(jugador)

#########################################################################################
    texto=False
    terminar = False
 
    reloj = pygame.time.Clock()
 
    # -------- ciclo del juego -----------
    while not terminar:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                terminar = True 
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                	#####################La pausa se activa con escape#################
                    terminar4 = False
                    while not terminar4:
                        pantalla.blit(fondoPausa, [370, 280])
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                terminar4 = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    terminar4 = True
                    ####################################################################			
                if current_level_no==0:			
                    if event.key == pygame.K_SPACE:
                        variable += 1
						
                #if current_level_no==0 and current_position <= -2570:		
                    #if event.key == pygame.K_SPACE:
                        #variable1 += 1				
						
                if current_level_no==1:			
                    if event.key == pygame.K_SPACE:
                        variable2 += 1		
						
                if event.key == pygame.K_t:
                    texto = True			
                if event.key == pygame.K_LEFT:
                    jugador.ir_izquierda()
                if event.key == pygame.K_RIGHT:
                    jugador.ir_derecha()
                if event.key == pygame.K_UP:
                    jugador.saltar()
                if event.key == pygame.K_d:
                    pos = jugador.getPosicion()
                    disparo = DisparoJugador(pos[0],pos[1],jugador.getDerecha())
                    disparo.level = current_level
                    disparo.lista_sprites_activos = lista_sprites_activos
                    lista_sprites_activos.add(disparo)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and jugador.change_x < 0:
                    jugador.detenerse()
                if event.key == pygame.K_RIGHT and jugador.change_x > 0:
                    jugador.detenerse()
 
        # actualizar jugador.
        lista_sprites_activos.update()
 
        # Update items in the level
        current_level.update()
 
        # si el jugador esta cerca del lado derecho, cambia el mundo a la izquierdo (-x)
		
        if jugador.rect.right >= 450:           #para mantener en el centro
            diff = jugador.rect.right - 450     #para mantener en el centro
            jugador.rect.right = 450            #para mantener en el centro
            current_level.shift_world(-diff)    #para mantener en el centro
  
        # si el jugador esta cerca del lado izquierdo, cambia el mundo a la derecha (+x)
		
        if jugador.rect.left <= 450:            #para mantener en el centro
            diff = 450 - jugador.rect.left      #para mantener en el centro
            jugador.rect.left = 450             #para mantener en el centro
            current_level.shift_world(diff)     #para mantener en el centro
		
        # pasar de nivel cuando llega al final
        current_position = jugador.rect.x + current_level.world_shift
		
        if current_position < current_level.level_limit:
            jugador.rect.x = 450#120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                jugador.level = current_level	 

				
				
		# encima de esto colocar todo lo referente a enemigos, despues pintamos		
        current_level.draw(pantalla)
        lista_sprites_activos.draw(pantalla)
        print (current_position)		
		
		
		
		
		
		
		
		
		
		
		
################################ P U N T A J E ####################################
		
		#mostrar puntaje jugador
        txt_puntos = fuente_puntaje.render("Puntaje "+ str(puntaje), True, constantes.color_negro)
        pantalla.blit(txt_puntos, [jugador.rect.x-450,2])

################################   S A L U D   ####################################
		
		#mostrar puntaje jugador
        txt_puntos = fuente_puntaje.render("salud "+ str(jugador.salud), True, constantes.color_negro)
        pantalla.blit(txt_puntos, [jugador.rect.x,2])		
		
############################## D I A L O G O S 1 ##################################		
        if current_level_no == 0:
            if texto==False:
                if variable   == 1:	
                    txt_1 = fuente_texto.render(textos_1.locin_1, True, constantes.color_red)
                    pantalla.blit(txt_1, [jugador.rect.x,530])
                elif variable == 2:
                    txt_2 = fuente_texto.render(textos_1.locin_2, True, constantes.color_red)
                    pantalla.blit(txt_2, [jugador.rect.x,530])	
                elif variable == 3:	
                    txt_3 = fuente_texto.render(textos_1.locin_3, True, constantes.color_red)
                    pantalla.blit(txt_3, [jugador.rect.x,530])
                elif variable == 4:
                    txt_4 = fuente_texto.render(textos_1.locin_4, True, constantes.color_red)
                    pantalla.blit(txt_4, [jugador.rect.x,530])
                elif variable == 5:
                    txt_5 = fuente_texto.render(textos_1.locin_5, True, constantes.color_red)
                    pantalla.blit(txt_5, [jugador.rect.x,530])	
                elif variable == 6:	
                    txt_6 = fuente_texto.render(textos_1.locin_6, True, constantes.color_red)
                    pantalla.blit(txt_6, [jugador.rect.x,530])
                elif variable == 7:
                    txt_7 = fuente_texto.render(textos_1.jace_1 , True, constantes.color_azul)
                    pantalla.blit(txt_7, [jugador.rect.x,530])						
                elif variable == 8:
                    txt_8 = fuente_texto.render(textos_1.jace_2,  True, constantes.color_azul)
                    pantalla.blit(txt_8, [jugador.rect.x,530])	
                elif variable == 9:	
                    txt_9 = fuente_texto.render(textos_1.locin_7, True, constantes.color_red)
                    pantalla.blit(txt_9, [jugador.rect.x,530])
                elif variable == 10:
                    txt_10 = fuente_texto.render(textos_1.locin_8, True, constantes.color_red)
                    pantalla.blit(txt_10, [jugador.rect.x,530])
                elif variable == 11:
                    txt_11 = fuente_texto.render(textos_1.locin_9, True, constantes.color_red)
                    pantalla.blit(txt_11, [jugador.rect.x,530])	
                elif variable == 12:	
                    txt_12= fuente_texto.render(textos_1.locin_10, True, constantes.color_red)
                    pantalla.blit(txt_12, [jugador.rect.x,530])
                elif variable == 13:
                    txt_13 = fuente_texto.render(textos_1.locin_11 , True, constantes.color_red)
                    pantalla.blit(txt_13, [jugador.rect.x,530])		
                elif variable == 14:
                    txt_14 = fuente_texto.render(textos_1.locin_12, True, constantes.color_red)
                    pantalla.blit(txt_14, [jugador.rect.x,530])
                elif variable == 15:
                    txt_15 = fuente_texto.render(textos_1.locin_13, True, constantes.color_red)
                    pantalla.blit(txt_15, [jugador.rect.x,530])	
                elif variable == 16:	
                    txt_16= fuente_texto.render(textos_1.locin_14, True, constantes.color_red)
                    pantalla.blit(txt_16, [jugador.rect.x,530])
                elif variable == 17:
                    txt_17 = fuente_texto.render(textos_1.locin_15 , True, constantes.color_red)
                    pantalla.blit(txt_17, [jugador.rect.x,530])					
                elif variable == 18:
                    txt_18 = fuente_texto.render(textos_1.jace_3 , True, constantes.color_azul)
                    pantalla.blit(txt_18, [jugador.rect.x,530])	
                elif variable == 19:	
                    txt_19= fuente_texto.render(textos_1.locin_16, True, constantes.color_red)
                    pantalla.blit(txt_19, [jugador.rect.x,530])
                elif variable == 20:
                    txt_20 = fuente_texto.render(textos_1.locin_17 , True, constantes.color_red)
                    pantalla.blit(txt_20, [jugador.rect.x,530])		
                elif variable ==21:
                    txt_21 = fuente_texto.render(textos_1.locin_18, True, constantes.color_red)
                    pantalla.blit(txt_21, [jugador.rect.x,530])
                elif variable == 22:
                    txt_22 = fuente_texto.render(textos_1.locin_19, True, constantes.color_red)
                    pantalla.blit(txt_22, [jugador.rect.x,530])	
                elif variable == 23:	
                    txt_23= fuente_texto.render(textos_1.locin_20, True, constantes.color_red)
                    pantalla.blit(txt_23, [jugador.rect.x,530])
                elif variable == 24:
                    txt_24 = fuente_texto.render(textos_1.locin_21 , True, constantes.color_red)
                    pantalla.blit(txt_24, [jugador.rect.x,530])					
                elif variable == 25:
                    txt_25 = fuente_texto.render(textos_1.jace_4 , True, constantes.color_azul)
                    pantalla.blit(txt_25, [jugador.rect.x,530])
					
############################## D I A L O G O S 2 ##################################	
        if current_level_no == 0 and current_position <= -2570:
            if texto==False:
                if variable1   == 1:	
                    txt_1 = fuente_texto.render(textos_1_boss.locin_1, True, constantes.color_red)
                    pantalla.blit(txt_1, [jugador.rect.x,530])
                elif variable1 == 2:
                    txt_2 = fuente_texto.render(textos_1_boss.locin_2, True, constantes.color_red)
                    pantalla.blit(txt_2, [jugador.rect.x,530])	
                elif variable1 == 3:	
                    txt_3 = fuente_texto.render(textos_1_boss.locin_3, True, constantes.color_red)
                    pantalla.blit(txt_3, [jugador.rect.x,530])
                elif variable1 == 4:
                    txt_4 = fuente_texto.render(textos_1_boss.jace_4, True, constantes.color_azul)
                    pantalla.blit(txt_4, [jugador.rect.x,530])
                elif variable1 == 5:
                    txt_5 = fuente_texto.render(textos_1_boss.jace_5, True, constantes.color_azul)
                    pantalla.blit(txt_5, [jugador.rect.x,530])	
                elif variable1 == 6:	
                    txt_6 = fuente_texto.render(textos_1_boss.locin_6, True, constantes.color_red)
                    pantalla.blit(txt_6, [jugador.rect.x,530])
                elif variable1 == 7:
                    txt_7 = fuente_texto.render(textos_1_boss.locin_7 , True, constantes.color_red)
                    pantalla.blit(txt_7, [jugador.rect.x,530])						
                elif variable1 == 8:
                    txt_8 = fuente_texto.render(textos_1_boss.jace_8,  True, constantes.color_azul)
                    pantalla.blit(txt_8, [jugador.rect.x,530])	
####################################################################################
        puntaje += 1		
        reloj.tick(60)
        pygame.display.flip()

    pygame.quit()
 
if __name__ == "__main__":
    main()
