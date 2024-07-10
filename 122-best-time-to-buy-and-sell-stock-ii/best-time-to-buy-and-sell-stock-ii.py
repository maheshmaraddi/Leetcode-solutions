class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp ={}
        def find(ind,buy):
            if ind ==n:
                return 0
            if (ind,buy) in dp:
                return dp[(ind,buy)]
            if not buy: # can buy
                opt1 = find(ind+1,0)
                opt2 = find(ind+1,1) - prices[ind]
            else:
                opt1 = find(ind+1,1)
                opt2 = find(ind+1,0) + prices[ind]
            dp[(ind,buy)] = max(opt1,opt2)
            return dp[(ind,buy)]
        return find(0,0)
                
        