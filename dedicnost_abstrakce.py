from abc import ABC, abstractmethod

class Polygon(ABC):
    #abstraktní třída pro mnohoůhelník
    @abstractmethod
    def numofsides(self):
    #abstraktní metoda pro počet stran mnohoúhelíku
        pass

class Triangle(Polygon):
    def numofsides(self):
        print("Triangle has 3 sides")

class Pentagon(Polygon):
    def numofsides(self):
        print("Pentagon has 5 sides")

class Oktagon(Polygon):
    def numofsides(self):
        print("Oktagon has 8 sides")

t = Triangle()
t.numofsides()

p = Pentagon()
p.numofsides()

o = Oktagon()
o.numofsides()