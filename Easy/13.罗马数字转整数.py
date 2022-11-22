#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        valDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        resultVal = 0
        strEnum = enumerate(s)
        sLen = len(s)

        for idx, item in strEnum:
            value = valDict[s[idx]]
            if idx < sLen - 1 and value < valDict[s[idx + 1]]:
                resultVal -= value
            else:
                resultVal += value

        return resultVal
        
# @lc code=end

print(Solution().romanToInt("MCMXCIV"))