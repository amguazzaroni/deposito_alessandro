#if-else
numero = -10
if numero > 0:
    print("il numero è positivo")
else:
    print("Blocco Else")
    
#elif
numero = -10
if numero > 0:
    print("il numero è positivo")
    if numero == 100:
        print("wow")
elif numero < 0:
    print("il numero è negativo")
else:
    print("Blocco Else")

stringa = input("inserisci il tuo nome")
if stringa.lower() == "mirko":
    print("wow")
    
    