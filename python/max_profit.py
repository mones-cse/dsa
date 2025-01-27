# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# historut 27/1/25 - 45 min
def max_profit(prices):
    maxProfit = 0
    l=0
    r=1
    if(len(prices)<2):
        return maxProfit
    
    while(r!=len(prices)):
        if (prices[l] >= prices[r]):
            l=r
            r=r+1
        else:
            profit = prices[r]-prices[l]
            maxProfit = profit if profit > maxProfit else maxProfit
            r=r+1

    return maxProfit
    


def max_profit_executor():
    print('max profit')
    print(max_profit([7,1,5,3,6,4,0])) # 5
    print(max_profit([7,6,4,3,1])) # 0
    print(max_profit([3,2,6,5,0,3])) # 4
    print(max_profit([2,1,2,1,0,1,2])) # 2
    print(max_profit([1])) # 0
    print(max_profit([1,2])) # 1
    print(max_profit([2,1])) # 0