from mylib.vector_1 import Vector

a = Vector(2, 3)  # Instantiierung
b = Vector(-1, 3)  # Instantiierung

print("x-Wert von a: ", a.x)
print("y-Wert von a: ", a.y)
print("a: ", a)  # Pretty Print - __str__
print("b: ", b)  # Pretty Print - __str__


c = a + b  # Addition
print("c: ", c)

d = a - b  # Subtraktion
print("d: ", d)

y = Vector(-3, 5)
z = Vector(-3, 5)

print(f"Die Vektoren y: {y} und z: {z} sind: ",  {True: "gleich", False: "verschieden"}[y == z])
if y == z:
    print("y und z sind gleich")
else:
    print("y und z sind ungleich")




u = -a  # Negation
print("u: ", u)

e = a * 1.2  # Multiplikation mit einem Skalar
print("e: ", e)

f = 1.2 * a  # Multiplikation mit einem Skalar
print("f: ", f)

g = a * b  # Skalarprodukt
print("g: ", g)

h = abs(a)  # Betrag des Vektors - Länge des Vektors
print("h: ", h)

# print(a * "Hallo")  # TypeError
j = len(a)
print("j: ", j)

u = Vector(3, 1)
v = Vector(-1, 3)
w = u * v

print("u: ", u)
print("v: ", v)
print("w: ", w)



# print("Wieso ist der letzte Wert 0?")
# print("Weil u und v senkrecht aufeinander stehen!")