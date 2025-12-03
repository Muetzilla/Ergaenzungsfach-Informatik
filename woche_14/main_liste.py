from mylib.list_template import Liste, Knoten

kids = Liste()

kids.anhaengen("Lia")
kids.anhaengen("Mia")
kids.anhaengen("Pia")
kids.anhaengen("Leo")
kids.anhaengen("Max")

print("Kids: ", kids)
print("Anzahl Kids: ", len(kids))

kids.anhaengen("Tom")
print("Kids: ", kids)
print("Anzahl Kids: ", len(kids))

knoten = kids.finde_knoten(3)
print("Kind im Knoten 3: ", knoten.inhalt)

kid = kids[3]
print("Kind mit Index 3: ", kid)

kid = kids[0]
print("Kind mit Index 0: ", kid)

kids[3] = "Lea"
print("Kids: ", kids)

kids.einfuegen(0, "Leo")
print("Kids: ", kids)

kids.einfuegen(3, "Kai")
print("Kids: ", kids)

kids.einfuegen(3, "Jan")
print("Kids: ", kids)
print("Anzahl Kids: ", len(kids))

for index, kid in enumerate(kids):
    print("Kind", index + 1, ":", kid)