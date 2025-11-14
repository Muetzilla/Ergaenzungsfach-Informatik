def count(bisZahl):
    if bisZahl == 1:
        print(bisZahl)
        return
    else:
        print(bisZahl)
        count(bisZahl - 1)
        return

def summe(n):
    if n == 1:
        return 1
    else:
        return n + summe(n - 1)

def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


count(10)
print("Summe: ",summe(10))
print("Fibonacci (Mit Index 0 beginnend): ",fibonacci(9))

