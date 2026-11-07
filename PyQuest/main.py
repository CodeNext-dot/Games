# bibliotecas
import pygame
import threading
import os

pygame.init()

# variaveis
posX = 500
posY = 600
window = pygame.display.set_mode((posX, posY))
clock = pygame.time.Clock()
resposta = ""

# variaveis do player
player_itens = {
    "name": "",
    "person": 0,
    "life": 100,
    "damage": 10,
    "money": 0,
    "cor": (0, 0, 0)
}

# objetos
player = pygame.Rect(posX / 2, posY - 50, 50, 50)

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
    if((player_itens["person"] != 1) and (player_itens["person"] != 2) and (player_itens["person"] != 3)):
        player_itens["cor"] = (255, 255, 255)
    else:
        if(player_itens["person"] == 1):
            player_itens["cor"] = (0, 0, 255)
        elif(player_itens["person"] == 2):
            player_itens["cor"] = (255, 0, 0)
        else:
            player_itens["cor"] = (0, 255, 0)
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

def receber_resposta(resposta):
    if((resposta == 'w') and (0 < player.y)):
        player.move_ip(0, -50)
    elif((resposta == 'd') and (posX - 50 > player.x)):
        player.move_ip(50, 0)
    elif((resposta == 'a') and (0 < player.x)):
        player.move_ip(-50, 0)
    elif((resposta == 's') and (posY - 50 > player.y)):
        player.move_ip(0, 50)
    elif(resposta == 'e'):
        pegar = pygame.Rect(player.x + 20, player.y - 25, 10, 10)
        pygame.draw.rect(window, (255, 255, 0), pegar)
        pygame.display.flip()
        tempo_inicio = pygame.time.get_ticks()
        while True:
            if pygame.time.get_ticks() - tempo_inicio >= 1000:
                break

    elif(resposta == 'q'):
        player.move_ip(0, 50)

# função principal
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if resposta:
        receber_resposta(resposta)
        resposta = ""
        
    window.fill((0, 0, 0))

    pygame.draw.rect(window, player_itens["cor"], player)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()