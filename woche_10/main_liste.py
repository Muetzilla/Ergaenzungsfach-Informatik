from mylib import Liste, Knoten

#Beispiel 1.6 (Seite 23 - 26)
K3 = Knoten.Knoten(27, None)
K2 = Knoten.Knoten(13, K3)
K1 = Knoten.Knoten(7, K2)


folge = Liste.Liste(K1)
K3.naechster = K1

print(K3.naechster)
print(K3.naechster.naechster)
print(K3.naechster.naechster.naechster)
print(folge.anker.naechster.naechster.naechster)

#Übungsaufgaben 1.22 - 1.24

#Erarbeitung von Beispiel 1.7

#Implementierung von __str__ in Klasse Liste (soll alle Knoten in der Reihenfolge ihrer Verkettung anzeigen, d.h. -7-13-27-):
K3.naechster = None
print(folge)

#Implementierung von findeLetzten() in Klasse Liste (Inhalt des letzten Knotens, hier 27):
print("Inhalt des letzten Knotens:",folge.findeLetzten())

#Implementierung von append(inhalt) (am Schluss der Liste hinzufügen):
folge.append(10)
print(folge)


#Aufgabe 1.27: Implementierung von suchen(inhalt):
print("Gefundener Knoten:", folge.suchen(10))


#Aufgabe 1.28: Implementierung von entfernen(inhalt):
folge.entfernen(27)
folge.entfernen(13)
print(folge)

#Aufgabe 1.29: Implementierung einfuegen(inhalt) unter Erhaltung der Ordnung:
folge.einfuegen(9)
print(folge)


#Zusatzaufgabe (siehe Punkt 15 in der Aufgabenliste auf Teams): Liste mit Iterator traversieren
print("Liste mit for-loop traversieren")
for i in folge:
    print(i)

#Aufgabe 1.30: Doppelt verkettete Liste