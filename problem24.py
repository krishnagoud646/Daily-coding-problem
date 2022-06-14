"""Given a array of numbers representing the stock prices of a company in chronological order, 
write a function that calculates the maximum profit you could have made from buying and selling that stock once. 
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
 since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
from collections import deque


def stock_max_profit(prices):
    max = 0
    prices = deque(prices)
    buy_price = prices.popleft()


    for price in prices:


        if price < buy_price:
            buy_price = price


        else:
            profit = price - buy_price


            if profit > max:
                max = profit


    if max:
        return max


prices = [9, 11, 8, 5, 7, 10]
max_profit = stock_max_profit(prices)
print(prices,"Max Profit:",max_profit)# return 5
