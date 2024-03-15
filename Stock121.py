from typing import List
class solution:
    def MaxProfit(self,prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            if min_price > i:
                min_price =i

            else:
                max_profit = max(max_profit, i - min_price)
        return max_profit

solution_instance = solution()
prices = [7, 1, 5, 3, 6, 4]
print(solution_instance.MaxProfit(prices))    