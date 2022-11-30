#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aNum, bNum = int(a, 2), int(b, 2)
        sum = aNum + bNum
        return bin(sum)[2:]

        '''maxLen = len(a)
        minLen = len(b)
        maxStr = a
        minStr = b

        if maxLen < minLen:
            maxLen = maxLen + minLen
            mimLen = maxLen - minLen
            maxLen = maxLen - minLen
            maxStr = b
            minStr = a

        sign = 0
        for i in range(maxLen - 1, -1, -1):
            print(i)
            if minLen > 0:
                pass
            else:
                pass'''
# @lc code=end

print(Solution().addBinary("101", "10"))