class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minPrice = prices[0]
        maxProfit = 0

        for price in prices:

            if minPrice > price:
                minPrice = price
            
            curProfit = price - minPrice

            if curProfit > maxProfit:
                maxProfit = curProfit

        return maxProfit
            


                    






            

