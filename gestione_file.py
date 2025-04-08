#lettura file
file = open("esempio_testo.txt","r") #apertura in modalità lettura
riga = file.readline()
tutte_le_righe = file.read()
print(tutte_le_righe)
file.close()

#scrittura file (sovrascrittura oppure se non esiste il file lo crea)
file = open("esempio_testo.txt","w")
file.write("alpha, beta, gamma")
file.close()

# with permette di aprire e chiudere automaticamente MA non si può mix w/r
with open("esempio_testo_nuovo.txt","w") as file:
    file.write("daje Roma")

#Aggiunta testo
file = open("esempio_testo.txt","a")
file.write("alpha, beta, gamma")
file.close()   