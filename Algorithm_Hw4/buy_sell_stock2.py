#if no profit return 0
# Example : prices = [7,1,5,3,6,4] Return: 7
# the stock is sold fof the best price in future
# buy and sell stock as many times as you want to
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price=6), profit = 6-1   = 5


def buy_sell_stock(prices):
    maximum = 0
    for i in range(len(prices) - 1):
        if prices[i+1] > prices[i]:
            maximum = maximum + prices[i + 1] - prices[i]

    return maximum

prices_list = [7,1,5,3,6,4]
result = buy_sell_stock(prices_list)
print(result)
