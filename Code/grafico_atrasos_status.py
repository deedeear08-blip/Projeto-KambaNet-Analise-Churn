import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT
        c.status,
        p.pagamentos_atrasados
    FROM clientes c
    JOIN pagamentos p
        ON c.id = p.cliente_id
""", conn)

conn.close()

ativos = df.loc[
    df["status"] == "Ativo",
    "pagamentos_atrasados"
]

cancelados = df.loc[
    df["status"] == "Cancelado",
    "pagamentos_atrasados"
]

plt.figure(figsize=(8, 5))

plt.boxplot(
    [ativos, cancelados],
    labels=["Ativo", "Cancelado"]
)

plt.title("Distribuição de Pagamentos Atrasados por Status")
plt.xlabel("Status")
plt.ylabel("Pagamentos Atrasados")
plt.grid(axis="y", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/atrasos_status_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()