class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        for i, num in enumerate(arr):
            if 0 <= i - 1 and i + 1 < len(arr):
                if arr[i-1] < arr[i] > arr[i+1]:
                    l,r = i - 1, i + 1
                    while 0 < l and arr[l - 1] < arr[l]:
                        l -= 1
                    while r < len(arr) - 1 and arr[r + 1] < arr[r]:
                        r += 1
                    res = max(res, r-l + 1)
        return res