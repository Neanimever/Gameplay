import divination
import hangman

print("************************************")
print("********Escolha o seu jogo!********")
print("************************************")

print("(1) Forca | (2) Adivinhação")
game = int(input("Qual jogo deseja jogar? "))

if (game == 1):
    hangman.play()
elif (game == 2):
    divination.play()
else:
    print("Jogo não identificado")
