import sqlite3

# =========================================================
# CONEXÃO COM O BANCO DE DADOS
# =========================================================

conn = sqlite3.connect("kambanet.db")
cursor = conn.cursor()

# Ativar FOREIGN KEY
cursor.execute("PRAGMA foreign_keys = ON")


# =========================================================
# APAGAR TABELAS ANTIGAS
# =========================================================
# Primeiro as tabelas dependentes e depois clientes

cursor.execute("DROP TABLE IF EXISTS pagamentos")
cursor.execute("DROP TABLE IF EXISTS suporte")
cursor.execute("DROP TABLE IF EXISTS clientes")


# =========================================================
# 1. CRIAR TABELA CLIENTES
# =========================================================

cursor.execute("""
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE NOT NULL,
    nome TEXT NOT NULL,
    provincia TEXT NOT NULL,

    tipo_cliente TEXT NOT NULL
        CHECK(tipo_cliente IN ('Residencial', 'Empresarial')),

    plano TEXT NOT NULL
        CHECK(plano IN ('Básico', 'Standard', 'Premium')),

    mensalidade REAL NOT NULL,
    meses_cliente INTEGER NOT NULL,

    status TEXT NOT NULL
        CHECK(status IN ('Cancelado', 'Ativo'))
)
""")


# =========================================================
# DADOS DOS CLIENTES
# =========================================================

clientes = [
    ('CLI001', 'João', 'Luanda', 'Residencial', 'Básico', 15000, 3, 'Cancelado'),
    ('CLI002', 'Maria', 'Luanda', 'Residencial', 'Premium', 35000, 24, 'Ativo'),
    ('CLI003', 'Pedro', 'Benguela', 'Residencial', 'Básico', 15000, 5, 'Cancelado'),
    ('CLI004', 'Ana', 'Luanda', 'Residencial', 'Standard', 25000, 18, 'Ativo'),
    ('CLI005', 'Carlos', 'Huíla', 'Residencial', 'Básico', 15000, 2, 'Cancelado'),
    ('CLI006', 'Sofia', 'Luanda', 'Residencial', 'Premium', 35000, 30, 'Ativo'),
    ('CLI007', 'Manuel', 'Benguela', 'Residencial', 'Standard', 25000, 8, 'Cancelado'),
    ('CLI008', 'Isabel', 'Luanda', 'Residencial', 'Básico', 15000, 14, 'Ativo'),
    ('CLI009', 'António', 'Huambo', 'Residencial', 'Premium', 35000, 6, 'Cancelado'),
    ('CLI010', 'Teresa', 'Luanda', 'Residencial', 'Standard', 25000, 20, 'Ativo'),
    ('CLI011', 'Paulo', 'Benguela', 'Residencial', 'Básico', 15000, 4, 'Cancelado'),
    ('CLI012', 'Carla', 'Luanda', 'Residencial', 'Premium', 35000, 36, 'Ativo'),
    ('CLI013', 'Bruno', 'Huíla', 'Residencial', 'Standard', 25000, 7, 'Cancelado'),
    ('CLI014', 'Marta', 'Luanda', 'Residencial', 'Básico', 15000, 10, 'Ativo'),
    ('CLI015', 'Ricardo', 'Huambo', 'Residencial', 'Premium', 35000, 4, 'Cancelado'),
    ('CLI016', 'Elisa', 'Luanda', 'Residencial', 'Standard', 25000, 16, 'Ativo'),
    ('CLI017', 'Daniel', 'Benguela', 'Residencial', 'Básico', 15000, 3, 'Cancelado'),
    ('CLI018', 'Júlia', 'Luanda', 'Residencial', 'Premium', 35000, 28, 'Ativo'),
    ('CLI019', 'Fernando', 'Huíla', 'Residencial', 'Standard', '25000', 5, 'Cancelado'),
    ('CLI020', 'Patrícia', 'Luanda', 'Residencial', 'Básico', 15000, 22, 'Ativo'),
    ('CLI021', 'Luís', 'Huambo', 'Residencial', 'Premium', 35000, 3, 'Cancelado'),
    ('CLI022', 'Beatriz', 'Luanda', 'Residencial', 'Standard', 25000, 19, 'Ativo'),
    ('CLI023', 'Sérgio', 'Benguela', 'Residencial', 'Básico', 15000, 6, 'Cancelado'),
    ('CLI024', 'Daniela', 'Luanda', 'Residencial', 'Premium', 35000, 32, 'Ativo'),
    ('CLI025', 'Ricardo', 'Huíla', 'Residencial', 'Standard', 25000, 9, 'Ativo'),
    ('CLI026', 'Helena', 'Luanda', 'Residencial', 'Básico', 15000, 12, 'Ativo'),
    ('CLI027', 'Jorge', 'Huambo', 'Residencial', 'Premium', 35000, 2, 'Cancelado'),
    ('CLI028', 'Vanessa', 'Luanda', 'Residencial', 'Standard', 25000, 15, 'Ativo'),
    ('CLI029', 'Mateus', 'Benguela', 'Residencial', 'Básico', 15000, 3, 'Cancelado'),
    ('CLI030', 'Laura', 'Luanda', 'Residencial', 'Premium', 35000, 26, 'Ativo')
]


# =========================================================
# INSERIR CLIENTES
# =========================================================

cursor.executemany("""
    INSERT INTO clientes (
        codigo,
        nome,
        provincia,
        tipo_cliente,
        plano,
        mensalidade,
        meses_cliente,
        status
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", clientes)


# =========================================================
# 2. CRIAR TABELA SUPORTE
# =========================================================

cursor.execute("""
CREATE TABLE suporte (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    reclamacoes INTEGER NOT NULL,

    FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
)
""")


# =========================================================
# DADOS DE SUPORTE
# =========================================================

suporte = [
    (1, 5),
    (2, 1),
    (3, 4),
    (4, 1),
    (5, 6),
    (6, 0),
    (7, 5),
    (8, 1),
    (9, 7),
    (10, 0),
    (11, 4),
    (12, 0),
    (13, 6),
    (14, 2),
    (15, 5),
    (16, 1),
    (17, 5),
    (18, 0),
    (19, 4),
    (20, 1),
    (21, 6), 
    (22, 0),
    (23, 5),
    (24, 0),
    (25, 2),
    (26, 1),
    (27, 7),
    (28, 1),
    (29, 4),
    (30, 0)
]


# =========================================================
# INSERIR SUPORTE
# =========================================================

cursor.executemany("""
    INSERT INTO suporte (
        cliente_id,
        reclamacoes
    )
    VALUES (?, ?)
""", suporte)


# =========================================================
# 3. CRIAR TABELA PAGAMENTOS
# =========================================================

cursor.execute("""
CREATE TABLE pagamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    pagamentos_atrasados INTEGER NOT NULL,

    FOREIGN KEY (cliente_id)
        REFERENCES clientes(id)
)
""")


# =========================================================
# DADOS DE PAGAMENTOS
# =========================================================

pagamentos = [
    (1, 2),
    (2, 0),
    (3, 1),
    (4, 0),
    (5, 3),
    (6, 0),
    (7, 2),
    (8, 0),
    (9, 2),
    (10, 0),
    (11, 1),
    (12, 0),
    (13, 3),
    (14, 0),
    (15, 2),
    (16, 0),
    (17, 2),
    (18, 0),
    (19, 2),
    (20, 0),
    (21, 3),
    (22, 0),
    (23, 1),
    (24, 0),
    (25, 1),
    (26, 0),
    (27, 2),
    (28, 0),
    (29, 1),
    (30, 0)
]


# =========================================================
# INSERIR PAGAMENTOS
# =========================================================

cursor.executemany("""
    INSERT INTO pagamentos (
        cliente_id,
        pagamentos_atrasados
    )
    VALUES (?, ?)
""", pagamentos)


# =========================================================
# GUARDAR TODAS AS ALTERAÇÕES
# =========================================================

conn.commit()


# =========================================================
# SELECTS — ANÁLISE DOS DADOS
# =========================================================

print("\n========================================")
print("        CLIENTES")
print("========================================")

cursor.execute("""
SELECT *
FROM clientes
""")

for linha in cursor.fetchall():
    print(linha)


print("\n========================================")
print("        SUPORTE")
print("========================================")

cursor.execute("""
SELECT *
FROM suporte
""")

for linha in cursor.fetchall():
    print(linha)


print("\n========================================")
print("        PAGAMENTOS")
print("========================================")

cursor.execute("""
SELECT *
FROM pagamentos
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# SELECT — CLIENTES + SUPORTE + PAGAMENTOS
# =========================================================

print("\n========================================")
print("     VISÃO GERAL DOS CLIENTES")
print("========================================")

cursor.execute("""
SELECT
    c.id,
    c.nome,
    c.provincia,
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
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# TOTAL DE CLIENTES
# =========================================================

print("\n========================================")
print("     TOTAL DE CLIENTES")
print("========================================")

cursor.execute("""
SELECT COUNT(*)
FROM clientes
""")

print(cursor.fetchone()[0])


# =========================================================
# CLIENTES ATIVOS E CANCELADOS
# =========================================================

print("\n========================================")
print("     STATUS DOS CLIENTES")
print("========================================")

cursor.execute("""
SELECT
    status,
    COUNT(*) AS quantidade
FROM clientes
GROUP BY status
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# CLIENTES POR PLANO
# =========================================================

print("\n========================================")
print("     CLIENTES POR PLANO")
print("========================================")

cursor.execute("""
SELECT
    plano,
    COUNT(*) AS quantidade
FROM clientes
GROUP BY plano
ORDER BY quantidade DESC
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# CLIENTES POR PROVÍNCIA
# =========================================================

print("\n========================================")
print("     CLIENTES POR PROVÍNCIA")
print("========================================")

cursor.execute("""
SELECT
    provincia,
    COUNT(*) AS quantidade
FROM clientes
GROUP BY provincia
ORDER BY quantidade DESC
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# RECEITA MENSAL DOS CLIENTES ATIVOS
# =========================================================

print("\n========================================")
print("     RECEITA MENSAL — CLIENTES ATIVOS")
print("========================================")

cursor.execute("""
SELECT
    SUM(mensalidade)
FROM clientes
WHERE status = 'Ativo'
""")

print(f"{cursor.fetchone()[0]:,.2f} Kz")


# =========================================================
# RECEITA PERDIDA COM CANCELAMENTOS
# =========================================================

print("\n========================================")
print("     RECEITA PERDIDA")
print("========================================")

cursor.execute("""
SELECT
    SUM(mensalidade)
FROM clientes
WHERE status = 'Cancelado'
""")

print(f"{cursor.fetchone()[0]:,.2f} Kz")


# =========================================================
# TOTAL DE RECLAMAÇÕES
# =========================================================

print("\n========================================")
print("     TOTAL DE RECLAMAÇÕES")
print("========================================")

cursor.execute("""
SELECT
    SUM(reclamacoes)
FROM suporte
""")

print(cursor.fetchone()[0])


# =========================================================
# TOTAL DE PAGAMENTOS ATRASADOS
# =========================================================

print("\n========================================")
print("     TOTAL DE PAGAMENTOS ATRASADOS")
print("========================================")

cursor.execute("""
SELECT
    SUM(pagamentos_atrasados)
FROM pagamentos
""")

print(cursor.fetchone()[0])


# =========================================================
# CLIENTES COM MAIS RECLAMAÇÕES
# =========================================================

print("\n========================================")
print("     CLIENTES COM MAIS RECLAMAÇÕES")
print("========================================")

cursor.execute("""
SELECT
    c.nome,
    s.reclamacoes
FROM clientes c
JOIN suporte s
    ON c.id = s.cliente_id
ORDER BY s.reclamacoes DESC
LIMIT 10
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# CLIENTES COM PAGAMENTOS ATRASADOS
# =========================================================

print("\n========================================")
print("     PAGAMENTOS ATRASADOS")
print("========================================")

cursor.execute("""
SELECT
    c.nome,
    p.pagamentos_atrasados
FROM clientes c
JOIN pagamentos p
    ON c.id = p.cliente_id
WHERE p.pagamentos_atrasados > 0
ORDER BY p.pagamentos_atrasados DESC
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# CLIENTES CANCELADOS COM RECLAMAÇÕES
# =========================================================

print("\n========================================")
print("     CANCELADOS + RECLAMAÇÕES")
print("========================================")

cursor.execute("""
SELECT
    c.nome,
    c.plano,
    s.reclamacoes
FROM clientes c
JOIN suporte s
    ON c.id = s.cliente_id
WHERE c.status = 'Cancelado'
ORDER BY s.reclamacoes DESC
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# CLIENTES CANCELADOS COM ATRASOS
# =========================================================

print("\n========================================")
print("     CANCELADOS + PAGAMENTOS ATRASADOS")
print("========================================")

cursor.execute("""
SELECT
    c.nome,
    c.plano,
    p.pagamentos_atrasados
FROM clientes c
JOIN pagamentos p
    ON c.id = p.cliente_id
WHERE c.status = 'Cancelado'
ORDER BY p.pagamentos_atrasados DESC
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# ANÁLISE COMBINADA
# =========================================================

print("\n========================================")
print("     ANÁLISE COMBINADA")
print("========================================")

cursor.execute("""
SELECT
    c.nome,
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

WHERE s.reclamacoes >= 5
   OR p.pagamentos_atrasados >= 2

ORDER BY
    s.reclamacoes DESC,
    p.pagamentos_atrasados DESC
""")

for linha in cursor.fetchall():
    print(linha)


# =========================================================
# FECHAR CONEXÃO
# =========================================================

conn.close()

print("\n========================================")
print("Banco de dados criado com sucesso!")
print("3 tabelas criadas.")
print("30 clientes + suporte + pagamentos inseridos.")
print("========================================")