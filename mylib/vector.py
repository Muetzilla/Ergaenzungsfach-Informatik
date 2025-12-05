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

class Vector3D:
    def __init__(self, x, y, z):
        """
        2-dimensionaler Vektor
        :param x: x-Komponente
        :param y: y-Komponente
        :param z: z-Komponente
        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        "String-Darstellung für Maschinen, Repräsentation"
        return f"Vector2D({self.x}, {self.y}, {self.z})"

    def __str__(self):
        "String-Darstellung für Menschen"
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector3D(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector3D' and '{}'".format(type(other).__name__))

    def __rmul__(self, other):
        assert isinstance(other, (int, float))
        return Vector3D(other * self.x, other * self.y, other * self.z)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __len__(self):
        return len(self.__dict__.items())

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("Index out of bounds for Vector3D")

    def __setitem__(self, key, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise IndexError("Index out of bounds for Vector3D")

def cross(self, other):
    cx = self.y * other.z - self.z * other.y
    cy = self.z * other.x - self.x * other.z
    cz = self.x * other.y - self.y * other.x
    return Vector3D(cx, cy, cz)

def unit(self):
    length = abs(self)
    if length == 0:
        raise ValueError("Cannot compute unit vector of zero vector")
    return Vector3D(self.x / length, self.y / length, self.z / length)