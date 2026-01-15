from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        y_min = float('inf')
        y_max = float('-inf')
        total_area = 0
        for x,y,l in squares:
            total_area += l**2
            if y + l > y_max:
                y_max = y + l
            if y < y_min:
                y_min = y
        eps = 10E-5

        def calc_lower(mid):
            lower_area = 0
            for x,y,l in squares:
                if y + l < mid:
                    lower_area += l**2
                elif y < mid < y + l:
                    lower_area += l * (mid - y)
            return lower_area

        def binary_search(low, high, target):
            guess = (high + low) / 2
            lower_area = calc_lower(guess)
            if abs(lower_area - target) < eps:
                return guess
            elif lower_area < target:
                return binary_search(guess, high, target)
            else:
                return binary_search(low, guess, target)

        min_bound = binary_search(y_min, y_max, total_area / 2)
        min_max_bound = float('-inf')
        for x,y,l in squares:
            if y < min_bound < y + l:
                return min_bound
            if min_bound > y + l > min_max_bound:
                min_max_bound = y + l
        return min_max_bound




squares = [[0,0,2],[1,1,1]]
squares = [[0,0,1],[2,2,1]]
print(Solution().separateSquares(squares))


