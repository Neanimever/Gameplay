import random


def play():
    print("***************************************")
    print("***Bem vindo ao jogo de Adivinhação!***")
    print("***************************************")

    secret_number = int(random.random() * 50 + 1)
    total_tries = 0
    game_round = 1
    score = 1000

    print("Qual nível de dificuldade você deseja jogar?")
    print("(1) Fácil | (2) Médio | (3) Difícil")

    game_level = int(input("Escolha o nível: "))

    if (game_level == 1):
        total_tries = 25
    elif (game_level == 2):
        total_tries = 15
    elif (game_level == 3):
        total_tries = 10
    else:
        print("Parabéns!! Você desbloqueou o nível super difícil")
        total_tries = 3

    for game_round in range(1, total_tries + 1):
        print(f"Tentativa {game_round} de {total_tries}")

        attempt = input("Digite o seu número entre 1 e 50: ")

        if (int(attempt) < 1 or int(attempt) > 50):
            print("Você deve digitar um número entre 1 e 50!")
            continue

        print("Você digitou", attempt)

        win = int(attempt) == secret_number
        bigger_attempt = int(attempt) > secret_number

        if (win):
            print("Você acertou")
            print(f"Sua pontuação é {score}")
            break
        else:
            if (bigger_attempt):
                print("O número secreto é menor")
                if (game_level == 1):
                    score = score - (40 * game_round)
                elif (game_level == 2):
                    score = score - (60 * game_round)
                elif (game_level == 3):
                    score = score - (100 * game_round)
                else:
                    score = score - (300 * game_round)

                print(f"Sua pontuação é {score}")
            else:
                print("O número secreto é maior")
                if (game_level == 1):
                    score = score - (40 * game_round)
                elif (game_level == 2):
                    score = score - (60 * game_round)
                elif (game_level == 3):
                    score = score - (100 * game_round)
                else:
                    score = score - (300 * game_round)

                print(f"Sua pontuação é {score}")

    print("Fim do jogo")

if (__name__ == "__main__"):
    play()

