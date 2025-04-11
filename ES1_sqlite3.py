import sqlite3  # Importa il modulo per lavorare con SQLite

# 1. Connessione (crea un file 'scuola.db' se non esiste)
conn = sqlite3.connect('scuola.db')

# 2. Cursore per eseguire comandi SQL
cur = conn.cursor()

# 3. Creazione di una tabella (se non esiste)
cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

# 4. Inserimento nome tramite input utente
while True:
    nome = input("Inserisci il nome dello studente (oppure digita 'basta'): ")
    if nome == "basta":
        break
    cur.execute("INSERT INTO studenti (nome) VALUES (?)", (nome,))

# 5. Salvataggio delle modifiche
conn.commit()

# 6. Query per leggere i dati
cur.execute("SELECT * FROM studenti")
righe = cur.fetchall()

# 7. Stampa dei risultati
for riga in righe:
    print(riga)

# 8. Chiusura della connessione
conn.close()