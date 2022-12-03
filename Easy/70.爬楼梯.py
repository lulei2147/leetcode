#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        a, b = 1, 0 
        res = 0
        for i in range(1, n+1):
            res = a + b
            b = a
            a = res

        return res
# @lc code=end

