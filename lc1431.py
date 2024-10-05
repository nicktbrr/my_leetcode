
def kidsWithCandies(candies, extraCandies):
    m = max(candies)
    r = []
    for n in candies:
        if n + extraCandies >= m:
            r.append(True)
        else:
            r.append(False)
    return r


candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))