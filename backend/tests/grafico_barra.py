import matplotlib.pyplot as plt

# Dados
labels = ['Carboidratos', 'Proteínas', 'Lipídios', 'Açucares']
values = [10, 20, 15, 30]
colors = ["red", 'blue', 'green', 'orange']

# Criar gráfico de barras
plt.bar(labels, values, color = colors)

# Títulos e rótulos
plt.title("Gráfico de Barras")
plt.xlabel("Categorias")
plt.ylabel("Valores")

# Exibir o gráfico
plt.show()
