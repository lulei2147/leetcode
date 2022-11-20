#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strsLen = len(strs)
        shortestStr = strs[0]
        # 找出最短字符串
        for idx in range(1,strsLen):
            if len(shortestStr) > len(strs[idx]):
                shortestStr = strs[idx]

        resultStr = ""
        for idx in range(len(shortestStr)): # O(n2)
            resultStr = shortestStr[0:idx+1]
            for strItem in strs:
                if resultStr != strItem[0:idx+1]:
                    return resultStr[0:idx]
        
        return resultStr

# @lc code=end
s1 = ["flower", "flow", "floight"]
s2 = ["dog", "racecar", "car"]
print(Solution().longestCommonPrefix(s1))
