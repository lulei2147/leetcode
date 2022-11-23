#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        repIdx = 0
        numsLen = len(nums)
        curIdx = 0

        if numsLen == 1 or numsLen == 0:
            return numsLen

        while curIdx < numsLen - 1:
            if nums[curIdx] == nums[curIdx + 1]:
                curIdx += 1
                if repIdx == 0:
                    repIdx = curIdx
            else:
                curIdx += 1
                if repIdx != 0:
                    nums[repIdx] = nums[curIdx]
                    repIdx += 1
        # 输入nums没有重复元素
        if repIdx == 0:
            repIdx = curIdx + 1

        return repIdx
# @lc code=end

Solution().removeDuplicates([1,2,3,3,4,4,4,4])
