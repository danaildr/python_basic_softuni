days = int(input())
worker = int(input())
cake = int(input())
gofrete = int(input())
pancake = int(input())
one_worker_cake_price = cake * 45
one_worker_gofrete_price = gofrete * 5.80
one_worker_pancake_price = pancake * 3.20
one_day_price = worker * (one_worker_cake_price + one_worker_gofrete_price + one_worker_pancake_price)
finale_price = one_day_price * days * 7 / 8

print(f'{finale_price:.2f}')