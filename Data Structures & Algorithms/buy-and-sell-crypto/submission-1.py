class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,best=0,0

        for r in range(len(prices)):
            if prices[l]<prices[r]:
                best=max(best,prices[r]-prices[l])
            else:
                l=r
        return best

                