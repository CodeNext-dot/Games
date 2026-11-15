import pygame

def receber_inimigo(game):

    if game.enemy_status.time % 4 == 0:

        # Calcula a direção do ataque
        if (game.Player.y == game.Enemy.y):

            if (game.Player.y == game.Enemy.y) and (game.Player.x > game.Enemy.x):  # direita
                enemy_acao_temp = [75, 20]

            else:  # esquerda
                enemy_acao_temp = [-25, 20]

        else:

            if (game.Player.x == game.Enemy.x) and (game.Player.y > game.Enemy.y):  # baixo
                enemy_acao_temp = [20, 75]

            else:  # cima
                enemy_acao_temp = [20, -25]


        # Cria a área do ataque
        enemy_acao = pygame.Rect(game.Enemy.x + enemy_acao_temp[0], game.Enemy.y + enemy_acao_temp[1], 10, 10)

        game.enemy_status.time += 1

    else:
        game.enemy_status.time += 1
        return

    # verifica se ataque bateu no player
    if (enemy_acao.colliderect(game.Player)) and (game.player_status.life > 0):
        print(f"O ataque do inimigo te acertou!")
        game.player_status.life -= game.enemy_status.damage

        if(game.player_status.life <= 0):
            print("\033[91m VOCÊ MORREU \033[0m")
            game.running = False

    # Desenha o ataque
    pygame.draw.rect(game.window, (255, 120, 120), enemy_acao)