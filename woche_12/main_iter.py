from mylib.liste_p31 import Knoten, Liste

k1 = Knoten(5, None)
k2 = Knoten(15, k1)
k3 = Knoten(25, k2)
liste = Liste(k3)

for knoten in liste:
    print(knoten)
