class Automobile: #dichiaro la classe
    
    numero_di_ruote = 4 #attributo di classe

    def __init__(self,marca, modello): #metodo costruttore #self riferito all'oggetto
            self.marca = marca #attributo di istanza

            self.modello = modello #attributo di istanza
    def stampa_info(self): #metodo di istanza
            print("L'automobile è una",self.marca,self.modello)

auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW","X3")

auto1.stampa_info()
auto2.stampa_info()

class Calcolatrice: #serve a creare un oggetto 
   
    @staticmethod
    def somma(a,b):
        return a+b
#uso del metodo statico senza creare un'istanza
risultato = Calcolatrice.somma(5,3) # i metodi statici si richiamano dalla classe e non dall'oggetto

print(risultato)

class Contatore:
    numero_istanze = 0 #attributo classe
    
    def __init__(self):
        Contatore.numero_istanze +=1
        
    @classmethod #permette alla classe di prendere se stesso come metodo
    def mostra_numero_istanze(cls): #cls si riferisce alla classe
        print(f"Sono state create {cls.numero_istanze} istanze.")

#creazione alcune istanze        
c1 = Contatore() 
c2 = Contatore()

Contatore.mostra_numero_istanze()
#output: sono state create 2 istanze 