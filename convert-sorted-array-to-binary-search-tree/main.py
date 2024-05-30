"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
"""

import unittest
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _execute(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        i_mid = len(nums) // 2
        mid_node = TreeNode(val=nums[i_mid], left=None, right=None)
        mid_node.left = self._execute(nums[:i_mid])
        mid_node.right = self._execute(nums[i_mid+1:])

        return mid_node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self._execute(nums)


class Test_solution(unittest.TestCase):
    def to_node_list(self, list1: List[int]) -> List[TreeNode]:
        nodes:List[TreeNode] = []

        for n in list1:
            current_node = TreeNode(val=n, next=None)

            try:
                nodes[-1].next = current_node
            except IndexError:
                pass

            nodes.append(current_node)

        return nodes if nodes else None

    def to_array(self, head: TreeNode) -> List[int]:
        result: List[int] = []
        current_node = head
        while current_node is not None:
            result.append(current_node.val)
            current_node = current_node.next
        
        return result

    def test_input_1(self):
        _input = [-10,-3,0,5,9]
        n = 2

        leaf = Solution().sortedArrayToBST( _input )
        assert leaf.left.val == -3
        assert leaf.left.right is None
        assert leaf.left.left.val == -10
        assert leaf.left.left.right is None
        assert leaf.right.val == 9
        assert leaf.right.right is None
        assert leaf.right.left.val == 5


unittest.main()
