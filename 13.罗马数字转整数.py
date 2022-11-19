#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        valDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
        'a':900, 'b':400, 'c':90, 'd':40, 'e':9, 'f':4}

        # IV: 4    IX: 9
        # XL: 40   XC: 90
        # CD: 400  CM: 900
        resStr = s.replace("CM", "a")
        resStr =resStr.replace("CD", "b")
        resStr =resStr.replace("XC", "c")
        resStr =resStr.replace("XL", "d")
        resStr =resStr.replace("IX", "e")
        resStr =resStr.replace("IV", "f")

        resultVal = 0
        resultList = list(resStr)

        for item in resultList:
            resultVal += valDict[item]

        return resultVal
        
# @lc code=end

print(Solution().romanToInt("LVIII"))