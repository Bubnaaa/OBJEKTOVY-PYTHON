class Knihovna:    
    class Kniha:
        def __init__(self, nazev, autor, pocet_stran):
            self.__nazev = nazev
            self.__autor = autor
            self.__pocet_stran = pocet_stran

        def get_nazev(self):
            return self.__nazev

        def get_autor(self):
            return self.__autor
        
        def get_pocet_stran(self):
            return self.__pocet_stran
        
        def __str__(self):
            return f"Název knihy: {self.__nazev}: {self.__autor}: {self.__pocet_stran}"
        
    def __init__(self, jmeno) -> None:
        self.__jmeno = jmeno
        self.__knihovna = []

    def get_jmeno(self):
        return self.__jmeno
    
    def pridej_knihu(self, nazev, autor, pocet_stran):
        self.__knihovna.append(self.Kniha(nazev, autor, pocet_stran))

    def odeber_knihu(self, nazev):
        for k in self.__knihovna:
            if k.get_nazev() == nazev:
                self.__knihovna.remove(k)

    def vypis_knihy(self):
        return [str(kniha) for kniha in self.__knihovna]

aa = Knihovna("Knihovna")
aa.pridej_knihu("Kulička", "Guy de Maupassant", 215)
aa.pridej_knihu("Harry Potter", "J. K. Rowling", 400)
aa.pridej_knihu("Hobbit", "J. R. Tolkien", 400)
aa.pridej_knihu("Fahrenheit 451", "Ray Bradbury", 300)
aa.odeber_knihu("Kulička")

for k in aa.vypis_knihy():
    print(k)
