"""
    Schreiben Sie ein Programm "Warenbestellung":
    -> Codieren Sie ein Dictionary mit diversen statischen Angaben
       wie z.B. {"Ottmar":"1234", "Josef":"34246"}
    -> Einer Person wird angeboten:
            -> Einloggen
            -> Neu registrieren
            -> Abbruch

       Falls sich der Anwender für Einloggen entscheidet, muss er
       einen Benutzernamen und ein Kennwort eingeben und dabei eine gültige
       Kombination aus dem Dictionary finden. Findet er diese nicht, ist
       eine Fehlermeldung auszugeben
    
       Falls sich der Anwender für "Neu registrieren" entscheidet,
       muss er sich zunächt für einen Benutzernamen entscheiden. Falls dieser
       Name im Dictionary bereits vorhanden ist, muss eine entsprechende
       Fehlermeldung ausgegeben werden, falls nicht, ist das Dictionary um
       den Benutzernamen und ein abzufragendes Kennwort zu erweitern.

       Falls Abbruch gewählt wird, terminiert das Programm.

       Hat der Anwender sich erfolgreich eingeloggt oder aber neu
       registriert, ist ein Hinweis "Programm wird ausgeführt" auszugeben
"""













# Lösung
Users = {"Ottmar":"1234", "Josef":"34567"}

while True:
    print("(e)inloggen\nneu (r)egistrieren\n(a)bbruch\n")
    Selection = input()
     
        Login    = input("Ihr Benutzername: ")
        Password = input("Ihr Kennwort:     ")
        Zugang = False
        key = (Login, Password)
        for keys in Users.items():
            if key == keys:
                Zugang = True
        if Zugang:
            print("Sie haben Zugang\n")
            break
        else:
            print("Benutzername oder Kennwort falsch\n")
            continue

    elif Selection == "r" or Selection == "R":
        Login    = input("Ihr Benutzername: ")
        Zugang = True
        for keys in Users:
            if keys == Login:
                Zugang = False
        if Zugang:
            Password = input("Ihr Kennwort:     ")
            Users[Login] = Password
            continue
            #break
        else:
            print("Der Benutzername ist bereits vorhanden")
            continue
    
    elif Selection == "a" or Selection =="A":
        break

    else:
        continue

    print("Es geht weiter")

print("Es geht im Hauptprogramm weiter")
print("Programm wird beendet")
    
