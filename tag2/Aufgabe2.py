"""
    Aufgabe 3

    Ein Schulungszentrum organisiert Schulungen für verschiedene
    Kurse. Eine Liste mit Neuanmeldungen liegt vor. Das Schulungszentrum
    hat bereits Schulungen für 1234 Personen durchgeführt. Für die bereits
    durchgeführten Schulungen gibt es ein Doictionary. (Da dieser Teil in
    dieser Aufgabe irrelevant ist, können Sie ein leeres Dictionary) erzeugen.
    
    a) Erstellen Sie eine statische Liste mit Namen der Neuanmeldungen, z.B.
    ["Otto Mueller", "Sandra Meyer", "Josef Schmidt", .....]

    b) Generieren Sie auf Basis der Länge Ihrer Liste dynamisch eine
    zweite Liste mit Nummern. Wenn Ihre erste Liste 20 Namen
    enthält, soll Ihre zweite Liste aus den Elementen 20 fortlaufenden (freien)
    Nummern bestehen: [1235, 1236, 1237, 1238, ....., 1253, 1254]

    c) Verknüpfen Sie beide Listen (verwenden Sie dafür die Sytemfunktion zip)

    d) Das Schulungszentrum bietet Kurse für Python, Java und Assembler an.
    Schreiben Sie eine Funktion "Kurszuweisung", die als Eingabeparameter ein
    Tupel (Name, Teilnehmernummer) bekommt, dazu den richtigen Kurs, für die
    die Anmeldung gelten soll, erfragt und daraus ein Dictionary der Form
    {Teilnehmernummer : (Name, Kurs)} befüllt

    e) Rufen Sie Ihre Funktion (die eigentlich ein Tupel erwartet)
    mit der kompletten Teilnehmerliste auf, verwenden Sie 'map'
    (Hinweis: Diese letzte Teilaufgabe hat ein paar Stolpersteine, sie ist
    'tricky', überlegen Sie sich genau, was zip und map genau
    machen und zurückliefern und wie Sie an die Werte herankommen)
    
"""




dict ={}
print()

def Seminarzuweisung(TN):
    print("Welchen Kurs soll", TN[1], "mit der Nummer", TN[0], "besuchen?\n")
    print("(1) Assembler\n(2) JAVA\n(3) Python\n")
    Selection = input()
    match Selection:
            Kurs = "Assembler"
        case "2":
            Kurs = "JAVA"
        case "3":
            Kurs = "Python"
    else:
        Kurs = "noch unbestimmt"
    Zuordnungen[TN[0]] = (TN[1], Kurs)
    return True 








# Lösung
Zuordnungen = {}

# d) Funktion für die Zuordung zu einem Kurs
def Seminarzuweisung(TN):
    print("Welchen Kurs soll", TN[1], "mit der Nummer", TN[0], "besuchen?\n")
    print("(1) Assembler\n(2) JAVA\n(3) Python\n")
    Selection = input()
    if Selection == "1":
        Kurs = "Assembler"
    elif Selection == "2":
        Kurs = "JAVA"
    elif Selection == "3":
        Kurs = "Python"
    else:
        Kurs = "noch unbestimmt"
    Zuordnungen[TN[0]] = (TN[1], Kurs)
    return True   

# a) Statische Liste
Teilnehmer = ["Otto Mueller", "Sandra Meyer", "Josef Schmidt"]

# b) Listenplätze berechnen
LetzteNummer = 1234
Nummern = []
for i in range(LetzteNummer + 1, LetzteNummer + len(Teilnehmer) + 1):
    Nummern.append(i)
LetzteNummer = LetzteNummer + len(Teilnehmer) 

# c) Listen mit zip verknüpfen
TNListeZIP = zip(Nummern, Teilnehmer)
TNListe = []
for Elem in TNListeZIP:
    TNListe.append(Elem)

# e) Funktion mit Liste verknüpfen
z = map(Seminarzuweisung, TNListe)
for Elem in z:
    pass

print (Zuordnungen)


    
