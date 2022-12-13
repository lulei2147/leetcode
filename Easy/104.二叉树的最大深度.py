#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth, depthCnt = 0, 0
        stack = []

        while root or stack:
            if root != None:
                stack.append(root)
                root = root.left
                depthCnt = depthCnt + 1
            else:
                if depthCnt > depth:
                    depth = depthCnt

                root = stack.pop()
                root = root.right

                if root == None:
                    depthCnt = depthCnt - 1

        return depth


# @lc code=end

