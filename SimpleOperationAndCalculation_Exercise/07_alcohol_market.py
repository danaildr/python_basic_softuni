wiskey_price = float(input())
rakia_price = wiskey_price / 2
wine_price = rakia_price - (0.4 * rakia_price)
beer_price = rakia_price - (0.8 * rakia_price)
beer =  float(input())
wine =  float(input())
rakia =  float(input())
wiskey =  float(input())

need_money = beer * beer_price + wine * wine_price + rakia * rakia_price + wiskey * wiskey_price

print(f'{need_money:.2f}')