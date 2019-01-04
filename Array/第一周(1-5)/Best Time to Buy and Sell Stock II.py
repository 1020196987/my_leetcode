class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_len = len(prices)
        profit_all = 0
        # 假设第一天的价格最小
        min_price = prices[0]
        for i in range(1, prices_len):
            if prices[i] > min_price:
                profit = prices[i] - min_price
                profit_all += profit
                min_price = prices[i]
            else:
                # 如果后面的没有比今天大的就卖了吧，并把当天设为最小值，即第二天再买入
                min_price = prices[i]

                # 并将当前卖出价格的后一天最为买入价格并设置为最小价格
        return profit_all


s = Solution()
# res = s.maxProfit([7, 1, 5, 3, 6, 4])
res = s.maxProfit([7, 6, 4, 3, 1])
# res = s.maxProfit([1, 2, 3, 4, 5])

print(res)
