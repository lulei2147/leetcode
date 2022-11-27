#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
                
        if nums[low] < target:
            return low + 1
        
        return low
# @lc code=en

print(Solution().searchInsert([1,3,5,6], 2))