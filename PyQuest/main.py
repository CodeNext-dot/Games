# bibliotecas
import pygame
import threading
import os
import random

pygame.init()

# variaveis
posX = 500
posY = 600
window = pygame.display.set_mode((posX, posY))
clock = pygame.time.Clock()
resposta = ""

# variaveis do jogo
player_itens = {
    "name": "",
    "person": 0,
    "life": 100,
    "damage": 10,
    "money": 0,
    "cor": (0, 0, 0)
}
enemy_itens = {
    "life": 10,
    "damage": 5,
    "cor": (128, 0, 128),
    "tempo": 0
}

# objetos
player = pygame.Rect(posX / 2, posY - 50, 50, 50)
enemy = pygame.Rect(random.randrange(50, 451, 50), random.randrange(50, 401, 50), 50, 50)
player_acao = pygame.Rect(0, 0, 10, 10)
enemy_acao = pygame.Rect(0, 0, 10, 10)

# funções a parte
os.system("cls")
def receber_input():
    global resposta
    global player_itens

    # Menu de cadastro
    print("\033[96m" + "="*20 + " BEM VINDO AO CADASTRO DO JOGADOR " + "="*20 + "\033[0m")
    player_itens["name"] = str(input("Nome do jogador: "))
    player_itens["person"] = int(input("Personagens[1 - azul][2 - vermelho][3 - verde]: "))
    tutorial = int(input("Deseja o tutorial?[1 - Sim][2 - Não]: "))
    os.system("cls")
    print("\033[32mConcluído!\033[0m")

    # cores e tutorial
    if(player_itens["person"] == 1):
        player_itens["cor"] = (0, 0, 255)
    elif(player_itens["person"] == 2):
        player_itens["cor"] = (255, 0, 0)
    elif(player_itens["person"] == 3):
        player_itens["cor"] = (0, 255, 0)
    else:
        player_itens["cor"] = (255, 255, 255)
    if(tutorial == 1):
        print(
            "\033[33m"
            "=========== COMANDOS ===========\n"
            "| W  -> Frente\n"
            "| A  -> Esquerda\n"
            "| S  -> Voltar\n"
            "| D  -> Direita\n"
            "| E  -> Pegar\n"
            "| Q  -> Atacar\n"
            "--------------------------------\n"
            "| WE -> Frente + Pegar\n"
            "| WQ -> Frente + Atacar\n"
            "================================"
            "\033[0m"
        )

    # dados de resposta e informações
    while True:
        if resposta == "":
            print("\033[96m" + "="*50 + "\033[0m")
            print(f"| vida: {player_itens['life']}\n| dano: {player_itens['damage']}\n| dinheiro: R${player_itens['money']:.2f}")
            resposta = input("--> ")
            print("\033[33mRodando...\033[0m")
threading.Thread(target=receber_input, daemon=True).start()

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

def receber_resposta(respostas):
    for resposta in respostas.split('-'):
        receber_inimigo() # ativa as ações do inimigo

        if((resposta == 'w') and (0 < player.y)):
            player.move_ip(0, -50)
        elif((resposta == 'd') and (posX - 50 > player.x)):
            player.move_ip(50, 0)
        elif((resposta == 'a') and (0 < player.x)):
            player.move_ip(-50, 0)
        elif((resposta == 's') and (posY - 50 > player.y)):
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

        atualizar_windows()

# ver depois --
def receber_iteracoes():
    if player_acao.colliderect(enemy):
        enemy_itens["life"] -= 1
    if enemy_acao.colliderect(player):
        player_itens["life"] -= 10

def atualizar_windows():
    pygame.display.flip()
    if resposta:
        pygame.time.delay(500)

    window.fill((0, 0, 0))
    
    pygame.draw.rect(window, enemy_itens["cor"], enemy)
    pygame.draw.rect(window, player_itens["cor"], player)

    pygame.display.flip()
    
# função principal
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if resposta:
        receber_resposta(resposta)
        resposta = ""
        
    atualizar_windows()
    clock.tick(60)

pygame.quit()