import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT
        c.nome,
        s.reclamacoes,
        p.pagamentos_atrasados
    FROM clientes c
    JOIN suporte s
        ON c.id = s.cliente_id
    JOIN pagamentos p
        ON c.id = p.cliente_id
""", conn)

conn.close()

df["risco_score"] = (
    df["reclamacoes"]
    + 2 * df["pagamentos_atrasados"]
)

top = df.nlargest(
    10,
    "risco_score"
).sort_values(
    "risco_score"
)

plt.figure(figsize=(9, 6))

plt.barh(
    top["nome"],
    top["risco_score"],
    edgecolor="black"
)

plt.title("Top 10 Clientes por Score de Risco")
plt.xlabel("Score de Risco")
plt.ylabel("Cliente")
plt.grid(axis="x", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/top10_risco.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()