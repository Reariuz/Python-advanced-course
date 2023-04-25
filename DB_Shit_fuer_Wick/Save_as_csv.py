import sqlite3
import os.path
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "finance.db")
with sqlite3.connect(db_path) as db:
#   conn = sqlite3.connect("finance.db")
    db.text_factory = str ## my current (failed) attempt to resolve this
    cur = db.cursor()
    data = cur.execute("SELECT * FROM Portfolio")

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    #writer.writerow(['Column 1', 'Column 2', ...])
    writer.writerows(data)
f.close()