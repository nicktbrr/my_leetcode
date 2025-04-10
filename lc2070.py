from bisect import bisect_right
from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        from bisect import bisect_right
        from typing import List

        class Solution:
            def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
                # Sort items by price
                items.sort()

                # For each price point, keep track of maximum beauty seen so far
                max_beauty = 0
                prices = []
                beauties = []

                for price, beauty in items:
                    max_beauty = max(max_beauty, beauty)
                    prices.append(price)
                    beauties.append(max_beauty)

                result = []
                for q in queries:
                    # Find the index of the first item with price > q
                    idx = bisect_right(prices, q) - 1

                    if idx >= 0:
                        result.append(beauties[idx])
                    else:
                        result.append(0)

                return result






s = Solution()
items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]
print(s.maximumBeauty(items, queries))
