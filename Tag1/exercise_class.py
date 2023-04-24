
# Defenition der Klasse
class Person:
  def __init__(self, Nachname, Vorname, PLZ, Ort, Straße, Alter ) :
      self.Nachname = Nachname
      self.Vorname = Vorname
      self.PLZ = PLZ
      self.Ort = Ort
      self.Straße = Straße
      self.Alter = Alter

# Defenition der Daten
  def Daten (self):
     print (self.Nachname, self.Vorname, self.PLZ, self.Ort, self.Straße, self.Alter)

# Defenition und Berechnung Alter +1
  def Geburtstag (self):
     self.Alter = self.Alter + 1

#Personen anlegen und Altersberechung Ausgabe
person = Person ("Steff", "Wick", "00001", "Schabernak", "Laufweg 1", 40 )
person1 = Person ("Rene", "Bruns", "24000", "Sasas", "Laufhaus 5", 27)
person2 = Person ("Zick", "Zack", "00001", "Sasas", "Laufhaus 20", 21)
person.Geburtstag()
person.Daten()
person1.Geburtstag()
person1.Daten()
person2.Geburtstag()
person2.Daten()

# Programmende