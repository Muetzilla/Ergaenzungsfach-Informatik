from mylib.vector import Vector2D


counter = 0
def display(info=""):
    global counter
    counter = counter + 1
    print(f"--------------------\n\n#### {counter} #### {info}")


display("__init__")
a = Vector2D(2, 3)  # Instantiierung
b = Vector2D(-1, 3)  # Instantiierung

print("x-Wert von a: ", a.x)
print("y-Wert von a: ", a.y)

display("__str__")
print("a: ", a)  # Pretty Print - __str__
print("b: ", b)  # Pretty Print - __str__

display("__repr__")
print("a: ", repr(a))  # __repr__ Repräsentation
print("b: ", repr(b))  # __repr__ Repräsentation

display("Addition zweier Vektoren")
c = a + b  # Addition
print("c: ", c)

display("Subtraktion zweier Vektoren")
d = a - b  # Subtraktion
print("d: ", d)

display("Negation eines Vektors")
u = -a  # Negation
print("u: ", u)

display("Multiplikation eines Vektors mit einem Skalar von rechts __mul__")
e = a * 1.2  # Multiplikation mit einem Skalar
print("e: ", e)

display("Multiplikation eines Vektors mit einem Skalar von links: __rmul__")
f = 1.2 * a  # Multiplikation mit einem Skalar
print("f: ", f)

display("Skalarprodukt zweier Vektoren")
g = a * b  # Skalarprodukt
print("g: ", g)

display("Betrag (Länge) eines Vektors")
h = abs(a)  # Betrag des Vektors - Länge des Vektors
print("h: ", h)

display("Dimensionalität")
j = len(a)
print("j: ", j)

display("Das Skalarprodukt zweier senkrecht aufeinander stehender Vektoren ist 0.")
u = Vector2D(3, 1)
v = Vector2D(-1, 3)
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

display("Adress-Operator __getitem__")
print("Komponenten von u, Variante 2:", u)
for index in range(len(u)):
    print("Komponente", index, "=", u[index])

display("Adress-Operator __setitem__")
u[0] = 2
u[1] = -2
print("Neue Komponenten für u: ", u)