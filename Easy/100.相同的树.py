#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack, q_stack = [], []

        while (p_stack or p) or (q_stack or q):
            if p != None and q != None:
                if p.val == q.val:
                    p_stack.append(p)
                    q_stack.append(q)
                    p = p.left
                    q = q.left
                else:
                    return False
            else:
                if p == None and q == None:
                    p = p_stack.pop()
                    p = p.right
                    q = q_stack.pop()
                    q = q.right
                else:
                    return False

        return True
# @lc code=end

