#Findet eine Nullstelle in einem gewissen Interval
def bisect(func, a, b, epsilon):
   #Überprüft, ob die Eingaben korrekt sind
    assert a != b, f"Das Intervall darf nicht leer sein: a {a} == b {b}" # Schaut, ob die Bedingung a != b erfüllt ist, wenn nicht wird eine Fehlermeldung ausgegeben

    if func(a) == 0:
        return a
    elif func(b) == 0:
        return b

   # Schaut, ob die Bedingung a * b < 0 erfüllt ist, wenn nicht wird eine Fehlermeldung ausgegeben
    assert func(a) * func(b) < 0, f"Die Funktionswerte der Intervalle müssen ein unterschiedliches Vorzeichen haben. f({a}) = {func(a)}, f({b}) = {func(b)}"

    if a > b:
        a, b = b, a

    value_left = func(a)
    value_right = func(b)

    mid = (a + b) / 2
    value_mid = func(mid)
    counter = 0
    while abs(value_mid) > epsilon and (b - a) / 2 > epsilon:
#        print(mid)
        if value_left * value_mid < 0:
            b = mid
            value_right = value_mid
        else:
            a = mid
            value_left = value_mid

        mid = (a + b) / 2
        value_mid = func(mid)
        if value_mid == 0:
            return mid
        counter += 1
    return round(mid, 8)


# Findet alle Nullstellen in einem Intervall indem es das Intervall in kleinere Intervalle aufteilt und in jedem Intervall nach einer Nullstelle sucht
def zeros(func, links, rechts, delta = None, epsilon = 1.0e-9):
    if delta is None:
        delta = (abs(links) + rechts) / 1000
    assert links != rechts, f"Das Intervall der Funktion {func.__name__}darf nicht leer sein: a {links} == b {rechts} func: {func}"  # Schaut, ob die Bedingung a != b erfüllt ist, wenn nicht wird eine Fehlermeldung ausgegeben
    if links > rechts:
        links, rechts = rechts, links
    nullstellen = []
    left_value = links
    while left_value < rechts:
        if func(left_value) * func(left_value + delta) < 0:
            nullstellen.append(bisect(func, left_value, left_value + delta, epsilon))
        elif -epsilon < func(left_value) < epsilon:
            nullstellen.append(round(left_value,8))
        left_value += delta
    return nullstellen

def steigung(func, x, dx = 0.000001):
    dy = func(x + dx/2) - func(x - dx/2)
    return dy / dx

def minmax(func, links, rechts):
    return zeros(lambda x: steigung(func, x), links, rechts)

def maxima(func, links, rechts, epsilon=1.0e-8):
    minmax_values = minmax(func, links, rechts)
    maxima_elements = []
    for i in range(len(minmax_values)):
        if steigung(func, minmax_values[i] + epsilon) < steigung(func, minmax_values[i] - epsilon):
            maxima_elements.append(minmax_values[i])
    return maxima_elements

def minima(func, links, rechts, epsilon=1.0e-8):
    minmax_values = minmax(func, links, rechts)
    minima_elements = []
    for i in range(len(minmax_values)):
        if steigung(func, minmax_values[i] + epsilon) > steigung(func, minmax_values[i] - epsilon):
            minima_elements.append(minmax_values[i])
    return minima_elements
