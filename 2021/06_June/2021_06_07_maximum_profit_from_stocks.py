# O(n) time complexity
# O(1) space complexity
def buy_and_sell(arr):
    # At most one buy and one sell
    bestProfit = 0
    bestBuy = 10**10 # whatever upper price limit you have
    bestSell = 0
    for day in arr:
        if day < bestBuy: 
            bestBuy = day
            bestSell = day
        if day > bestSell: bestSell = day
        bestProfit = max(bestProfit, bestSell - bestBuy)
    return bestProfit
  
print('Should be 5: {}'.format(buy_and_sell([9, 11, 8, 5, 7, 10])))
print('Should be 5: {}'.format(buy_and_sell([7, 1, 5, 3, 6, 4])))
print('Should be 0: {}'.format(buy_and_sell([7,6,4,3,1])))

