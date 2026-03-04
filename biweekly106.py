class Solution:
    def isFascinating(self, n: int) -> bool:
        n1 = str(n * 2)
        n2 = str(n * 3)
        n3 = str(n)+n1+n2
        c = Counter(n3)
        if c.total() != 9 or len(c.values()) != 9 or '0' in c:
            return False
        return True

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        l = 0
        res = 1
        num_pairs = 0
        pair_idx = 0
        for r in range(1, len(s)):
            if s[r] == s[r-1]:
                num_pairs += 1
                if num_pairs > 1:
                    l = pair_idx
                pair_idx = r
            res = max(res, r-l + 1)
        return res

class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i in range(len(nums)):
            if s[i] == 'R':
                nums[i] += d
            else:
                nums[i] -= d
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            res += (abs(nums[i-1] - nums[i]) * (len(nums) - i) * i)
        return res % (10**9 + 7)

class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        mask_d = {}
        for idx,row in enumerate(grid):
            num = 0
            for c in range(len(grid[0])):
                num |= (row[c] << c)
            if num == 0:
                return [idx]
            if num not in mask_d:
                mask_d[num] = idx
        v = sorted(mask_d.keys())
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                if v[i] & v[j] == 0:
                    return sorted([mask_d[v[i]], mask_d[v[j]]])
        return []