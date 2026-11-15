import pygame, random

def atualizar_windows(game, resposta=False):
    pygame.display.flip()

    if resposta:
        pygame.time.delay(300)

    game.window.fill((0, 0, 0))

    # verifica se player passou para a próxima fase
    if game.Player.y < 0:
        game.Player = pygame.Rect(game.window.get_width() / 2, game.window.get_height() - 50, 50, 50)

        # proximo level
        game.enemy_status.level += 0.5

        # fase normal
        if game.enemy_status.level % 3 != 0:
            game.Enemy = pygame.Rect(random.randrange(50, 451, 50), random.randrange(50, 401, 50), 50, 50)
            game.enemy_status.life = 10 * game.enemy_status.level

        # fase do vendedor
        else:
            game.enemy_status.life = 0

    # inimigo, npc e player
    pygame.draw.rect(game.window, game.player_status.color, game.Player)

    if game.enemy_status.level % 3 == 0:
        pygame.draw.rect(game.window, game.npc_status.color, game.Npc)

    elif game.enemy_status.life > 0:
        pygame.draw.rect(game.window, game.enemy_status.color, game.Enemy)

    # PORTÕES
    gate_left = pygame.Rect(0, 0, 200, 10)
    gate_right = pygame.Rect(game.window.get_width() - 200, 0, 200, 10)

    pygame.draw.rect(game.window, (139, 69, 19), gate_left)
    pygame.draw.rect(game.window, (139, 69, 19), gate_right)

    # COLISÃO COM OS PORTÕES
    if game.Player.colliderect(gate_left) or game.Player.colliderect(gate_right):
        game.Player.move_ip(0, 50)

    pygame.display.flip()