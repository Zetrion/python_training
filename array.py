prices = [7, 1, 5, 3, 6, 4]
profit = 0
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        _profit = prices[j] - prices[i]
        if _profit > profit:
            profit = _profit
print(profit)

