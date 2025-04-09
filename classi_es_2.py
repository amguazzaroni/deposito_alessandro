#classe libro
class Libro():
    def __init__(self,titolo,autore,pag):
        self.titolo  = titolo
        self.autore = autore
        self.pag = pag
        
    def stampa (self):
        print(self.titolo)
        print(self.autore) 
        print(self.pag)

#menu per la gestione del libro
while True:
    titolo = input("inserisci il titolo")
    autore = input("inserisci l'autore")
    nr_pag = int(input("inserisci il numero pagine"))
    
    Libro_mio = Libro(titolo, autore, nr_pag)
    Libro_mio.stampa()
    
    scelta_ciclo = ("vuoi ripetere?")
    if scelta_ciclo.lower == "si":
        continue
    else:
        break
    
class Biblioteca():
    def __init__(self):
        self.libri=[]
    
    def aggiungi_libro(self, titolo, autore, pag):
        nuovo_libro = Libro(titolo, autore, pag)
        self.libri.append(nuovo_libro)
        
    def stampa_libri(self):
        for x in self.libri:
            x.stampa()
            
biblio = Biblioteca()
biblio.aggiungi_libro("Ferrari", "charles le clerc", 100)
biblio.aggiungi_libro("Mercedes", "lewis", 200)
biblio.stampa_libri()