#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n)
        records = dict()
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]

        # 暴力解法 时间复杂度O(n2)，44ms
        # result = []
        # length = len(nums)
        # for i in range(length):
        #     for j in range(length - i - 1):
        #         if nums[i] + nums[i + j + 1] == target:
        #             result = [i, i + j + 1]
        # return result
# @lc code=end

