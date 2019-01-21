class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        # arr = []
        # arr_max_list = []
        #
        # for i, i_v in enumerate(prices):
        #     for j, j_v in enumerate(prices[i:]):
        #         arr.append(j_v - i_v)
        #     arr_max_list.append(max(arr))
        #     arr.clear()
        # return max(arr_max_list)
        #
        # for i in range(len(prices)):
        #     arr_max_list.append(max(prices[i:]) - prices[i])
        # return max(arr_max_list)

        # 解题思路：以当前价格为参考点，找到此价格之前的最小值，然后做差即为最大利润。
        minprice = float('inf')
        maxprice = 0
        for price in prices:
            minprice = min(minprice, price)
            # print(minprice)
            profit = price - minprice  # 遍历到此时price的最大利润
            maxprice = max(maxprice, profit)
        return maxprice


s = Solution()
res = s.maxProfit([7, 1, 5, 3, 6, 4])
print(res)
