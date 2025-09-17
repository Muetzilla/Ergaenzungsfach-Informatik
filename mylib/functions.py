import numpy as np
def func1(x):
    """
        -2x - 3
    """
    return -2 * x - 3

def func2(x):
    """
        x^2 - 4
    """
    return x ** 2 - 4

def func3(x):
    """
        x^3 - 2x
    """
    return x ** 3 - 2 * x

def func4(x):
    """
        0.2 * x^4 - x^2 + 1
    """
    return 0.2 * x ** 4 - x ** 2 + 1

def func5(x):
    """
    3 * e^(-x) * x^2
    """
    return 3 * np.exp(-x) * x ** 2

def sin(x):
    """
    sin(x)
    """
    return np.sin(x)

def func6(x):
    """
    x^2
    """
    return x ** 2

def func7(x):
    """
    x^3 - 7x + 1
    """
    return x ** 3 - 7 * x + 1

def funcSPAMM(x):
    """
    e^x - x^2
    """
    return np.exp(x) - x ** 2

def funcSPAMM2(x):
    """
    2 * sin(x) + e^x
    """
    return 2 * np.sin(x) + np.exp(x)
