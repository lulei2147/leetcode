#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        spaceFlg = 0
        header = 0
        tail = 0

        if idx == -1:
            return 0

        while idx >= 0:
            if spaceFlg == 0:
                if s[idx] != ' ':
                    spaceFlg = 1
                    tail = idx
            elif spaceFlg == 1:
                if s[idx] == ' ':
                    header = idx + 1
                    break
                elif idx == 0:
                    header = idx
                    break
            idx -= 1
        
        if header != tail:  # "abc "
            return tail - header + 1
        else:
            if s[header] != ' ':
                return 1
            else:
                return 0

# @lc code=end

print(Solution().lengthOfLastWord("Hello World"))
