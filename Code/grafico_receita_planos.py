import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT plano, mensalidade
    FROM clientes
    WHERE status = 'Ativo'
""", conn)

conn.close()

dados = df.groupby("plano")["mensalidade"].sum()

plt.figure(figsize=(8, 5))

plt.bar(
    dados.index,
    dados.values,
    edgecolor="black"
)

plt.title("Receita Mensal por Plano")
plt.xlabel("Plano")
plt.ylabel("Receita (Kz)")
plt.grid(axis="y", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/receita_planos.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()