import sqlite3
import random

class Libreria:
    def __init__(self):
        self.conn = sqlite3.connect('libreria.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS libri (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titolo TEXT,
                autore TEXT
            )
        ''')
        self.conn.commit()

    def inserisci_libri(self, libri):
        self.cur.executemany('INSERT INTO libri (titolo, autore) VALUES (?, ?)', libri)
        self.conn.commit()

    def mostra_libri(self):
        try:
            self.cur.execute('SELECT id, titolo, autore, vendite FROM libri')
        except sqlite3.OperationalError:
            self.cur.execute('SELECT id, titolo, autore FROM libri')

        for riga in self.cur.fetchall():
            print(riga)

    def aggiungi_vendite(self):
        try:
            self.cur.execute('ALTER TABLE libri ADD COLUMN vendite INTEGER')
        except sqlite3.OperationalError:
            pass

        self.cur.execute('SELECT id FROM libri')
        for (libro_id,) in self.cur.fetchall():
            vendite = random.randint(10, 1000)
            self.cur.execute('UPDATE libri SET vendite = ? WHERE id = ?', (vendite, libro_id))

        self.conn.commit()

    def chiudi(self):
        self.conn.close()


#per utilizzo
libri_iniziali = [
    ("Il nome della rosa", "Umberto Eco"),
    ("1984", "George Orwell"),
    ("Il piccolo principe", "Antoine de Saint-Exupéry")
]

libreria = Libreria()
libreria.inserisci_libri(libri_iniziali)
print("Libri inseriti:")
libreria.mostra_libri()

libreria.aggiungi_vendite()
print("Libri con vendite:")
libreria.mostra_libri()

libreria.chiudi()