from delay import delay

def texto_para_binario(texto):
    return ' '.join(format(ord(c), '08b') for c in texto)

def binario():
    mensagem1 = "informe sua mensagem:"
    
    delay(mensagem1, 100)
    resposta = input("\n:>")
    binario = texto_para_binario(resposta)

    mensagem2 = f"Sua mensagem é: {binario} "
    delay(mensagem2, 100)