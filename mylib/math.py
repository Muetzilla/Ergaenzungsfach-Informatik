def ifac(num):
    """
    Iterative Berechnung der Fakultät
    :param num: Die Zahl, von der die Fakultät berechnet werden soll
    :return:  Die Fakultät der Zahl
    """
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def rfac(num):
    """
    Rekursive Berechnung der Fakultät
    :param num: Die Zahl, von der die Fakultät berechnet werden soll
    :return:  Die Fakultät der Zahl
    """
    if num == 1:
        return 1
    else:
        return num * rfac(num - 1)