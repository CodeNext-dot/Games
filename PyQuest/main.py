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
player_name = ""
player_person = 3
life = 10
damage = 1
money = 0.00

# objetos
player = pygame.Rect(250, posY - 50, 50, 50)

# função a parte
os.system("cls")
def receber_input():
    global resposta
    global player_name
    global player_person
    global life
    global damage
    global money

    print("\033[96m" + "="*20 + " BEM VINDO AO CADASTRO DO JOGADOR " + "="*20 + "\033[0m")
    player_name = str(input("Nome do jogador: "))
    player_person = int(input("Personagens[1 - azul][2 - vermelho][3 - verde]: "))
    tutorial = int(input("Deseja o tutorial?[1 - Sim][2 - Não]: "))
    os.system("cls")
    print("\033[32mConcluído!\033[0m")

    if((player_person != 1) and (player_person != 2) and (player_person != 3)):
        player_person = 3
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

    while True:
        print("\033[96m" + "="*50 + "\033[0m")
        print(f"| vida: {life}\n| dano: {damage}\n| dinheiro: R${money:.2f}")
        resposta = input("--> ")
threading.Thread(target=receber_input, daemon=True).start()

# função principal
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if resposta:
        resposta = ""

    pygame.draw.rect(window, (255, 0, 0), player)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()