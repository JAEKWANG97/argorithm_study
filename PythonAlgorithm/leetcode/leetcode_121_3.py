prices = [7,1,5,3,6,4]

def maxProfit(prices: list):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print(maxProfit(prices))
# 포문 돌리면서 제일 낮은건지 체크 하고, max를 찾아야함