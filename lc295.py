class MedianFinder:

    def __init__(self):
        self.nums = []
        self.is_even = True
        self.length = 0

    def addNum(self, num: int) -> None:
        def bisect(num):
            low = 0
            high = self.length

            while low < high:
                mid = (low + high) // 2
                if self.nums[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            return low

        idx = bisect(num)
        self.nums.insert(idx, num)
        self.length += 1
        self.is_even = not self.is_even

    def findMedian(self) -> float:
        if self.is_even:
            n1 = self.nums[self.length // 2]
            n2 = self.nums[(self.length // 2) - 1]
            return (n1 + n2) / 2
        else:
            return self.nums[self.length // 2]

# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(5)
obj.addNum(1)
obj.addNum(3)
obj.addNum(4)
param_2 = obj.findMedian()
print(param_2)