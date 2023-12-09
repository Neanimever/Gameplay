import random


def play():
    welcome()

    secret_word = random_word()

    got_hint = ["_" for word in secret_word]

    lost_game = False
    win_game = False
    error = 0

    print("Dica: Linguagem de Programação")

    while ((not lost_game) and (not win_game)):
        print(got_hint)

        user_try = input("Digite uma letra: ")
        user_try = user_try.strip().lower()

        if (user_try in secret_word):
            index = 0
            for word in secret_word:
                if (user_try == word):
                    got_hint[index] = word
                index += 1
        else:
            error += 1
            hangman_body(error)
            print(f"Você ainda possui {7 - error} tentativas")

        lost_game = error == 7
        win_game = "_" not in got_hint

    if (win_game):
        winner(got_hint, secret_word)
    else:
        loser(secret_word)

    print("Fim do jogo")


def welcome():
    print("************************************")
    print("****Bem vindo ao jogo da Forca!****")
    print("************************************")


def random_word():
    list_word = ["Python", "Java", "JavaScript", "Ruby", "PHP", "Swift", "GoogleGo"]
    list_word = list_word[random.randrange(0, len(list_word))]
    secret_word = list_word.lower()

    return secret_word


def hangman_body(error):
    print("  _______     ")
    print(" |/      |    ")

    if (error == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (error == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (error == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (error == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (error == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (error == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (error == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def winner(got_hint, secret_word):
    print(got_hint)
    print(f"Parabéns!! Você acertou a palavra secreta: {secret_word.capitalize()}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def loser(secret_word):
    print("Puxa, você foi enforcado :(")
    print(f"A palavra secreta era {secret_word.capitalize()}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if (__name__ == "__main__"):
    play()

