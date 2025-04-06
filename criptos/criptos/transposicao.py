def criptografia_transposicao(mensagem, chave):
    ordem = sorted(range(len(chave)), key=lambda x: chave[x])
    
    colunas = len(chave)
    linhas = [''] * colunas

    for i in range(len(mensagem)):
        linhas[i % colunas] += mensagem[i]

    mensagem_criptografada = ''.join(linhas[i] for i in ordem)
    return mensagem_criptografada

def transp():
    mensagem = input("insira sua mensagem\n>:")
    chave = input("insira a chave desejada\n>:")
    resultado = criptografia_transposicao(mensagem, chave)
    print(resultado)