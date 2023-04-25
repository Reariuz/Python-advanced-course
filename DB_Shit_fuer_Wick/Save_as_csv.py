import sqlite3
import os.path
import csv

# BASE_DIR ist eine variable die den dateifad dieser datei enthält
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# db_path ist der zusammengefügte pfad betriebsystemgerecht.
db_path = os.path.join(BASE_DIR, "finance.db")

#verbinde mit db
with sqlite3.connect(db_path) as db:

    #setzt cursor auf db
    cur = db.cursor()

    #Filter db per SQL string und speicher ergebniss
    data = cur.execute("SELECT * FROM Portfolio")

#öffne eine output.csv, wenn noch nicht da, erstelle mit schreibrechten und lege den handler in f ab
with open('output.csv', 'w', newline='') as f:

    #erstelle einen csv-schreiber in writer auf f
    writer = csv.writer(f)

    # schreibe die daten zeilenweise
    writer.writerows(data)

#schließe den shit
f.close()