class Tovarna:

    TypDarku = ["Autíčko", "Panenka", "Fotbalový míč", "Mobil", "Tablet", "Sluchátka"]

    def __init__(self, typ_darku):
        self.darek = typ_darku
        self.darky = []

    def vyrabej(self):
        return self.darek
    
    class Darek:
        def __init__(self, typ, pocet):
            self.typ = typ
            self.pocet = pocet

        def getTyp(self):
            return self.typ

        def getPocet(self):
            return self.pocet
        
    def vyrobDarek(self, typ, pocet):
        if typ not in Tovarna.TypDarku:
            print("Neplatný typ dárku")
        else:
            for i in range(pocet):
                self.darky.append((f"{typ}: {pocet}"))

    def GetDarky(self):
        return self.darky
    
darky = Tovarna("Dárky")
darky.vyrobDarek("Autíčko", 10)
darky.vyrobDarek("Panenka", 5)
darky.vyrobDarek("Fotbalový míč", 2)
darky.vyrobDarek("Mobil", 10)
darky.vyrobDarek("Tablet", 5)
darky.vyrobDarek("Sluchátka", 2)

print(f"{darky.vyrabej()} \n**********")
for i in darky.GetDarky():
    print(i)
