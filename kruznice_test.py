class Kruznice:
    pi = 3.14159265358979

    def __init__(self, d):
        self.d = d
        self.s = self.ma_obsah()
        self.o = self.ma_obvod()

    def ma_obsah(self):
        return Kruznice.pi * (0.5 * self.d) ** 2 

    def ma_obvod(self):
        return Kruznice.pi * self.d 

    def __str__(self):
        return f"Kružnice o průměru {self.d} má obvod {self.o:.2f} a obsah {self.s:.2f}."

k = Kruznice(10)
print(k)