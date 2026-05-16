import matplotlib.pyplot as plt
import numpy as np

tempo_exp = np.array([0, 9.42, 20.48, 21.71, 27.14, 38.81])
posicao_exp = np.array([0, 20, 40, 60, 80, 100])

tempo_medio = np.array([0, 7.3, 14.7, 22.3, 29.8, 37.3])
posicao_medio = np.array([0, 20, 40, 60, 80, 100])


a, b = np.polyfit(tempo_medio, posicao_medio, 1)
tempo_reta = np.linspace(0, 40, 100)
posicao_reta = a * tempo_reta + b


plt.figure(figsize=(10, 7)) 

plt.plot(tempo_reta, posicao_reta, color='red', linestyle='--', label='Reta de tendência')

plt.scatter(tempo_exp, posicao_exp, color='blue', marker='o', s=50, zorder=4, label='Ponto experimental')

plt.scatter(tempo_medio, posicao_medio, color='#550000', marker='o', s=50, zorder=4, label='Ponto experimental médio')


for x, y in zip(tempo_exp, posicao_exp):
    label = f"({x})"
    plt.text(x, y + 4, label, fontsize=9, color='blue', ha='center', va='bottom')

for x, y in zip(tempo_medio, posicao_medio):
    label = f"({x})"
    plt.text(x, y - 4, label, fontsize=9, color='#550000', ha='center', va='top', fontweight='bold')


plt.title("Posição por Tempo", fontsize=14, fontweight='bold', pad=15)

plt.xlabel("tempo(s)", fontsize=12, labelpad=10)
plt.xlim(-2, 42) 
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35, 40])

plt.ylabel("posição(cm)", fontsize=12, labelpad=10)
plt.ylim(-5, 110)
plt.yticks([0, 20, 40, 60, 80, 100])

plt.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)

plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()
