'''
#U (Understand)
Goal: Maximize profit by buying on day i and selling on day j (where j > i).

Key Constraints:

    If no profit is possible, return 0.

    The "Buy" must happen before the "Sell."

    The "Window" Insight: We are looking for the largest "gap" between a price and a 
    subsequent higher price. We don't need to check every pair; we only need to track 
    the lowest price found so far to serve as our buying point.

#P (Plan)
    Strategy:
        Initialize: * Set l (buy pointer) to index 0 and r (sell pointer) to index 1.

        Set maxP (max profit) to 0.

        Iterate: Use a while loop to move the sell pointer (r) across the array.

            The Window Logic:

                If prices[l] < prices[r]: A profit is possible. 
                    Calculate profit = prices[r] - prices[l]. 
                    Update maxP if this profit is higher than the current maxP.
                Else (prices[l] >= prices[r]): The current price at r is lower than our buy price at l. We found a better "buy" opportunity! 
                    Move the l pointer to r (reset our buy day).
                Advance: Always move the sell pointer r forward by 1 to check the next day.
            Return: After the loop finishes, return the maxP.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
            
        return max_profit






        