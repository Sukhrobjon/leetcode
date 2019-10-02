class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # find the min number
        # and find the max number after min num's index
        # if there is no one return 0 else return 
        # max - min
        # if not prices:
        #     return 0
        # min = [prices[0], 0]
        # for i, price in enumerate(prices):
        #     if price < min[0]:
        #         min = [price, i]
        # buy, location = min[0], min[1]

        # # if buy is last day then we cant sell it anymore
        # if buy == prices[-1]:
        #     return 0
        # # find the max price from rest of the min price
        # sell = max(prices[location+1:])

        # profit = sell - buy
        # return profit if profit > 0 else 0
        if not prices:
            return 0
        profit = 0
        min_price = prices[0]
        for price in prices:
            # find the min so far
            min_price = min(price, min_price)

            # compare the new profit with current price and min price we saw
            # so far
            current_profit = price - min_price
            # find which profit is bigger current profit or the profit we
            # saw so far
            profit = max(profit, current_profit)

        return profit


prices = []
obj = Solution()
result = obj.max_profit(prices)
print(result)
