def cifra_de_cesar1(texto, deslocamento):
    resultado = ""
    
    for i in range(len(texto)):
        char = texto[i]
        if char.isupper():
            temp = ((-ord(char) - 66 - deslocamento) % 26) + 65
            resultado += chr(temp)
        elif char.islower():
            temp = ((-ord(char) - 86 - deslocamento) % 26) + 97
            resultado += chr(temp)
        else:
            resultado += char

    return resultado