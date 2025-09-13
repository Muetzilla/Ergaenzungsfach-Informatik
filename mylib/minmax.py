from mylib.zeros import zeros
def steigung(func, x, dx = 0.000001):
    dy = func(x + dx/2) - func(x - dx/2)
    return dy / dx

def minmax(func, links, rechts):
    return zeros(lambda x: steigung(func, x), links, rechts)

def minmax2(func, links, rechts):
    def steigung(x, dx=0.000001):
        dy = func(x + dx / 2) - func(x - dx / 2)
        return dy / dx
    return zeros(steigung, links, rechts)