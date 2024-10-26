class Sorting: # definice třídy Sorting

  def __init__(self):
    # inicializace instanční vlastnosti cisla, prázdný list
    self.cisla = []
    # inicializace instanční vlastnosti smer na implicitní hodnotu řazení
    self.smer = "vzestupne" 

   # definice metody pro reřazení hodnot listu v zadaném směru
  def serad(self, seznam_cisel, smer = "vzestupne"):
    self.cisla = seznam_cisel
    if (smer == "vzestupne"):
      self.cisla.sort()
    elif (smer == "sestupne"):
      self.cisla.sort(reverse = True)

  def __str__(self):
    return str(self.cisla)

# vytvoření objektu cisla třídy Sorting
cisla = Sorting()
# seřazení zadaných hodnot pomocí metody serad
cisla.serad([25, 8, 17, 9, -1, 33, 16, 24, 5])
print(cisla) # zobrazení seřazených hodnot