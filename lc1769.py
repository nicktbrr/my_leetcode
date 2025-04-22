from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        my_dict = {'left': 0, 'right': len([idx + 1 for idx, c in enumerate(boxes[1:]) if c == '1'])}
        left = 0
        right = sum(idx + 1 for idx, c in enumerate(boxes[1:]) if c == '1')
        result.append(left + right)
        for idx, c in enumerate(boxes[1:]):
            if c == '0' and boxes[idx] == '1':
                my_dict['left'] += 1
                left = left + my_dict['left']
                right = right - my_dict['right']
            elif c == '1' and boxes[idx] == '0':
                left = left + my_dict['left']
                my_dict['right'] -= 1
                right = right - (my_dict['right'] + 1)
            elif c == '0' and boxes[idx] == '0':
                left = left + my_dict['left']
                right = right - my_dict['right']
            else:
                my_dict['left'] += 1
                my_dict['right'] -= 1
                left = left + my_dict['left']
                right = right - (my_dict['right'] + 1)
            result.append(left + right)
        return result


s = Solution()
print(s.minOperations('001011'))