#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        xstr = str(x)
        strlen = len(xstr)
        idx = 0

        while idx < ((strlen + 1) // 2):
            if xstr[idx] != xstr[-idx-1]:
                return False

            idx += 1

        return True
            
# @lc code=end

print(Solution().isPalindrome(123321))