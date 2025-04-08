#semantica funzioni
def nome_della_funzione():
    pass

#funzione di esecuzione
def saluta(nome):
    print("ciao",nome)
    
saluta("ciao")

#funzioni con parametri
def somma(x,y):
    risultato=x+y
    print(risultato)

somma(1,2)

#funzione di ritorno
def riporta_dato(x):
    return x*x

numero = riporta_dato(3)
print(numero)

somma(riporta_dato(3),riporta_dato(3))

#variante funzione di ritorno
def riporta_dato_senza_parametri():
    x=int(input("numero da elevare a potenza"))
    return x*x

#funzione con parametri standard 

def funzione_standard(x=1):
    return x+x