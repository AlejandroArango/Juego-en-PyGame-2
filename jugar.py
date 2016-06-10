import pygame 
 
import constantes
import niveles
 
from jugador import JugadorPrincipal
from disparo import DisparoJugador
 
def main():
    """ Main del Programa """
    #efecto lluvia
    contador=0	
    pygame.init()
 
    # definimos pantalla
    tamano_pantalla = [constantes.ancho_pantalla, constantes.alto_pantalla]
    pantalla = pygame.display.set_mode(tamano_pantalla)
 
    pygame.display.set_caption("Planeswalker")
 
    # creamos jugador
    jugador = JugadorPrincipal()
 
    # creamos niveles
    level_list = []
    level_list.append(niveles.Nivel_01(jugador))
    level_list.append(niveles.Nivel_02(jugador))
 
    # definimos nivel inicial
    current_level_no = 1
    current_level = level_list[current_level_no]
 
    lista_sprites_activos = pygame.sprite.Group()
    jugador.level = current_level
 
######################################################################################## 
 
    jugador.rect.x = 100#posicion inicial del jugador
    jugador.rect.y = 0#constantes.alto_pantalla - jugador.rect.height
    lista_sprites_activos.add(jugador)
	
#########################################################################################
#efecto de lluvia
#Gameover = pygame.image.load('img/inicio.png').convert_alpha()

    nivel1 = pygame.image.load('img/espacio_efecto.png').convert_alpha()

    def ini_polvo(contador,efecto):
        pantalla.blit(efecto,(3400,-640+(contador%40*15)))
        pantalla.blit(efecto,(3400,contador%40*15))

#########################################################################################	
	
    terminar = False
 
    reloj = pygame.time.Clock()
 
    # -------- ciclo del juego -----------
    while not terminar:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                terminar = True 
 
            if event.type == pygame.KEYDOWN:
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
			
        ini_polvo(contador,nivel1)    
        contador+=1
		
        # pasar de nivel cuando llega al final
        current_position = jugador.rect.x + current_level.world_shift
		
        if current_position < current_level.level_limit:
            jugador.rect.x = 450#120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                jugador.level = current_level
 
        current_level.draw(pantalla)
        lista_sprites_activos.draw(pantalla)
 
        reloj.tick(60)
 
        pygame.display.flip()

    pygame.quit()
 
if __name__ == "__main__":
    main()
