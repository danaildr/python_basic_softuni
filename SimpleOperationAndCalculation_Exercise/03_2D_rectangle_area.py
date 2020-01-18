x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

side_a = abs(x1 - x2)
side_b = abs (y1 - y2)
area = side_a * side_b
perimeter = 2 * (side_a + side_b)
print(f'{area:.2f}')
print(f'{perimeter:.2f}')