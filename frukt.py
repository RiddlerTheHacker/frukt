import random

#Definerar en funktion
def print_fruit(userInput):
    fnr = int(userInput)
    print('\n' + frukten [fnr - 1] + ' kommer här!')

frukten =('Banan', 'Apelsin', 'Äpple', 'Päron', 'Kiwi')
looping = True

while looping:

    go = input('Vill du välja en frukt?')

    if (go == 'n'):
        break