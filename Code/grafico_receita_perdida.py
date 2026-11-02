import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT mensalidade, status
    FROM clientes
""", conn)

conn.close()

receita_ativa = df.loc[
    df["status"] == "Ativo",
    "mensalidade"
].sum()

receita_perdida = df.loc[
    df["status"] == "Cancelado",
    "mensalidade"
].sum()

valores = [
    receita_ativa,
    receita_perdida
]

labels = [
    "Receita atual",
    "Receita perdida"
]

plt.figure(figsize=(7, 7))

plt.pie(
    valores,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"width": 0.45}
)

plt.title("Receita Atual vs Receita Perdida")

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/receita_atual_vs_perdida.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()