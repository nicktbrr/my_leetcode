class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            s1 = heapq.heappop(max_heap)
            s2 = heapq.heappop(max_heap)
            if s1 != s2:
                heapq.heappush(max_heap, s1 - s2)
        return -max_heap[0] if max_heap else 0

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            popped = False
            while stack and stack[-1] == c:
                stack.pop()
                popped = True
            if not popped:
                stack.append(c)
        return "".join(stack)

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        cache = {w:1 for w in words}
        for w in words:
            scores = []
            for i in range(len(w)):
                temp = w[:i] + w[i+1:]
                if temp in cache:
                    scores.append(cache[temp] + 1)
            if scores:
                cache[w] = max(scores)
            else:
                cache[w] = 1
        return max(cache.values()) if cache else 1


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = 0
        for s in stones:
            total += s
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for s in stones:
            for i in range(len(dp) - 1, s - 1, -1):
                if dp[i - s]:
                    dp[i] = True

        for i in range(len(dp) - 1, -1, -1):
            if dp[i]:
                return total - (i * 2)
        return 0