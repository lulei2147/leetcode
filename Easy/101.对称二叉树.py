#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        l_stack, r_stack = [], []

        leftTree = root.left
        rightTree = root.right

        while l_stack or leftTree or r_stack or rightTree:
            if leftTree != None and rightTree != None:
                if leftTree.val == rightTree.val:
                    l_stack.append(leftTree)
                    r_stack.append(rightTree)
                    leftTree = leftTree.left
                    rightTree = rightTree.right
                else:
                    return False
            else:
                if leftTree == None and rightTree != None:
                    return False
                if leftTree != None and rightTree == None:
                    return False

                leftTree = l_stack.pop()
                leftTree = leftTree.right
                rightTree = r_stack.pop()
                rightTree = rightTree.left

        return True


# @lc code=end

