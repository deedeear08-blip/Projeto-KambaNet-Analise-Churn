import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =========================================================
# 1. CONECTAR AO BANCO DE DADOS EXISTENTE
# =========================================================

conn = sqlite3.connect("kambanet.db")


# =========================================================
# 2. PEGAR OS DADOS DO BANCO
# =========================================================

query = """
SELECT
    c.id,
    c.codigo,
    c.nome,
    c.provincia,
    c.tipo_cliente,
    c.plano,
    c.mensalidade,
    c.meses_cliente,
    c.status,
    s.reclamacoes,
    p.pagamentos_atrasados

FROM clientes c

JOIN suporte s
    ON c.id = s.cliente_id

JOIN pagamentos p
    ON c.id = p.cliente_id

ORDER BY c.id
"""


df = pd.read_sql_query(query, conn)


# Fechar conexão
conn.close()


# =========================================================
# 3. VERIFICAR OS DADOS
# =========================================================

print("\n================ DADOS ================\n")
print(df)

print("\n================ INFORMAÇÕES ================\n")
print(df.info())

print("\n================ ESTATÍSTICAS ================\n")
print(df.describe())


# =========================================================
# 4. CRIAR PASTA PARA OS GRÁFICOS
# =========================================================

import os

os.makedirs("graficos", exist_ok=True)


# =========================================================
# 6. GRÁFICO — CLIENTES POR PLANO
# =========================================================

planos = df["plano"].value_counts()

plt.figure(figsize=(8, 6))

plt.bar(
    planos.index,
    planos.values
)

plt.title("Quantidade de Clientes por Plano")
plt.xlabel("Plano")
plt.ylabel("Quantidade de clientes")

plt.tight_layout()

plt.savefig(
    "graficos/clientes_por_plano.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# =========================================================
# 7. GRÁFICO — CLIENTES POR PROVÍNCIA
# =========================================================

provincias = df["provincia"].value_counts()

plt.figure(figsize=(9, 6))

plt.bar(
    provincias.index,
    provincias.values
)

plt.title("Clientes por Província")
plt.xlabel("Província")
plt.ylabel("Quantidade de clientes")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    "graficos/clientes_por_provincia.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# =========================================================
# 8. GRÁFICO — RECEITA MENSAL POR PLANO
# =========================================================

receita_plano = (
    df[df["status"] == "Ativo"]
    .groupby("plano")["mensalidade"]
    .sum()
)

plt.figure(figsize=(8, 6))

plt.bar(
    receita_plano.index,
    receita_plano.values
)

plt.title("Receita Mensal por Plano — Clientes Ativos")
plt.xlabel("Plano")
plt.ylabel("Receita mensal (Kz)")

plt.tight_layout()

plt.savefig(
    "graficos/receita_por_plano.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# =========================================================
# 9. GRÁFICO — RECLAMAÇÕES POR PLANO
# =========================================================

reclamacoes_plano = (
    df.groupby("plano")["reclamacoes"]
    .sum()
)

plt.figure(figsize=(8, 6))

plt.bar(
    reclamacoes_plano.index,
    reclamacoes_plano.values
)

plt.title("Total de Reclamações por Plano")
plt.xlabel("Plano")
plt.ylabel("Número de reclamações")

plt.tight_layout()

plt.savefig(
    "graficos/reclamacoes_por_plano.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# =========================================================
# 10. GRÁFICO — PAGAMENTOS ATRASADOS POR PLANO
# =========================================================

atrasos_plano = (
    df.groupby("plano")["pagamentos_atrasados"]
    .sum()
)

plt.figure(figsize=(8, 6))

plt.bar(
    atrasos_plano.index,
    atrasos_plano.values
)

plt.title("Pagamentos Atrasados por Plano")
plt.xlabel("Plano")
plt.ylabel("Pagamentos atrasados")

plt.tight_layout()

plt.savefig(
    "graficos/atrasos_por_plano.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# =========================================================
# 11. GRÁFICO — MESES COMO CLIENTE VS RECLAMAÇÕES
# =========================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    df["meses_cliente"],
    df["reclamacoes"]
)

plt.title("Tempo como Cliente vs Reclamações")
plt.xlabel("Meses como cliente")
plt.ylabel("Número de reclamações")

plt.tight_layout()

plt.savefig(
    "graficos/tempo_vs_reclamacoes.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# =========================================================
# 12. GRÁFICO — MESES COMO CLIENTE VS PAGAMENTOS ATRASADOS
# =========================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    df["meses_cliente"],
    df["pagamentos_atrasados"]
)

plt.title("Tempo como Cliente vs Pagamentos Atrasados")
plt.xlabel("Meses como cliente")
plt.ylabel("Pagamentos atrasados")

plt.tight_layout()

plt.savefig(
    "graficos/tempo_vs_atrasos.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# =========================================================
# 13. GRÁFICO — RECLAMAÇÕES VS PAGAMENTOS ATRASADOS
# =========================================================

plt.figure(figsize=(8, 6))

plt.scatter(
    df["reclamacoes"],
    df["pagamentos_atrasados"]
)

plt.title("Reclamações vs Pagamentos Atrasados")
plt.xlabel("Número de reclamações")
plt.ylabel("Pagamentos atrasados")

plt.tight_layout()

plt.savefig(
    "graficos/reclamacoes_vs_atrasos.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# =========================================================
# 14. NUMPY — CORRELAÇÕES
# =========================================================

correlacao_reclamacoes_atrasos = np.corrcoef(
    df["reclamacoes"],
    df["pagamentos_atrasados"]
)[0, 1]

correlacao_tempo_reclamacoes = np.corrcoef(
    df["meses_cliente"],
    df["reclamacoes"]
)[0, 1]

correlacao_tempo_atrasos = np.corrcoef(
    df["meses_cliente"],
    df["pagamentos_atrasados"]
)[0, 1]


print("\n================ CORRELAÇÕES ================\n")

print(
    f"Reclamações × Pagamentos atrasados: "
    f"{correlacao_reclamacoes_atrasos:.2f}"
)

print(
    f"Meses × Reclamações: "
    f"{correlacao_tempo_reclamacoes:.2f}"
)

print(
    f"Meses × Pagamentos atrasados: "
    f"{correlacao_tempo_atrasos:.2f}"
)


# =========================================================
# 15. NUMPY — RECEITA TOTAL
# =========================================================

receitas_ativas = df.loc[
    df["status"] == "Ativo",
    "mensalidade"
].to_numpy()

receita_total = np.sum(receitas_ativas)

print("\n================ RECEITA ================\n")

print(
    f"Receita mensal dos clientes ativos: "
    f"{receita_total:,.2f} Kz"
)


# =========================================================
# 16. NUMPY — RECEITA PERDIDA
# =========================================================

receitas_cancelados = df.loc[
    df["status"] == "Cancelado",
    "mensalidade"
].to_numpy()

receita_perdida = np.sum(receitas_cancelados)

print(
    f"Receita mensal perdida com cancelamentos: "
    f"{receita_perdida:,.2f} Kz"
)


# =========================================================
# FINAL
# =========================================================

print("\n============================================")
print("ANÁLISE CONCLUÍDA!")
print("============================================")
print("Os gráficos foram salvos na pasta:")
print("graficos/")