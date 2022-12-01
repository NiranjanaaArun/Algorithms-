#if no profit return 0
# Example : prices = [7,1,5,3,6,4] Return: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price=6), profit = 6-1   = 5
# the stock is sold fof the best price in future
def buy_sell_stock(prices):
    max_sum = 0
    curr_sum = 0

    for i in range(len(prices) - 1):
        curr_sum = curr_sum + prices[i+1] - prices[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0

    return max_sum

prices = [7, 1, 5, 3, 6, 4]
result = buy_sell_stock(prices)
print(result)


