import os

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cifra_de_cesar(texto, deslocamento):
    resultado = ""

    for i in range(len(texto)):
        char = texto[i]

        if char.isupper():
            resultado += chr((ord(char) + int(deslocamento) - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) + int(deslocamento) - 97) % 26 + 97)
        else:
            resultado += char

    return resultado