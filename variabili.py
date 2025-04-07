# Variabili

#tipi numerici
intero = int(input("inserisci un intero"))
virgola =float(input("inserisci un numero con la virgola"))

#tipi semantici
stringa = input("inserisci una parola")

print(stringa[0])
print(stringa.lower())

#metodi incorporati per manipolazione stringhe
s = "Ciao, mondo!"

print(len(s))
print(s.upper())
print(s.split(','))
print(s.replace('mondo', 'universo'))

#Non c'è bisogno ci chr, python le riconosce da sè (non si utilizzerà mai)
#carattere = chr(input("inserisci una singola lettera"))

#booleani
x = 5
y = 10
z = 7
print(x > y and y > z)
print(x <y  or z > y)
print(not(x < y))

#liste

lista_dati1 = [1,2,3,4]
lista_dati2 = [1,"alessandro",True]
lista_dati3 = []

print(lista_dati1)
print(lista_dati1[2])
print(lista_dati2[1])
lista_dati1.sort()
print(lista_dati1)
