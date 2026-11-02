import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT
        c.meses_cliente,
        c.mensalidade,
        s.reclamacoes,
        p.pagamentos_atrasados
    FROM clientes c
    JOIN suporte s
        ON c.id = s.cliente_id
    JOIN pagamentos p
        ON c.id = p.cliente_id
""", conn)

conn.close()

corr = df.corr(numeric_only=True)

plt.figure(figsize=(8, 6))

plt.imshow(
    corr,
    interpolation="nearest"
)

plt.colorbar(label="Correlação")

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

for i in range(len(corr)):
    for j in range(len(corr)):
        plt.text(
            j,
            i,
            f"{corr.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("Matriz de Correlação")

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/matriz_correlacao.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()