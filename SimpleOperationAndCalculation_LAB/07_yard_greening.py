area_for_work = float(input())
total_cost = area_for_work * 7.61
discount = total_cost * 0.18
finale_cost = total_cost - discount
print(f'The final price is:{finale_cost: .2f} lv.')
print(f'The discount is:{discount: .2f} lv.')