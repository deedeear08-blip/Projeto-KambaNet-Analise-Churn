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

total = df.groupby("plano").size()

cancelados = (
    df[df["status"] == "Cancelado"]
    .groupby("plano")
    .size()
)

churn = (
    cancelados
    .div(total)
    .fillna(0)
    * 100
)

plt.figure(figsize=(8, 5))

plt.bar(
    churn.index,
    churn.values,
    edgecolor="black"
)

plt.title("Taxa de Churn por Plano")
plt.xlabel("Plano")
plt.ylabel("Churn (%)")
plt.grid(axis="y", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/churn_planos.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()