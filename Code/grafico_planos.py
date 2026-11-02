import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query(
    "SELECT plano FROM clientes",
    conn
)

conn.close()

dados = df["plano"].value_counts()

plt.figure(figsize=(8, 5))

plt.bar(
    dados.index,
    dados.values,
    edgecolor="black"
)

plt.title("Quantidade de Clientes por Plano")
plt.xlabel("Plano")
plt.ylabel("Clientes")
plt.grid(axis="y", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/clientes_planos.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()