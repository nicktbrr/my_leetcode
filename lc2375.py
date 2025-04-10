def smallestNumber(pattern: str) -> str:
    buf = []
    nums = []
    for i, p in enumerate(pattern):
        if p == "I":
            if len(buf) != 0:
                buf.append(i + 1)
                nums = nums + list(reversed(buf))
                buf = []
            else:
                nums.append(i + 1)
        else:
            buf.append(i + 1)
    if len(buf) != 0:
        buf.append(len(pattern) + 1)
        nums = nums + list(reversed(buf))
    else:
        nums.append(len(pattern) + 1)
    return ''.join(str(x) for x in nums)

print(smallestNumber('IDID'))