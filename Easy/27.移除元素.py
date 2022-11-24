#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numsLen = len(nums)
        curIdx = 0
        repIdx = -1

        while curIdx < numsLen:
            if nums[curIdx] == val:
                if repIdx == -1:
                    repIdx = curIdx
            else:
                if repIdx != -1:
                    nums[repIdx] = nums[curIdx]
                    repIdx += 1
                
            curIdx += 1

        if repIdx == -1:
            repIdx = curIdx

        return repIdx
# @lc code=end

Solution().removeElement([], 4)

