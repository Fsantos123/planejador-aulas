import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS planos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tema TEXT,
    turma TEXT,
    data TEXT,
    objetivo TEXT,
    atividade TEXT
)
''')

conn.commit()
conn.close()

print("Banco criado!")