def receber_inimigo():
    if((enemy_itens["tempo"] % 4) == 0):
        if (player.x - enemy.x) > (player.y - enemy.y):
            if player.x >= enemy.x:  # direita
                enemy_acao_temp = [75, 20]
            else:  # esquerda
                enemy_acao_temp = [-25, 20]

        else:
            if player.y >= enemy.y:  # baixo
                enemy_acao_temp = [20, 75]
            else:  # cima
                enemy_acao_temp = [20, -25]

        enemy_acao = pygame.Rect(enemy.x + enemy_acao_temp[0], enemy.y + enemy_acao_temp[1], 10, 10)
        enemy_itens["tempo"] += 1

    else:
        enemy_itens["tempo"] += 1
        return

    pygame.draw.rect(window, (255, 120, 120), enemy_acao)
