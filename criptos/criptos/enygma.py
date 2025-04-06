import string
alfabeto = string.ascii_uppercase

chave1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
chave2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
chave3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
chaveprincipal = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def encriptograflor(cript):
    return cript[1:] + cript[0]

def enigma_encrypt(mensagem, pos1, pos2, pos3):
    criptografafo = []
    # pinto
    # rogério
    chave_pos1 = chave1[pos1:] + chave1[:pos1]
    chave_pos2 = chave2[pos2:] + chave2[:pos2]
    chave_pos3 = chave3[pos3:] + chave3[:pos3]
    
    for letra in mensagem.upper():
        if letra in alfabeto:
            index = alfabeto.index(letra)
            letra = chave_pos1[index]
            
            index = alfabeto.index(letra)
            letra = chave_pos2[index]
            
            index = alfabeto.index(letra)
            letra = chave_pos3[index]
            
            index = alfabeto.index(letra)
            letra = chaveprincipal[index]
            
            index = chave_pos3.index(letra)
            letra = alfabeto[index]
            
            index = chave_pos2.index(letra)
            letra = alfabeto[index]
            
            index = chave_pos1.index(letra)
            letra = alfabeto[index]
            
            criptografafo.append(letra)
            
            chave_pos1 = encriptograflor(chave_pos1)
            if len(criptografafo) % 26 == 0:  
                chave_pos2 = encriptograflor(chave_pos2)
            if len(criptografafo) % (26 * 26) == 0:  
                chave_pos3 = encriptograflor(chave_pos3)
        else:
            criptografafo.append(letra)  
    
    return ''.join(criptografafo)