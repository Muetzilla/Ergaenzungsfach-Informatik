from mylib.vector import Vector3D, cross, unit

counter = 0
def display(info):
    global counter
    counter = counter + 1
    print(f"--------------------\n\n#### {counter} #### {info}")

display("__init__")
a = Vector3D(2, 3, 0)  # Instantiierung
b = Vector3D(-1, 3, 1)  # Instantiierung

print("x-Wert von a: ", a.x)
print("y-Wert von a: ", a.y)

display("__str__")
print("a: ", a)  # Pretty Print - __str__
print("b: ", b)  # Pretty Print - __str__

display("__repr__")
print("a: ", repr(a))  # __repr__ Repräsentation
print("b: ", repr(b))  # __repr__ Repräsentation

display("Addition")
c = a + b  # Addition
print("c: ", c)

display("Subtraktion")
d = a - b  # Subtraktion
print("d: ", d)

display("Negation")
u = -a  # Negation
print("u: ", u)

display("Multiplikation mit einem Skalar (einer Zahl) von rechts")
e = a * 1.2  # Multiplikation mit einem Skalar
print("e: ", e)

display("Multiplikation mit einem Skalar (einer Zahl) von links")
f = 1.2 * a  # Multiplikation mit einem Skalar
print("f: ", f)

display("Skalarprodukt")
g = a * b  # Skalarprodukt
print("g: ", g)

display("Betrag des Vektors (Länge)")
h = abs(a)  # Betrag des Vektors - Länge des Vektors
print("h: ", h)

display("Dimensionalität des Vektors")
j = len(a)
print("j: ", j)

display("Skalarprodukt für zwei Vektoren ist 0, wenn sie senkrecht aufeinander stehen")
u = Vector3D(3, 1, 0)
v = Vector3D(-1, 3, 0)
w = u * v

print("u: ", u)
print("v: ", v)
print("w: ", w)
print("Wieso ist der letzte Wert 0?")
print("Weil u und v senkrecht aufeinander stehen!")

display("__iter__")
print("Komponenten von u, Variante 1:", u)
for index, komponente in enumerate(u):
    print("Komponente", index, "=", komponente)

display("Addressoperator - __getitem__")
print("Komponenten von u, Variante 2:", u)
for index in range(len(u)):
    print("Komponente", index, "=", u[index])

display("Adress-Operator __setitem__")
u[0] = 2
u[1] = -2
u[2] = 22
print("Neue Komponenten für u: ", u)

display(""" Das Vektorprodukt zweier Vektoren ist selbst ein Vektor. 
 Es steht immer senkrecht auf jeden der beiden.
 Deshalb sollte das Folgende Null ergeben.""")

ergebnis = u * cross(u, v)
print("u * cross(u, v) =", ergebnis)

display("Das ganze nochmal schrittweise")
print("u = ", u)
print("v = ", v)
x = cross(u, v)
print("cross(u, v) = ", x)
print("u * cross(u, v) = ", u * x)

display("Einheitsvektor")
e = unit(v)
print("Einheitsvektor von u =", u, ": e(u) =", e)

display("Die Länge eines Einheitsvektors ist immer 1.0")
print("Länge von e = ", abs(e))
