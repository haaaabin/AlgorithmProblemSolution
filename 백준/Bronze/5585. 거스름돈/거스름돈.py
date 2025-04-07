n = int(input())

coins = [500, 100, 50, 10, 5, 1]
money = 1000 - n

count = 0
for coin in coins:
    if money >= coin:
        count += money //coin
        money = money % coin

print(count)