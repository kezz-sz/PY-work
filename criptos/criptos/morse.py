from delay import delay

chave = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
         '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.'}

def morse():
    mensagem1 = "Digite o texto a traduzir"
    delay(mensagem1,100)
    resposta1 = input('\n>:')
    mensagem_a_codificar = resposta1.upper()
    morse = []
    for char in mensagem_a_codificar:
            if char in chave:
                morse.append(chave[char])
            a = " ".join(morse)

    original = "\nmensagem original:\n"
    delay(original,100)
    delay(resposta1,100)
    mensagemmorse = "\nmensagem em morse:\n"
    delay(mensagemmorse,100)
    delay(a,100)