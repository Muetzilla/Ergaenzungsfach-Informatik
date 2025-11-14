from mylib import Liste, Knoten

#Beispiel 1.6 (Seite 23 - 26)
K3 = Knoten.Knoten(27, None, None)
K2 = Knoten.Knoten(13, K3)
K1 = Knoten.Knoten(7, K2)


folge = Liste.Liste(K1)
K3.naechster = K1

print(K3.naechster)
print(K3.naechster.naechster)
print(K3.naechster.naechster.naechster)
print(folge.anker.naechster.naechster.naechster)

#Übungsaufgaben 1.22 - 1.24




print("#############################")
X1 = Knoten.Knoten(1000, None)
X5 = Knoten.Knoten(44, X1)
X100 = Knoten.Knoten(86, X1)
X13 = Knoten.Knoten(10, X100.naechster)
X66 = Knoten.Knoten(38, X13)

folge = Liste.Liste(Knoten.Knoten(77, X66, None))
folge.vorherige_setzen()
print(folge.anker)
print(folge.anker.inhalt)
print(folge.anker==folge.anker.inhalt)
print(folge.anker.naechster)
print(folge.anker.naechster.naechster)
print(folge.anker.naechster.naechster.naechster)
print(folge.anker.naechster.naechster.naechster.naechster)
print(folge)
print("#############################")
print("#############################")
kn_1 = Knoten.Knoten(100, None)
kn_0 = Knoten.Knoten(100, kn_1)
drei = Liste.Liste(Knoten.Knoten(-7, kn_0))

print("Drei: ",drei)
print("#############################")
print("#############################")

Z1 = Knoten.Knoten(0,None)
Z0 = Knoten.Knoten(7, Z1)

X1 = Knoten.Knoten(6, Z0)
X0 = Knoten.Knoten(4, X1)

Y1 = Knoten.Knoten(5, Z0)
Y0 = Knoten.Knoten(3, Y1)

liste_x1 = Liste.Liste(X0)
liste_y1 = Liste.Liste(Y0)

print("Liste 1:", liste_x1)
print("Liste 2:", liste_y1)
print("#############################")
print("#############################")
print("Neunen Knoten einfach via Liste hizufügen:")

liste_x1.add_element(Knoten.Knoten(1234, None, None))
liste_x1.vorherige_setzen()
print("New Liste X1: ", liste_x1)
print("#############################")
print("Neunen Knoten einfach via Knoten hizufügen:")

liste_y1.add_element_via_knoten(Knoten.Knoten(4321, None, None))
liste_y1.vorherige_setzen()
print("New Liste Y1: ", liste_y1)
print("#############################")



#Erarbeitung von Beispiel 1.7

#Implementierung von __str__ in Klasse Liste (soll alle Knoten in der Reihenfolge ihrer Verkettung anzeigen, d.h. -7-13-27-):
K3.naechster = None
print(folge)

#Implementierung von findeLetzten() in Klasse Liste (Inhalt des letzten Knotens, hier 27):
print("Inhalt des letzten Knotens:",folge.findeLetzten())

print("#############################")

knoten_3 = Knoten.Knoten(12, None)
knoten_2 = Knoten.Knoten(6, knoten_3)
knoten_1 = Knoten.Knoten(3, knoten_2)
knoten_0 = Knoten.Knoten(-3, knoten_1)
liste26 = Liste.Liste(Knoten.Knoten(-4, knoten_0, None))
liste26.vorherige_setzen()
print("Liste 26: ", liste26)
print("#############################")
print("#############################")

print("Der gefundene Knoten:", liste26.suchen(6))
print("Der gefundene Knoten:", liste26.suchen(-4))
print("Der gefundene Knoten:", liste26.suchen(633))
print("#############################")
print("#############################")
print("Liste 26 alle Elemente: ", liste26)
liste26.entfernen(6)
print("Liste 26 knoten 2 entfernt: ", liste26)
print("#############################")
print("#############################")
print("Liste 26 alle Elemente: ", liste26)
liste26.einfuegen(Knoten.Knoten(11, None))
liste26.einfuegen(Knoten.Knoten(-11, None))
liste26.einfuegen(Knoten.Knoten(1, None))
liste26.einfuegen(Knoten.Knoten(8, None))
liste26.einfuegen(Knoten.Knoten(8, None))
print("Liste 26 eingefügter Knoten: ", liste26)
print("#############################")
print("#############################")
print("Liste 26 iter: ", liste26.__iter__())
for i in liste26:
    print("Iterator Element: ", i)

print("#############################")











#Implementierung von append(inhalt) (am Schluss der Liste hinzufügen):
# folge.append(10)
# print(folge)


#Aufgabe 1.27: Implementierung von suchen(inhalt):
# print("Gefundener Knoten:", folge.suchen(10))


#Aufgabe 1.28: Implementierung von entfernen(inhalt):
# folge.entfernen(27)
# folge.entfernen(13)
# print(folge)

#Aufgabe 1.29: Implementierung einfuegen(inhalt) unter Erhaltung der Ordnung:
# folge.einfuegen(9)
# print(folge)


#Zusatzaufgabe (siehe Punkt 15 in der Aufgabenliste auf Teams): Liste mit Iterator traversieren
# print("Liste mit for-loop traversieren")
# for i in folge:
#     print(i)

#Aufgabe 1.30: Doppelt verkettete Liste