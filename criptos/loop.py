import os

def limpa():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
#heranca
from menu import menu
from criptos.cesar import cifra_de_cesar
from criptos.binario import binario
from criptos.morse import morse
from criptos.transposicao import transp
from linha import linha
from delay import delay
from criptos.xruiz_wv_xvhzi import cifra_de_cesar1
from criptos.enygma import enigma_encrypt
from criptos.porta import porta

#codigo para looping
def loop():
    while True:
        menu()
        linha()
        pergunta = "Escolha uma opção"
        delay(pergunta,100)
        opcao = input("\n>:")
        
        if opcao == '1':
            limpa()
            linha()
            mensagem1 = "Escolha a Cifra:\n"
            mensagem2 = "1. Cesar comum\n"
            mensagem3 = "2. Cesar invertida\n"
            delay(mensagem1,100)
            delay(mensagem2,100)
            delay(mensagem3,100)
            linha()
            
            respostaCesar = input(">:")
            limpa()
            if respostaCesar == '1':
                texto = "Digite o texto que você deseja criptografar: "
                delay(texto, 100)
                textoresposta = input(">:")

                deslocamento = "Digite o número de casas que você quer se deslocar no alfabeto, digite apenas números: "
                delay(deslocamento, 100)

                deslocamentoresposta = input(">:")

                print(cifra_de_cesar(textoresposta, int(deslocamentoresposta)))

            if respostaCesar == '2':
                texto1 = "Digite a mensagem a ser criptografada\n"
                delay(texto1, 100)
                texto1resposta = input(">:")
                
                deslocamento1  = "Digite uma chave que seja qualquer número inteiro\n"
                delay(deslocamento1, 100)
                
                deslocamento1resposta = input(">:")
                
                print(cifra_de_cesar1(texto1resposta, int(deslocamento1resposta)))

        elif opcao == '2':
            binario()
        elif opcao == '3':
            linha()
            morse()
            linha()

        elif opcao == '4':
            linha()
            transp()
            linha()

        elif opcao == '5':
            linha()
            mensagem = "informe sua mensagem\n"
            delay(mensagem, 100)
            resposta = input(">:")
            pos1, pos2, pos3 = 0, 0, 0 
            cu = f"Mensagem criptografada: {enigma_encrypt(resposta, pos1, pos2, pos3)}"
            delay(cu, 100)
            linha()

        elif opcao == '6':
            linha()
            porta()
            linha()

        elif opcao == '0':
            saindo = "saindo..."
            delay(saindo,100)
            break

        else:
            invalido = "Opção inválida. Tente novamente."
            delay(invalido,100)

if __name__ == "__main__":
    loop()
    
