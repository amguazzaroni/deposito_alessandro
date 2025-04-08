while True: #affinchè la condizione rimane True
    numero = int(input("Inserisci un numero per il conto alla rovescia: "))

    for i in range(numero, -1, -1): #start: numero inserito da utente, end: 0, passo: -1
        print(i)

    ripeti = input("Vuoi ripetere?: ").lower()
    if ripeti == 'si':
        continue
    else:
        print("Programma terminato.")
        break

