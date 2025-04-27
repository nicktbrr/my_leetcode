from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = 0
        prefix_mod = 0
        mod_freq = {0: 1}  # one empty‐prefix with remainder 0

        for num in nums:
            # If this card is “active,” bump our running count and wrap by modulo
            if num % modulo == k:
                prefix_mod = (prefix_mod + 1) % modulo

            # Any earlier prefix with remainder (prefix_mod – k) mod modulo
            # marks a valid start for an interesting block ending here
            needed = (prefix_mod - k) % modulo
            count += mod_freq.get(needed, 0)

            # Record we’ve now seen this prefix remainder one more time
            mod_freq[prefix_mod] = mod_freq.get(prefix_mod, 0) + 1

        return count


s = Solution()
n = [3,1,9,6]
m = 3
k = 0
print(s.countInterestingSubarrays(n, m, k))