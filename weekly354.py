class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        for idx, n in enumerate(nums):
            if (len(nums) % (idx + 1)) == 0:
                print(n)
                res += n**2
        return res


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,0
        res = 1
        while r < len(nums):
            if nums[l] + k < nums[r] - k:
                l += 1
            r += 1
            res = max(res, r-l)
        return res

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right = Counter(nums)
        left = Counter()
        left_tot = 0
        right_tot = right.total()
        dom = max(right.items(), key=lambda x: x[1])[0]
        for i in range(len(nums)):
            right[nums[i]] -= 1
            left[nums[i]] += 1

            right_tot -= 1
            left_tot += 1
            if right[nums[i]] == 0:
                del right[nums[i]]
            if left[dom] * 2 > left_tot and right[dom] * 2 > right_tot:
                return i
        return -1


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        left = 0
        f_set = set(forbidden)
        res = 0
        for right in range(len(word)):
            for i in range(right, max(right-10, left-1), -1):
                sub = word[i:right+1]
                if sub in f_set:
                    left = i + 1
                    break
            res = max(res, right-left+1)
        return res