#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsLen = len(digits)

        for i in range(digitsLen):
            idx = digitsLen - 1 - i
            if digits[idx] == 9:
                digits[idx] = 0
                if idx == 0:
                    digits = [1] + digits
                    break
                else:
                    continue
            else:
                if i == 0:
                    digits[-1] += 1
                else:
                    digits[idx] += 1
                break

        return digits
# @lc code=end

print(Solution().plusOne([1]))
