"""
    Aufgabe 2
    Erweitern Sie das Beispiel aus Aufgabe 1

    Erzeugen Sie im Hauptprogramm ein zweites Objekt.

    Sorgen Sie dafür, dass die Methode "ausgabe" nicht nur Namen,
    sondern auch Ist-Alter und Beruf ausgibt. Achten Sie auf die
    exakte Form "'Vorname' 'Zuname', 'x' Jahre alt, 'Beruf'", d.h.
    beachten Sie Leerzeichen und Kommata bei der Ausgabe.

    Sorgen Sie weiter dafür, dass ein Print-Befehl (print("Objekt"))
    zu Ausgabe von "'Zuname', 'Vorname'" führt.

    Führen Sie einen Vergleich durch, was sagt das System, wenn Sie
    Objekte 'Person_1 > Person_2' prüfen und warum ist das so? 
"""
class Person:
    def __init__(self, a, b, c, d):
        self.vorname = a
        self.zuname = b
        self.alter_aussehen = c
        self.alter_ist = self.alter_aussehen
        self.beruf = d
    def __str__(self):
        return(self.zuname + ", " + self.vorname)
    def ausgabe(self):
        print(self.vorname + " " + self.zuname + ",", self.alter_ist,
              "jahre alt,", self.beruf)

 dödel = person("rene","bruns",13,"soldat")   









IchSelbst = Person("rene", "test", 27, "soldat")
IchSelbst.ausgabe()
