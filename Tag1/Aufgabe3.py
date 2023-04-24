"""
Aufgabe 3:
    Schreiben Sie ein Programm, dass das Geburtsdatum des Anwenders abfragt.
    Ist der Anwender volljährig, soll "unbeschränkter Zugang", ansonsten soll
    "eingeschränkter Zugang" ausgegeben werden.
"""
from datetime import date

GebDat = input("Wann wurden Sie geboren? TT.MM.JJJJ: ")
Day = int(GebDat[0:2])
Month = int(GebDat[3:5])
Year = int(GebDat[6:10])

today = date.today()
print(today.year - Year - ((today.month, today.day) < (Month, Day)))
if (today.year - Year - ((today.month, today.day) < (Month, Day))) >= 18:
    print("unbeschränkter Zugang")
else:
    print("eingeschränkter Zugang")