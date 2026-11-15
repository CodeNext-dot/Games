import pygame
import utilidades.verificar_colisoes as verificar

def atualizar_windows(window: pygame.Surface, player_status, enemy_status, Player, Enemy, resposta=False):
    pygame.display.flip()

    # ativa apenas para mostrar o ataque por 1s
    if resposta == True:
        pygame.time.delay(500)

    window.fill((0, 0, 0))

    # player e inimigo
    pygame.draw.rect(window, player_status.color, Player)
    pygame.draw.rect(window, enemy_status.color, Enemy)

    # portões
    pygame.draw.rect(window, (139, 69, 19), (0, 0, 200, 10))
    pygame.draw.rect(window, (139, 69, 19), (window.get_width() - 200, 0, 200, 10))

    # detecta colisões com o portão
    verificar.verificar_colisao(window, Player)

    pygame.display.flip()