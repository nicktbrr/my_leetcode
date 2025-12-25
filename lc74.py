from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # t = 0
        # b = len(matrix)
        # while t < b:
        #     mid = (t + b ) // 2
        #     guess = matrix[mid][-1]
        #     if target > guess:
        #         t = mid + 1
        #     elif target < matrix[mid][0]:
        #         b = mid - 1
        #     else:
        #         break
        # if t >= b:
        #     return False
        # row = (t + b ) // 2
        # l = 0
        # r = len(matrix[t]) - 1
        # while l <= r:
        #     mid = (r + l) // 2
        #     guess = matrix[row][mid]
        #     if guess == target:
        #         return True
        #     elif guess < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        # return False

        t = 0
        b = len(matrix)
        # Variable to store the specific row we find
        row = -1

        while t < b:
            mid = (t + b) // 2
            # Check range: Start of row vs End of row
            if target > matrix[mid][-1]:
                t = mid + 1
            elif target < matrix[mid][0]:
                # FIX 1: use 'mid', not 'mid - 1'
                b = mid
            else:
                # FIX 2: Save the row index immediately
                row = mid
                break

        # If we didn't find a valid row
        if row == -1:
            return False

        l = 0
        # FIX 3: Use 'row' and subtract 1 for correct index bounds
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (r + l) // 2
            guess = matrix[row][mid]
            if guess == target:
                return True
            elif guess < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11

print(Solution().searchMatrix(matrix, target))