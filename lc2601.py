from typing import List

def largest_primes(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if i == 0:
                for j in range(num - 1, 1, -1):
                    if largest_primes(j):
                        nums[i] = num - j
                        break
            else:
                for j in range(num - 1, 1, -1):
                    if largest_primes(j) and nums[i - 1] < num - j:
                        nums[i] = num - j
                        break
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                # print(nums)
                return False
        # print(nums)
        return True


s = Solution()
print(s.primeSubOperation([5,8,3]))