import pygame
 
import constantes
import niveles
 
from jugador import JugadorPrincipal
 
def main():
    """ Main del Programa """
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
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    lista_sprites_activos = pygame.sprite.Group()
    jugador.level = current_level
 
    jugador.rect.x = 340
    jugador.rect.y = constantes.alto_pantalla - jugador.rect.height
    lista_sprites_activos.add(jugador)
 
    #
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
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and jugador.change_x < 0:
                    jugador.detenerse()
                if event.key == pygame.K_RIGHT and jugador.change_x > 0:
                    jugador.detenerse()
 
        # actualizar jugador.
        lista_sprites_activos.update()
 
 #esto no lo entendi
 
        # Update items in the level
        current_level.update()
 
        # If the jugador gets near the right side, shift the world left (-x)
        if jugador.rect.right >= 500:
            diff = jugador.rect.right - 500
            jugador.rect.right = 500
            current_level.shift_world(-diff)
  
        # If the jugador gets near the left side, shift the world right (+x)
        if jugador.rect.left <= 120:
            diff = 120 - jugador.rect.left
            jugador.rect.left = 120
            current_level.shift_world(diff)
 
        # pasar de nivel cuando llega al final
        current_position = jugador.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            jugador.rect.x = 120
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