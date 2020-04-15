
def maxProfit(prices) -> int:
    if not prices:
        return 0
    profit = 0
    for i in range(0, len(prices) - 1):
        if prices[i] < prices[i + 1]:
            temp = max(prices[i + 1:]) - prices[i]
            profit = max(profit, temp)

    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))