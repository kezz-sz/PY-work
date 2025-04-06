import random
import sys
import time

def contagem_regressiva(segundos):
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)
    print("Super aquecendo!")
    print("suspendendo!")
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)
    print("Não ocorreu nada, esperou de bocó!")

segundos_para_contar = 10

def roll():
    cu = random.randint(1, 1000000)
    if cu == 235:
        print("Ação mal execultada, preparando para reiniciar!")
        contagem_regressiva(segundos_para_contar)
        sys.exit()