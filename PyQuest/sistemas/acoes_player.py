import pygame
import sistemas.acoes_enemy as enemy_actions
import sistemas.acoes_npc as npc_actions
import sistemas.acoes_musics as action_music

def receber_resposta(resposta, game):
    if(game.enemy_status.life > 0):
        enemy_actions.receber_inimigo(game)


    if (resposta == 'w') or (resposta == 'a') or (resposta == 's') or (resposta == 'd'):
        if resposta == 'w':
            game.Player.move_ip(0, -50)
            action_music.som_movimento()

        elif resposta == 'd' and game.window.get_width() - 50 > game.Player.x:
            game.Player.move_ip(50, 0)
            action_music.som_movimento()

        elif resposta == 'a' and 0 < game.Player.x:
            game.Player.move_ip(-50, 0)
            action_music.som_movimento()

        elif resposta == 's' and game.window.get_height() - 50 > game.Player.y:
            game.Player.move_ip(0, 50)
            action_music.som_movimento()

        # verificar colisão com o inimigo
        if(game.Player.colliderect(game.Enemy)):
            if(game.enemy_status.life > 0):
                action_music.som_ataque()

                print("\033[91mVocê atingiu o inimigo! -10 vida\033[0m")
                game.Player.move_ip(0, 50)

                game.player_status.life -= 10
                
                if(game.player_status.life <= 0):
                    print("\033[91m VOCÊ MORREU \033[0m")
                    game.running = False

    elif 'e' in resposta or 'q' in resposta:

        if 'w' in resposta:
            acao_temp = [20, -25]

        elif 'd' in resposta:
            acao_temp = [75, 20]

        elif 'a' in resposta:
            acao_temp = [-25, 20]

        elif 's' in resposta:
            acao_temp = [20, 74]
            
        else:
            acao_temp = [20, -25]

        player_acao = pygame.Rect(game.Player.x + acao_temp[0], game.Player.y + acao_temp[1], 10, 10)

        if 'e' in resposta:
            pygame.draw.rect(game.window, (255, 255, 150), player_acao)

            # verifica se tocou no npc
            if (player_acao.colliderect(game.Npc)):
                action_music.som_interacao()

                print(f"Voce tocou no Bob!")
                npc_actions.receber_interacao(game)

        else:
            
            pygame.draw.rect(game.window, (255, 120, 120), player_acao)

            # verifica se ataque bateu no inimigo
            if (player_acao.colliderect(game.Enemy)) and (game.enemy_status.life > 0):
                action_music.som_ataque()

                print(f"O ataque acertou o inimigo!")
                game.enemy_status.life -= game.player_status.damage

                if(game.enemy_status.life <= 0):
                    print("inimigo morreu")
                    game.player_status.money += 5.00 * game.enemy_status.level