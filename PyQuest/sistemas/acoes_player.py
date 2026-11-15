import pygame
import utilidades.verificar_colisoes as verificar

def receber_resposta(resposta, player, window: pygame.Surface):
    # receber_inimigo() ativa as ações do inimigo

    if(resposta == 'w'):
        player.move_ip(0, -50)
    elif((resposta == 'd') and (window.get_width() - 50 > player.x)):
        player.move_ip(50, 0)
    elif((resposta == 'a') and (0 < player.x)):
        player.move_ip(-50, 0)
    elif((resposta == 's') and (window.get_height() - 50 > player.y)):
        player.move_ip(0, 50)
    elif(('e' in resposta) or ('q' in resposta)):
        if('w' in resposta):
            acao_temp = [20, -25]
        elif('d' in resposta):
            acao_temp = [75, 20]
        elif('a' in resposta):
            acao_temp = [-25, 20]
        elif('s' in resposta):
            acao_temp = [20, 74]
        else:
            acao_temp = [20, -25]

        player_acao = pygame.Rect(player.x + acao_temp[0], player.y + acao_temp[1], 10, 10)

        if('e' in resposta):
            pygame.draw.rect(window, (255, 255, 150), player_acao)
        else:
            pygame.draw.rect(window, (255, 120, 120), player_acao)
            # verificar.verificar_colisao(window, player_acao, enemy)