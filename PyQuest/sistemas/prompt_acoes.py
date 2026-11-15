import os
import entidades.classes as game_classes

def receber_input(resposta_status: game_classes.GameData, player_status: game_classes.Player_status):
    # Limpa o prompt
    os.system("cls")

    # Menu de cadastro
    print("\033[96m" + "="*20 + " BEM VINDO AO CADASTRO DO JOGADOR " + "="*20 + "\033[0m")
    player_status.name = str(input("Nome do jogador: "))
    player_status.person = int(input("Personagens[1 - azul][2 - vermelho][3 - verde]: "))
    tutorial = int(input("Deseja o tutorial?[1 - Sim][2 - Não]: "))

    # Limpa o prompt
    os.system("cls")

    print("\033[32mConcluído!\033[0m")

    # Cores e tutorial
    if player_status.person == 1:
        player_status.color = (0, 0, 255)
    elif player_status.person == 2:
        player_status.color = (255, 0, 0)
    elif player_status.person == 3:
        player_status.color = (0, 255, 0)
    else:
        player_status.color = (255, 255, 255)

    if tutorial == 1:
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

    # Dados de resposta e informações
    while True:
        if resposta_status.resposta == "":
            print("\033[96m" + "="*50 + "\033[0m")
            print(f"| vida: {player_status.life}\n| dano: {player_status.damage}\n| dinheiro: R${player_status.money:.2f}")
            resposta_status.resposta = input("--> ")
            print("\033[33mRodando...\033[0m")