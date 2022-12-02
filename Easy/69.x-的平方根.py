#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high, res = 0, x, 0

        while low <= high:
            mid = (low + high) // 2

            if (mid * mid) <= x:
                low = mid + 1
                res = mid # res*res 是小于x的最小整数
            else:
                high = mid - 1

        return res
# @lc code=end

print(Solution().mySqrt(4))