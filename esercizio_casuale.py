import random
def indovina_il_numero():
    numero_casuale = random.randint(1,100)

    while True:
        numero_inserito = input("Indovina il numero (o digita 'esc' per terminare): ")
        if numero_inserito.lower() == "esc":
            print("hai terminato")
       
        numero_inserito = int(input("indovina il numero"))
        if numero_casuale == numero_inserito:
             print("hai vinto")
            break
        elif numero_inserito > numero_casuale:
            print("numero inserito più alto")
        else:
            print("numero inserito più basso")
        
indovina_il_numero()
