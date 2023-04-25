
class Person:
    def __init__(self, a, b, c, d):
        self.vorname = a
        self.zuname = b
        self.alter_aussehen = c
        self.alter_ist = self.alter_aussehen
        self.beruf = d
    def ausgabe(self):
        print(self.vorname, self.zuname)

IchSelbst = Person("rene", "test", 27, "soldat")
IchSelbst.ausgabe()
