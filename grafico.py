import matplotlib.pyplot as plt

y = [20, 40, 60, 80, 100]
x = [9.42, 20.98, 21.71, 27.14, 38.81]

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

ax.plot(x, y, marker='o', markersize=10, linewidth=2.5, color='#2c3e50', 
        markerfacecolor='white', markeredgewidth=2, markeredgecolor='#e74c3c', 
        label='Valores Coletados')

for i in range(len(x)):
    label_formatado = f"{x[i]:.2f}".replace('.', ',')
    
    ax.annotate(
        label_formatado,          
        (x[i], y[i]),             
        textcoords="offset points", 
        xytext=(0, 12),           
        ha='center',              
        fontsize=11,              
        fontweight='bold',        
        color='#c0392b'           
    )

ax.set_title('Evolução dos Dados (X vs Y)', fontsize=18, fontweight='bold', pad=25)
ax.set_xlabel('Eixo X', fontsize=12, fontweight='bold')
ax.set_ylabel('Eixo Y', fontsize=12, fontweight='bold')

ax.set_ylim(min(y) - 1, max(y) + 1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

plt.savefig('grafico_com_valores.png')
print("Gráfico com rótulos salvo como 'grafico_com_valores.png'!")
plt.show()
