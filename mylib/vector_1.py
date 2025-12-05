class Vector:
    def __init__(self, x, y):
        """
        2-dimensionaler Vektor
        :param x: x-Komponente
        :param y: y-Komponente
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(other).__name__))

    def __rmul__(self, other):
        assert isinstance(other, (int, float))
        return Vector(other * self.x, other * self.y)

    def __abs__(self):
        return (self.x  ** 2 + self.y ** 2) ** 0.5

    def __len__(self):
        return len(self.__dict__.items())

    def distance(self, other):
        return abs(Vector(self.x - other.x, self.y - other.y))

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y