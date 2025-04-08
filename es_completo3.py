# Prende input dall'utente e crea una lista di numeri
input_utente = input("Inserisci una lista di numeri separati da spazi: ")
lista_numeri = input_utente.split(",")
numeri = [int(x) for x in lista_numeri]

# Stampa il quadrato di ciascun numero
for numero in numeri:
    quadrato = numero ** 2
    print(f"Il quadrato di {numero} è {quadrato}")
