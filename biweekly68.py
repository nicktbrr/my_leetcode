class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(s.split()) for s in sentences])


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ing_d = defaultdict(list)
        num_d = defaultdict(int)
        for i in range(len(recipes)):
            num_d[recipes[i]] = len(ingredients[i])
            for j in range(len(ingredients[i])):
                ing_d[ingredients[i][j]].append(recipes[i])

        queue = deque(supplies)
        res = []
        while queue:
            item = queue.popleft()
            r_list = ing_d[item]
            for r in r_list:
                num_d[r] -= 1
                if num_d[r] <= 0:
                    queue.append(r)
                    res.append(r)
        return res


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        balance = 0
        n = len(s)
        if n % 2 == 1:
            return False
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        balance = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return True

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        start = intervals[0][0]
        prev = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if prev >= s:
                prev = max(e, prev)
                continue
            else:
                res.append([start, prev])
                start = s
                prev = e
        res.append([start, prev])
        return res


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        print(dp)
        return max(dp)


