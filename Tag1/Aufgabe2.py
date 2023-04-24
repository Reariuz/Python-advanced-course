"""
Aufgabe 2:
    Schreiben Sie ein kleines Python-Programm, dass alle Zahlen ab 1 in
    Hexadezimalschreibweise ausgibt. Nach Ausgabe eines Blockes von 30 Zahlen
    soll der Anwender über eine Abfrage ("(w)eiter (e)nde") gefragt werden,
    ob er sich einen weiteren Block anzeigen lassen will oder ob das Programm
    beendet werden soll.
"""

a=1
while True:
    for i in range(a,a+30):
        print(hex(i))
    if input("Beenden(y)?") == 'y':
        break

    a += 30

