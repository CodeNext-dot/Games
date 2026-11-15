# bibliotecas
import pygame, threading, random
# import sistemas.acoes_enemy as enemy_actions
import sistemas.acoes_player as player_actions
import sistemas.prompt_acoes as action_prompt
import entidades.classes as game_classes
import utilidades.atualizar_window as atualizar

pygame.init()

# variaveis
window = pygame.display.set_mode((500, 600))
clock = pygame.time.Clock()

# classes
player_status = game_classes.Player_status()
enemy_status = game_classes.Enemy_status()
resposta_status = game_classes.GameData()

# objetos
Player = pygame.Rect(window.get_width() / 2, window.get_height() - 50, 50, 50)
Enemy = pygame.Rect(random.randrange(50, 451, 50), random.randrange(50, 401, 50), 50, 50)

# função da janela 2
def prompt_acoes():
    action_prompt.receber_input(resposta_status, player_status)
threading.Thread(target=prompt_acoes, daemon=True).start()

# ações do bixos

# função principal
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if resposta_status.resposta:
        for resposta in resposta_status.resposta.split('-'):
            player_actions.receber_resposta(resposta, Player, Enemy, window)
            atualizar.atualizar_windows(window, player_status, enemy_status, Player, Enemy, True)
        
        resposta_status.resposta = ""
        
    atualizar.atualizar_windows(window, player_status, enemy_status, Player, Enemy)
    clock.tick(60)

pygame.quit()