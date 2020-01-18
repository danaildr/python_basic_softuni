tank_x = int(input())
tank_y = int(input())
tank_z = int(input())
persect_bussi = float(input())

tank_capacity = tank_x * tank_y * tank_z * 0.001
water_capacity = tank_capacity * (1 - (persect_bussi  * 0.01))
print(f'{water_capacity:.3f}')

