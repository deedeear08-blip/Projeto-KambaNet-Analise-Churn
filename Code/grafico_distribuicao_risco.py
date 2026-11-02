import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT
        s.reclamacoes,
        p.pagamentos_atrasados
    FROM clientes c
    JOIN suporte s
        ON c.id = s.cliente_id
    JOIN pagamentos p
        ON c.id = p.cliente_id
""", conn)

conn.close()

risco = (
    df["reclamacoes"]
    + 2 * df["pagamentos_atrasados"]
)

plt.figure(figsize=(8, 5))

plt.hist(
    risco,
    bins=8,
    edgecolor="black"
)

plt.title("Distribuição do Score de Risco")
plt.xlabel("Score de Risco")
plt.ylabel("Número de Clientes")
plt.grid(axis="y", alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/distribuicao_risco.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()