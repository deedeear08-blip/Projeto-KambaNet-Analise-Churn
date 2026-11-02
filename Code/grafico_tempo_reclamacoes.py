import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT
        c.meses_cliente,
        s.reclamacoes
    FROM clientes c
    JOIN suporte s
        ON c.id = s.cliente_id
""", conn)

conn.close()

plt.figure(figsize=(8, 5))

plt.scatter(
    df["meses_cliente"],
    df["reclamacoes"]
)

plt.title("Tempo como Cliente vs Reclamações")
plt.xlabel("Meses como Cliente")
plt.ylabel("Reclamações")
plt.grid(alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/tempo_reclamacoes.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()