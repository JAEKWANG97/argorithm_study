# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라 

prices = [7,1,5,3,6,4]

# 출력 5

# 설명 1일 떄 사서 6일 때 팔면 5의 이익을 얻는다.

# 근데 이거 스택으로 풀 수 있을 것 같음

# print(prices[6:])
# print(max(prices[6:]))


def maxProfit(prices:list):
    profit = [0]
    for i in range(0,len(prices)):
        if prices[i] >= max(prices[i:]):
            continue
        else:
            profit.append(max(prices[i:]) - prices[i])
    max_profit = max(profit)
    return max_profit


print(maxProfit(prices))


