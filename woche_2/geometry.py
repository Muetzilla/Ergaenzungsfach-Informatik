import math


def circleArea(radius):
    area = math.pi * (radius ** 2)
    return area

def circleCircumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

def sphereSurfaceArea(radius):
    surfaceArea = 4 * math.pi * radius ** 2
    return surfaceArea

def cyliderSurfaceArea(radius_base, height):
    surfaceArea = 2 * circleArea(radius_base) + (circleCircumference(radius_base) * height)
    return surfaceArea

def cylinderVolume(radius_base, height):
    volume = circleArea(radius_base) * height
    return volume

def sphereVolume(radius):
    volume = 4 * math.pi / 3 * radius ** 3
    return volume


#Tests
radius = 3
height = 4

print(f"Die Fläche des Kreises bei Radius {radius} ist: {circleArea(radius)}")
print(f"Der Umfang des Kreises bei Radius {radius} ist: {circleCircumference(radius)}")
print(f"Die Fläche der Kugel bei Radius {radius} ist: {sphereSurfaceArea(radius)}")
print(f"Die Fläche des Zyliders bei Radius {radius} und Höhe {height} ist: {cyliderSurfaceArea(radius, height)}")
print(f"Das Volumen des Zyliders bei Radius {radius} und Höhe {height} ist: {cylinderVolume(radius, height)}")
print(f"Das Volumen der Kugel bei Radius {radius} ist: {sphereVolume(radius)}")


