table_count = int(input())
table_lenght = float(input())
table_widht = float(input())
rectangle_area = table_count * (table_lenght + 2 * 0.30) * (table_widht + 2 * 0.30)
care_area = table_count * (table_lenght/2) * (table_lenght/2)
price_usd = (rectangle_area * 7) + (care_area * 9)
price_bgn = price_usd * 1.85
print(f'{price_usd:.2f} USD')
print(f'{price_bgn:.2f} BGN')