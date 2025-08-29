import math

def circle_area(radius):
    """
    Dient zur Berechung der Fläche eines Kreises
    :param radius: Der Radius des Kreises
    :return: Die Fläche des Kreises
    """
    area = math.pi * (radius ** 2)
    return area

def circle_circumference(radius):
    """
    Berechnet den Umfrang eines Kreises
    :param radius: Der Radius des Kreises
    :return: Den Umfang des Kreises
    """
    circumference = 2 * math.pi * radius
    return circumference

def sphere_surface_area(radius):
    """
    Berechnet den Oberflächeninhalt einer Kugel
    :param radius: Der Radius der Kugel
    :return: Den Oberflächeninhalt der Kugel
    """
    surfaceArea = 4 * math.pi * radius ** 2
    return surfaceArea

def cylider_surface_area(radius_base, height):
    """
    Berechnet den Oberflächeninhalt eines Zylinders.
    :param radius_base:
    :param height:
    :return:
    """
    surfaceArea = 2 * circle_area(radius_base) + (circle_circumference(radius_base) * height)
    return surfaceArea

def cylinder_volume(radius_base, height):
    """
    Berechnet das Volumen eines Zylinders
    :param radius_base: Der Raduis des Kreises, welcher die Grundfläche des Zylinders bildet
    :param height: Die Höhe des Zylinders
    :return: Das Volumen des Zylinders
    """
    volume = circle_area(radius_base) * height
    return volume

def sphere_volume(radius):
    """
    Berechnet das Volumen einer Kugel
    :param radius: Der Radius der Kugel
    :return: Das Volumen der Kugel
    """
    volume = 4 * math.pi / 3 * radius ** 3
    return volume