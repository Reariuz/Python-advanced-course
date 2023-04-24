"""
Aufgabe 1:
    Schreiben Sie ein kleines Python-Programm, dass alle Zahlen zwischen
    1 und 500, die entweder durch 7 oder durch 13 teilbar sind, am Bildschirm
    ausgibt.
"""


upper_int = 500

for i in range(upper_int):
    if (i % 7) == 0 or (i % 13) ==0:
        print(i)