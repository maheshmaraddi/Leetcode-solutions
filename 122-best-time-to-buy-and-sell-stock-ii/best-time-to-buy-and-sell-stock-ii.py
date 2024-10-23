class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        # Traverse the prices array
        for i in range(1, len(prices)):
            # Add the profit if there's a price increase from day i-1 to day i
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

                
        
