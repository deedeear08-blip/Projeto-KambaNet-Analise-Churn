import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = sqlite3.connect("kambanet.db")

df = pd.read_sql_query("""
    SELECT
        c.meses_cliente,
        p.pagamentos_atrasados
    FROM clientes c
    JOIN pagamentos p
        ON c.id = p.cliente_id
""", conn)

conn.close()

plt.figure(figsize=(8, 5))

plt.scatter(
    df["meses_cliente"],
    df["pagamentos_atrasados"]
)

plt.title("Tempo como Cliente vs Pagamentos Atrasados")
plt.xlabel("Meses como Cliente")
plt.ylabel("Pagamentos Atrasados")
plt.grid(alpha=0.3)

os.makedirs("graficos", exist_ok=True)

plt.savefig(
    "graficos/tempo_atrasos.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()