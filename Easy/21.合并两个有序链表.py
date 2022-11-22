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
                list1 = list1.next
            else:
                currPointer.next = list2
                list2 = list2.next

            currPointer = currPointer.next

        if list1 is None:
            currPointer.next = list2
        else:
            currPointer.next = list1

        return resHead.next

# @lc code=end
