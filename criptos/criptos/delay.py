#biblioteca
import time

#codigo de delay do texto
def delay(texto, limite, delay_time=0.01):
    for i in range(len(texto)):
        print(texto[i], end="", flush=True)
        if (i + 1) % limite == 0:
            print()
        time.sleep(delay_time)