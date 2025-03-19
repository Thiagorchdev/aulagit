import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("gasolina.csv")

# Criar o gráfico
sns.set_style("whitegrid")
plt.figure(figsize=(8, 5))
sns.lineplot(data=df, x="dia", y="venda", marker="o", linewidth=2.5)

# Configurar rótulos
plt.xlabel("Dia")
plt.ylabel("Preço da Gasolina (R$)")
plt.title("Variação do Preço da Gasolina")

# Salvar o gráfico
plt.savefig("gasolina.png")
plt.show()

