from geometry import circle_area, circle_circumference, sphere_volume, sphere_surface_area, cylider_surface_area, cylinder_volume

#Tests
radius = 3
height = 4

print(f"Die Fläche des Kreises bei Radius {radius} ist: {circle_area(radius)}")
print(f"Der Umfang des Kreises bei Radius {radius} ist: {circle_circumference(radius)}")
print(f"Die Fläche der Kugel bei Radius {radius} ist: {sphere_surface_area(radius)}")
print(f"Die Fläche des Zyliders bei Radius {radius} und Höhe {height} ist: {cylider_surface_area(radius, height)}")
print(f"Das Volumen des Zyliders bei Radius {radius} und Höhe {height} ist: {cylinder_volume(radius, height)}")
print(f"Das Volumen der Kugel bei Radius {radius} ist: {sphere_volume(radius)}")


