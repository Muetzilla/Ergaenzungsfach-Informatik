from geometry import circleArea, circleCircumference, sphereVolume, sphereSurfaceArea, cyliderSurfaceArea, cylinderVolume

#Tests
radius = 3
height = 4

print(f"Die Fläche des Kreises bei Radius {radius} ist: {circleArea(radius)}")
print(f"Der Umfang des Kreises bei Radius {radius} ist: {circleCircumference(radius)}")
print(f"Die Fläche der Kugel bei Radius {radius} ist: {sphereSurfaceArea(radius)}")
print(f"Die Fläche des Zyliders bei Radius {radius} und Höhe {height} ist: {cyliderSurfaceArea(radius, height)}")
print(f"Das Volumen des Zyliders bei Radius {radius} und Höhe {height} ist: {cylinderVolume(radius, height)}")
print(f"Das Volumen der Kugel bei Radius {radius} ist: {sphereVolume(radius)}")


