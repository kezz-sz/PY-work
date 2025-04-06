def criptografia_porta(mensagem, chave):
    ordem = sorted(range(len(chave)), key=lambda x: chave[x])
    
    colunas = len(chave)
    linhas = [''] * colunas

    for i in range(len(mensagem)):
        linhas[i % colunas] += mensagem[i]

    mensagem_criptografada = ''.join(linhas[i] for i in ordem)
    return mensagem_criptografada

def porta():
    mensagem = input("insira sua mensagem:\n>")
    chave = "ABCD"
    resultado = criptografia_porta(mensagem, chave)
    print(resultado)