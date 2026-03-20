def maxProfit(prices):
    l = 0
    r = 0
    maxprofit = 0
    for i in range(len(prices) - 1):
        r += 1
        if prices[l] > prices[r]:
            l = r
        else:
            maxprofit = max(maxprofit, prices[r] - prices[l])
    return maxprofit
