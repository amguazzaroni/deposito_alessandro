import math
class Punto():
    
    def __init__(self,x, y): #metodo costruttore #self riferito all'oggetto
            self.x = x #attributo di istanza

            self.y = y #attributo di istanza
   
    def muovi(self,dx,dy): #metodo di istanza
            self.x += dx
            
            self.y += dy
    
    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)
    
p = Punto(3, 4)
print(p.distanza_da_origine())  # Output: 5.0

p.muovi(1, 2)
print(p.x, p.y)  # Output: 4 6
print(p.distanza_da_origine())  # Output: distanza aggiornata
