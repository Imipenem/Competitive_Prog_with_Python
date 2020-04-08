def maxProfit(prices) -> int:
    profit, idx = 0, 0
    length = len(prices)
    if length < 2: return profit

    while True:
        buy = prices[idx]
        idx += 1

        while idx < length and prices[idx] < buy:
            buy = prices[idx]
            idx += 1
            if idx >= length:
                return profit

        while idx < length and prices[idx] >= prices[idx-1]:
            idx += 1
        profit += (prices[idx-1] - buy)
        if idx >= length: return profit


if __name__ == '__main__':
    print(maxProfit([7,6,4,3,1]))