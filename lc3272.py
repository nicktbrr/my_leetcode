def gen_pali(n, idx, k, current=""):
    half_length = n // 2  # Integer division gives us the right half length

    if idx == half_length:
        if n % 2 == 0:
            # Even length - just mirror
            if int(current + current[::-1]) % k == 0:
                return [current + current[::-1]]
            return []
        else:
            # Odd length - try each possible middle digit
            result = []
            for c in "0123456789":
                if int(current + c + current[::-1]) % k == 0:
                    result.append(current + c + current[::-1])
            return result

    palis = []
    if idx == 0:
        num = "123456789"  # First digit can't be 0
    else:
        num = "0123456789"  # Other positions can be any digit

    for i in num:
        palis.extend(gen_pali(n, idx + 1, k, current + i))
    return palis

def create_pali_set(palis, facts, n):
    tot_counts = 0
    my_set = set()
    for pali in palis:
        pali_s = "".join(sorted(pali))
        if pali_s not in my_set:
            counts = {}
            for c in pali_s:
                if c not in counts:
                    counts[c] = 1
                else:
                    counts[c] += 1
            numerator = facts[n]
            denominator = 1
            tot_perms = 0
            for _, v in counts.items():
                denominator *= facts[v]
            tot_perms += (numerator // denominator)

            if "0" in counts:
                numerator = facts[n - 1]
                denominator = 1
                for k, v in counts.items():
                    denominator *= facts[v]
                temp= (numerator // (denominator // counts["0"]))
                tot_perms -= temp
            tot_counts += tot_perms
            my_set.add(pali_s)
    return tot_counts

def create_facts(n, start=1):
    ls = [1]
    for i in range(1, n + 1):
        ls.append(i * ls[-1])
    return ls


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        palis = gen_pali(n, 0, k)
        facts = create_facts(n)
        pali_set = create_pali_set(palis, facts, n)


        return pali_set


s = Solution()

p = s.countGoodIntegers(5, 6)
print(p)