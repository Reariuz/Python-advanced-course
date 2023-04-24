# Datenspeicher anlegen
datenspeicher = []

while True:
    person = []
    vorhanden = False
    i = 0

    # Person erfassen
    name = input("Name: ")
    groesse = float(input("Körpergröße: "))
    gewicht = int(input("Gewicht: "))

    # Bodymaß-Index berechnen
    bmi = gewicht / (groesse * 2)
    print("BMI: ", bmi)

    # Liste 'Person' erstellen
    person.append(name)
    person.append(groesse)
    person.append(gewicht)
    person.append(bmi)

    # Bewertung:
    if bmi >= 25:
        print("Übergewicht")
    elif bmi < 18.5:
        print("Untergewicht")
    else:
        print("Normalgewicht")

    # Datenspeicher aktualisieren
    # ####### Gucken, ob Person schon vorhanden #####
    for x in datenspeicher:
        if name in x[0]:
            vorhanden == True
            i = i + 1     #
    if not vorhanden:
        datenspeicher.append(person)
    else:
        datenspeicher.pop(i - 1)
        print("Person ist bereits vorhanden und wird aktualisiert")
        datenspeicher.append(person)

    # Ende?
    if (input("Beenden? q ") == "q"):
        break
       
print("Programmende")
print(datenspeicher)
