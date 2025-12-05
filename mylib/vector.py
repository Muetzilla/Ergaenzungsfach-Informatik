class Vector2D:
    def __init__(self, x, y):
        """
        2-dimensionaler Vektor
        :param x: x-Komponente
        :param y: y-Komponente
        """
        self.x = x
        self.y = y

    def __repr__(self):
        "String-Darstellung für Maschinen, Repräsentation"
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self):
        "String-Darstellung für Menschen"
        return f"({self.x}, {self.y})"


    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.x * other, self.y * other)
        elif isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector2D' and '{}'".format(type(other).__name__))

    def __rmul__(self, other):
        assert isinstance(other, (int, float))
        return Vector2D(other * self.x, other * self.y)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self):
        return len(self.__dict__.items())

    def __iter__(self):
        yield self.x
        yield self.y

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise IndexError("Index out of range for Vector2D")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        else:
            raise IndexError("Index out of range for Vector2D")