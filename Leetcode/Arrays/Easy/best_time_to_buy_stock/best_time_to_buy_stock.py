class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_prof = 0
        for i in prices[1:]:
            if max_prof < (i - min_price):
                max_prof = i - min_price
            if min_price > i:
                min_price = i
        return max_prof