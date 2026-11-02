import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query(
    "SELECT provincia FROM clientes",
    conn
)

conn.close()

dados = df["provincia"].value_counts().sort_values()

plt.figure(figsize=(8, 5))

plt.barh(
    dados.index,
    dados.values,
    edgecolor="black"
)

plt.title("Clientes por Província")
plt.xlabel("Quantidade de Clientes")
plt.ylabel("Província")
plt.grid(axis="x", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/clientes_provincias.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()