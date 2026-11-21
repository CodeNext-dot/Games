# bibliotecas
import pygame, threading, random
import sistemas.acoes_player as player_actions
import sistemas.prompt_acoes as action_prompt
import sistemas.acoes_musics as action_music
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
npc_status = game_classes.Npc_status()

# objetos
Player = pygame.Rect(window.get_width() / 2, window.get_height() - 50, 50, 50)
Enemy = pygame.Rect(random.randrange(50, 451, 50), random.randrange(50, 401, 50), 50, 50)
Npc = pygame.Rect(0, 0, 50, 50)

# agrupamento
class Game:
    def __init__(self, window, player_status, enemy_status, npc_status, Player, Enemy, Npc):
        self.window = window
        self.player_status = player_status
        self.enemy_status = enemy_status
        self.npc_status = npc_status
        self.Player = Player
        self.Enemy = Enemy
        self.Npc = Npc
        self.running = True
game = Game(window, player_status, enemy_status, npc_status, Player, Enemy, Npc)

# função da janela 2
def prompt_acoes():
    action_prompt.receber_input(resposta_status, game.player_status)
threading.Thread(target=prompt_acoes, daemon=True).start()

# função principal
while game.running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
    
    if resposta_status.resposta:
        for resposta in resposta_status.resposta.split('-'):
            player_actions.receber_resposta(resposta, game)
            atualizar.atualizar_windows(game, True)
        
        resposta_status.resposta = ""
        
    atualizar.atualizar_windows(game)
    clock.tick(60)

pygame.quit()