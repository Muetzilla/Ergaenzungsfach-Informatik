def create_counter(start=0, step=1):
    count = start
    def inc():
        nonlocal count
        count += step
        return count
    return inc

# Demo
c1 = create_counter()        # Start 0, Schritt 1
c2 = create_counter(10, 2)   # Start 10, Schritt 2
c3 = create_counter(100, 20)   # Start 10, Schritt 2

print(c1())  # 1
print(c1())  # 2
print(c2())  # 12
print(c1())  # 3
print(c3())
print(c3())
print(c3())


x = "global x"

def outer():
    x = "enclosing x"
    def inner():
        x = "local x"
        return x
    return inner()

print(outer())  # "local x"