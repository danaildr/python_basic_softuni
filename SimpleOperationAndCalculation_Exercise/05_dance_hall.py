import math

room_lenght = float(input()) * 100
room_widht = float(input()) * 100
g_side = float(input()) * 100
room_area = room_lenght * room_widht
g_area = g_side * g_side
using_area = room_area * 0.9 - g_area
count_dancer = using_area / (40 + 7000)
print(math.floor(count_dancer))