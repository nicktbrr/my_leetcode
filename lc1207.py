class Solution:
    def uniqueOccurrences(self, arr: [int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i, 1) + 1
        return len(d.values()) == len(set(d.values()))


arr = [-3,0,1,-3,1,1,1,-3,10,0]
arr1 = [1,1,2,2,3,3,3,3]
s = Solution()
print(s.uniqueOccurrences(arr1))