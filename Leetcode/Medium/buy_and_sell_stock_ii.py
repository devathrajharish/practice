# Say you have an array prices for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

def main():
    def buy_sell(prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[ i - 1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
    prices = [7,1, 5,3,6,4]
    print(buy_sell(prices))
if __name__ == '__main__':
    main()