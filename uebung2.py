
# die folgende Eigenschaften hat:
# Name = (Vorname, Zuname)
# Wohnort = (Straße, PLZ, Ort)
# Alter = zahl
# und über den Konstruktor sinnvoll gesetzt werden müssen.
# Außerdem gibt es die Methode 'Geburtstag', die dazu
# führt, dass das Alter einer Person sich um 1 erhöht.

# Erstellen Sie im 'Hauptprogramm' ein zwei Personen-Objekte und schaffen
# Sie einen Vergleich (>) die angibt, ob Person 1 älter ist, als Person 2

# Im Hauptprogramm soll ein Hinweis erscheinen, welche Person ein Spiel
# beginnt (nämlich die ältere Person)

# Rufen Sie Ihre Methode auf und gucken Sie, ob alles so funktioniert,
# wie Sie sich das wünschen.

class Person:
    name = ("leer", "unbekannt")
    wohnort = ("", "", "")
    #alter = 0

    def __init__(self, a, b, c):
        self.name = a
        self.wohnort = b
        self.alter = c   

    def __str__(self):
        return str(self.name[0]) + " " + str(self.name[1]) + " ist " + str(self.alter) + " Jahre alt"
        
    def Geburtstag(self):
        self.alter += 1
        print ("Glückwunsch zum Geburtstag")

    def __int__(self):
        return self.alter
    
    def __lt__(self, other):
        if self.alter > other.alter:
            return "Ich bin älter"
        else:
            return "der andere ist älter"

# Hauptprogramm
myself = Person(("max", "mueller"),
                ("Bahnhofstraße", "49439", "Steinfeld"), 23)

other = Person(("maya", "mueller"),
                ("Bahnhofstraße", "49439", "Steinfeld"), 11)


print(other < myself)



    
