from math import pi
area = 0.0
figure = input()
if figure == "square":
  side = float(input())
  area = side * side
elif figure == "rectangle":
  side_a = float(input())
  side_b = float(input())
  area = side_a * side_b
elif figure == "circle":
  radius = float(input())
  area = pi * radius * radius
elif figure == "triangle":
  side = float(input())
  heigth = float(input())
  area = (side * heigth) / 2

print(f"{area:.3f}")
