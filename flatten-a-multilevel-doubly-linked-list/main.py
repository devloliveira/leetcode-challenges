"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional
child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes.
These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the
example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list.
Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the
flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.
"""

from typing import Optional, List
import unittest


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:

    def _get_last_child(self, node):
        current_node = node
        while current_node.next is not None:
            current_node = current_node.next
        return current_node

    def _update_references(self, current_node, last_child_node):
        tmp_next = current_node.next
        current_node.next = current_node.child
        current_node.child.prev = current_node

        true_last_child_node = self._get_last_child(last_child_node)
        true_last_child_node.next = tmp_next

        if tmp_next:
            tmp_next.prev = true_last_child_node

        current_node.child = None
        return current_node

    def _execute(self, node):
        if not node:
            return None
        current_node = node
        while current_node.next is not None:
            if current_node.child:
                last_node_from_child = self._execute(current_node.child)
                self._update_references(current_node, last_node_from_child)
            current_node = current_node.next

        if current_node.child:
            last_node_from_child = self._execute(current_node.child)
            self._update_references(current_node, last_node_from_child)

        return current_node

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self._execute(head)
        return head


class Test_solution(unittest.TestCase):
    def test_input_1(self):
        node_3 = Node(3, prev=None, next=None, child=None)
        node_2 = Node(2, prev=None, next=node_3, child=None)
        node_1 = Node(1, prev=None, next=node_2, child=None)

        returned = Solution().flatten(node_1)
        assert returned.val == 1
        assert returned.next.val == 2
        assert returned.next.next.val == 3

    def test_input_2(self):
        node_3 = Node(3, prev=None, next=None, child=None)
        node_2 = Node(2, prev=None, next=None, child=node_3)
        node_1 = Node(1, prev=None, next=None, child=node_2)

        solution = Solution()
        returned_node_1 = solution.flatten(node_1)
        returned_node_2 = returned_node_1.next
        returned_node_3 = returned_node_2.next
        assert returned_node_1.val == 1
        assert returned_node_2.val == 2
        assert returned_node_3.val == 3
        assert returned_node_1.prev is None
        assert returned_node_2.prev == returned_node_1
        assert returned_node_3.prev == returned_node_2
        assert returned_node_1.child is None
        assert returned_node_2.child is None
        assert returned_node_3.child is None

if __name__ == '__main__':
    unittest.main()
