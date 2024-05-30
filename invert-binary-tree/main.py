"""
https://leetcode.com/problems/invert-binary-tree/submissions/1256909144/

Given the root of a binary tree, invert the tree, and return its root.
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _invert_from_node(self, node: TreeNode):
        if getattr(node, 'right', None):
            self._invert_from_node(node.right)

        if getattr(node, 'left', None):
            self._invert_from_node(node.left)

        try:
            tmp_right = node.right
            node.right = node.left
            node.left = tmp_right
        except AttributeError:
            pass

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        self._invert_from_node(root)

        return root
        