#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = ListNode(-1)

        currPointer = resHead

        while list1 and list2:
            if list1.val < list2.val:
                currPointer.next = list1

# @lc code=end

list1_2 = ListNode(4)
list1_1 = ListNode(2, list1_2)
list1_0 = ListNode(1, list1_1)

list2_3 = ListNode(7)
list2_2 = ListNode(4, list2_3)
list2_1 = ListNode(2, list2_2)
list2_0 = ListNode(1, list2_1)

list1 = [list1_0, list1_1, list1_2]
list2 = [list2_0, list2_1, list2_2, list2_3]

Solution().mergeTwoLists(list1, list2)