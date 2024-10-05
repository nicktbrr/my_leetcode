class Solution:
    def predictPartyVictory_bad(self, senate: str) -> str:
        queue = []
        i = 0
        while len(set(senate)) != 1:
            if len(queue) == 0:
                queue.append(senate[i])
                i = (i + 1) % len(senate)
            elif senate[i] != queue[0]:
                senate = senate[:i] + senate[i + 1:]
                queue.pop()
                i = i % len(senate)
            else:
                queue.append(senate[i])
                i = (i + 1) % len(senate)
        return "Radiant" if senate[0] == "R" else "Dire"

    def predictPartyVictory(self, senate: str) -> str:
        queue_d = []
        queue_r = []
        for i in range(len(senate)):
            if senate[i] == "D":
                queue_d.append(i)
            else:
                queue_r.append(i)
        i = len(senate)
        while len(queue_r) != 0 and len(queue_d) != 0:
            if queue_r.pop(0) < queue_d.pop(0):
                queue_r.append(i)
            else:
                queue_d.append(i)
            i += 1
        if len(queue_r) == 0:
            return "Dire"
        else:
            return "Radiant"


senate = "RD"
t = Solution()
print(t.predictPartyVictory(senate))
