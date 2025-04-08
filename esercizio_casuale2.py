# definisco la funzione
def fibonacci():
    n = int(input("Inserisci un numero: ")) # Chiedi all'utente di inserire un numero
    
    a, b = 0, 1 # Inizializza i primi due numeri della sequenza di Fibonacci

    while a <= n: # Finché il numero corrente è minore o uguale a N
        print(a)
        a, b = b, a + b
#richiamo funzione
fibonacci()