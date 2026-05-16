import matplotlib.pyplot as plt
import numpy as np


tempo_exp = np.array([0, 3.07, 4.58, 4.66, 5.21, 6.23])
posicao_exp = np.array([0, 20, 40, 60, 80, 100])

tempo_medio = np.array([0, 3.03, 4.06, 4.86, 5.53, 6.12])
posicao_medio = np.array([0, 20, 40, 60, 80, 100])

A, B, C = np.polyfit(tempo_exp, posicao_exp, 2)

tempo_curva = np.linspace(0, 40, 100)
posicao_curva = A * tempo_curva**2 + B * tempo_curva + C

plt.figure(figsize=(11, 7)) 

plt.plot(tempo_curva, posicao_curva, color='red', linestyle='--', label='Curva de tendência')

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
plt.xlim(-0.5, 7) 
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7])


plt.ylabel("posição(cm)", fontsize=12, labelpad=10)
plt.ylim(-10, 115)
plt.yticks([0, 20, 40, 60, 80, 100])

plt.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)
plt.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.show()
