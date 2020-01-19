vacantion_price = float(input())
pusles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
mini_trucks = int(input())

toys = pusles + dolls + bears + minions + mini_trucks
money_earned = pusles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + mini_trucks * 2

if toys >= 50:
  money_earned = money_earned - (money_earned * 0.25)
money_earned = money_earned - (money_earned * 0.1)
finale_money = abs(money_earned - vacantion_price)
if money_earned >= vacantion_price:
  print(f"Yes! {finale_money:.2f} lv left.")
else:
  print(f"Not enough money! {finale_money:.2f} lv needed.")
