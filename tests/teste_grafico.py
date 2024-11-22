import matplotlib.pyplot as plt

# Dados
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Criar gráfico de pizza
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Garantir que o gráfico seja desenhado como um círculo
plt.axis('equal')

# Título
plt.title("Gráfico de Pizza")

# Exibir o gráfico
plt.show()
