import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT
        c.status,
        s.reclamacoes
    FROM clientes c
    JOIN suporte s
        ON c.id = s.cliente_id
""", conn)

conn.close()

ativos = df.loc[
    df["status"] == "Ativo",
    "reclamacoes"
]

cancelados = df.loc[
    df["status"] == "Cancelado",
    "reclamacoes"
]

plt.figure(figsize=(8, 5))

plt.boxplot(
    [ativos, cancelados],
    labels=["Ativo", "Cancelado"]
)

plt.title("Distribuição de Reclamações por Status")
plt.xlabel("Status")
plt.ylabel("Número de Reclamações")
plt.grid(axis="y", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/reclamacoes_status_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()