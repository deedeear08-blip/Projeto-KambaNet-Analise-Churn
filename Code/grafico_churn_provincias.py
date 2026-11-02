import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query(
    "SELECT provincia, status FROM clientes",
    conn
)

conn.close()

total = df.groupby("provincia").size()

cancelados = (
    df[df["status"] == "Cancelado"]
    .groupby("provincia")
    .size()
)

churn = (
    cancelados
    .div(total)
    .fillna(0)
    * 100
).sort_values()

plt.figure(figsize=(8, 5))

plt.barh(
    churn.index,
    churn.values,
    edgecolor="black"
)

plt.title("Taxa de Churn por Província")
plt.xlabel("Churn (%)")
plt.ylabel("Província")
plt.grid(axis="x", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/churn_provincias.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()