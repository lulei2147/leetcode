#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        sStack = []
        for i in range(len(s)):
            if s[i] in '([{':
                sStack.append(s[i])
            else:
                if sStack == []:
                    return False

                popStr = sStack.pop()
                if s[i] == ')' and popStr != '(' or \
                    s[i] == ']' and popStr != '[' or \
                    s[i] == '}' and popStr != '{':
                    return False

        # 如果符合规则，最终栈肯定是空的
        if sStack != []:
            return False

        return True
                
# @lc code=end

print(Solution().isValid('[['))