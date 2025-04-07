#es. 1
nome = input("Inserisci il tuo nome: ")
età = int(input("Inserisci la tua età: "))
altezza = int(input("Inserisci la tua altezza in cm: "))

if nome.lower() == "bob":
    if età >= 18:
        if altezza >= 175:
            print("daje, accesso consentito")
        else:
            print("Non puoi accedere: altezza insufficiente")
    else:
        print("Non puoi accedere: età insufficiente")
else:
    print("Non puoi accedere: nome non valido")

#es.2
lista = ["Pietro","Paolo","Giulia"]
scelta = input("inserisci un nome")

if scelta.lower() == "e":
    print(lista)
    scelta = input("scegli quale nome vuoi eliminare")
    lista.remove(scelta)
elif scelta == "a":
    print(lista)
    scelta = input("scegli quale nome vuoi aggiungere")
    lista.append(scelta)
elif scelta == "m":
    print(lista)
    scelta = int(input("scegli quale nome vuoi modificare"))
    scelta2 = input("dimmi cosa vuoi aggiungere")
    lista[scelta]=scelta2
    print(lista)
else:
    print("comando non riconosciuto")
    
#es.3
#creazione variabili
id=0
x = True

#condizioni
while x:
    #registrazione
    nome = ""
    password=""
    if x:
        nome = input("inserisci il tuo nickname")
        password = input("inserisci la tua password")
        id +=1
    #login
    if nome == "":
        print("non hai valorizzato")
    else:
        nome_inserito = input("inserisci il tuo nickname")
        password_inserita = input("inserisci la tua password")
        if nome_inserito == nome and password_inserita == password:
            print("sei loggato")
            