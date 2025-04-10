
def numOfSubarrays(arr):
    mod = 1000000007  # Large prime number to prevent integer overflow
    sum_ = 0  # Cumulative sum tracker
    odd = 0  # Count of prefix sums that are odd
    even = 0  # Count of prefix sums that are even
    ans = 0  # Stores the total count of subarrays with odd sum

    # Iterate through each element in the array
    for num in arr:
        sum_ += num  # Update cumulative sum

        if sum_ % 2 == 1:  # If cumulative sum is odd
            odd += 1  # Increase count of odd prefix sums
            ans += even + 1  # Previous even sums + current subarray itself contributes to odd count
        else:  # If cumulative sum is even
            even += 1  # Increase count of even prefix sums
            ans += odd  # Any previous odd prefix sum can form a new odd subarray

    return ans % mod  # Return answer within modulo constraint

print(numOfSubarrays(([1,3,4,5])))