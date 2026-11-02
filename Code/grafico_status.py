import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query(
    "SELECT status FROM clientes",
    conn
)

conn.close()

dados = df["status"].value_counts()

plt.figure(figsize=(7, 7))

plt.pie(
    dados.values,
    labels=dados.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribuição dos Clientes por Status")

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/status_clientes.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()