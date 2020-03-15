class Solution(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        total = 0
        min_price = prices[0]
        for price in prices:
            # find the min so far
            min_price = min(price, min_price)

            # compare the new profit with current price and min price we saw
            # so far
            current_profit = price - min_price
            # find which profit is bigger current profit or the profit we
            # saw so far
            if current_profit > profit:
                profit = current_profit
                total += profit
                print("total: ", total)
            # profit = max(profit, current_profit)
        # print(total)
        return profit


prices = [7, 1, 5, 3, 6, 4]
obj = Solution()
result = obj.max_profit(prices)
print(result)
