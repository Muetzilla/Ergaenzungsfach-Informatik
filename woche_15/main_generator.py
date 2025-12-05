def foo():
    print("Hallo")
    yield 10
    print("Servus")
    yield 20
    print("Ciao")
    yield 30
    print("Welt")


print(type(foo))


g = foo()

print(g)
print(type(g))

print("--------------------")

x = next(g)
print('= side effect')
print(x, x, x)
x = next(g)
print('= side effect')
print(x, x, x)

print("--------------------")

for x in foo():
    print(x)

print("--------------------")

for num, x in enumerate(foo()):
    print(num, x, x, x)

print("--------------------")

x = next(g)
print('= side effect')
print(x, x, x)

print("--------------------")
from collections.abc import generator
print(isinstance(g, generator))

