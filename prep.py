import random


def threeSum(nums, target):
    nums.sort()
    n = len(nums)
    res = set()
    for i in range(n):
        first = nums[i]
        l, r = i + 1, n - 1
        while l < r:
            curr_sum = first + nums[l] + nums[r]
            if curr_sum == target:
                res.add((i, l, r))
                r -= 1
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
    return [list(combo) for combo in res]

def textWrapper(text, limit):
    res = []
    text = text.strip()
    while len(text) > limit:
        found_space = False
        for i in range(limit - 1, -1, -1):
            if text[i] == ' ':
                res.append(text[:i])
                text = text[i:].lstrip()
                found_space = True
                break
        if not found_space:
            res.append(text[:limit])
            text = text[limit:].lstrip()
    res.append(text)
    return "\n".join(res)


def rand_normal(mu=0, std=1):
    var = sum(random.random() for _ in range(12))
    z = var - 6
    return (z * std) + mu

print(rand_normal(0,1))
