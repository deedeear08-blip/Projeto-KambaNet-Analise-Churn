import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query(
    "SELECT plano, status FROM clientes",
    conn
)

conn.close()

dados = pd.crosstab(
    df["plano"],
    df["status"]
)

dados.plot(
    kind="bar",
    stacked=True,
    figsize=(8, 5),
    edgecolor="black"
)

plt.title("Clientes Ativos e Cancelados por Plano")
plt.xlabel("Plano")
plt.ylabel("Clientes")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)
plt.legend(title="Status")

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/status_por_plano.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()