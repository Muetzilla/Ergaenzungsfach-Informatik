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

  #  print(f"Nullstelle: {round(mid, 6)}")
    #print(f"Counter: {counter}")
    return round(mid, 8)


# Findet alle Nullstellen in einem Intervall indem es das Intervall in kleinere Intervalle aufteilt und in jedem Intervall nach einer Nullstelle sucht
def multi_zero_finder(func, a, b, epsilon):
    assert a != b, f"Das Intervall darf nicht leer sein: a {a} == b {b} func: {func}"  # Schaut, ob die Bedingung a != b erfüllt ist, wenn nicht wird eine Fehlermeldung ausgegeben
    if a > b:
        a, b = b, a
    nullstellen = []
    interval_size = round((abs(a) + b) / 10000, 9)
    left_value = a
    while left_value < b:
        if func(left_value) * func(left_value + interval_size) < 0:
            nullstellen.append(bisect(func, left_value, left_value + interval_size, epsilon))
        left_value += interval_size
    return nullstellen