import math

def circleArea(radius):
    """
    Dient zur Berechung der Fläche eines Kreises
    :param radius: Der Radius des Kreises
    :return: Die Fläche des Kreises
    """
    area = math.pi * (radius ** 2)
    return area

def circleCircumference(radius):
    """
    Berechnet den Umfrang eines Kreises
    :param radius: Der Radius des Kreises
    :return: Den Umfang des Kreises
    """
    circumference = 2 * math.pi * radius
    return circumference

def sphereSurfaceArea(radius):
    """
    Berechnet den Oberflächeninhalt einer Kugel
    :param radius: Der Radius der Kugel
    :return: Den Oberflächeninhalt der Kugel
    """
    surfaceArea = 4 * math.pi * radius ** 2
    return surfaceArea

def cyliderSurfaceArea(radius_base, height):
    """
    Berechnet den Oberflächeninhalt eines Zylinders.
    :param radius_base:
    :param height:
    :return:
    """
    surfaceArea = 2 * circleArea(radius_base) + (circleCircumference(radius_base) * height)
    return surfaceArea

def cylinderVolume(radius_base, height):
    """
    Berechnet das Volumen eines Zylinders
    :param radius_base: Der Raduis des Kreises, welcher die Grundfläche des Zylinders bildet
    :param height: Die Höhe des Zylinders
    :return: Das Volumen des Zylinders
    """
    volume = circleArea(radius_base) * height
    return volume

def sphereVolume(radius):
    """
    Berechnet das Volumen einer Kugel
    :param radius: Der Radius der Kugel
    :return: Das Volumen der Kugel
    """
    volume = 4 * math.pi / 3 * radius ** 3
    return volume