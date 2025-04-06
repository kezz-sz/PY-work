#biblioteca
import time  
import sys

#codigo de divisor
def linha(delay_time=0.01):
    print() 
    for i in range(102):
        print("=", end="", flush=True) 
        time.sleep(delay_time)
    print()