import pygame

def receber_interacao(game):

    print("\n" + "=" * 20)
    print(f" VENDEDOR {game.npc_status.name}")
    print("=" * 20)

    print("\nVendedor: Ah... um aventureiro.")
    pygame.time.delay(300)
    print("Vendedor: Tenho algumas coisas que podem")
    pygame.time.delay(300)
    print("te ajudar a sobreviver por aqui.\n")
    pygame.time.delay(300)

    while True:
        # Preços baseados no nível do inimigo
        preco_dano = 10 * game.enemy_status.level
        preco_vida = 8 * game.enemy_status.level

        print(f"Seu dinheiro: ${game.player_status.money:.2f}\n")

        print(f"[1] Aumentar dano em +5, por R${preco_dano}")
        print(f"[2] Aumentar vida máxima em +60, por R${preco_vida}")
        print("[3] Sair")

        resposta = input("\nO que deseja comprar? ").lower()
        pygame.time.delay(300)

        # AUMENTAR DANO
        if resposta == "1":

            if game.player_status.money >= preco_dano:

                game.player_status.money -= preco_dano
                game.player_status.damage += 5

                print("\nVendedor: Uma arma mais forte...")
                print("\033[92mDano aumentado em +5!\033[0m")

            else:
                print("\nVendedor: Parece que suas moedas não são suficientes.")


        # AUMENTAR VIDA
        elif resposta == "2":
            if game.player_status.money >= preco_vida:

                game.player_status.money -= preco_vida
                game.player_status.life += 60

                print("\nVendedor: Cuide-se. Você ainda vai precisar disso.")
                print("\033[92mVida aumentada em +60!\033[0m")

            else:
                print("\nVendedor: Volte quando tiver mais dinheiro.")


        # SAIR
        elif resposta == "3":
            print("\nVendedor: Então vá... e tente não morrer por aí.")
            break

        else:
            print("\nVendedor: Não entendi o que você quer.")