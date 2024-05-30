"""
https://leetcode.com/problems/linked-list-cycle/
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional
import unittest


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = set()
        current_node = head

        while current_node is not None:
            visited_nodes.add( id(current_node) )

            if current_node.next and id(current_node.next) in visited_nodes:
                return True

            current_node = current_node.next

        return False


class Test_solution(unittest.TestCase):

    def test_input_1(self):
        node_4 = ListNode(val=-4, next=None)
        node_3 = ListNode(val=0, next=node_4)
        node_2 = ListNode(val=2, next=node_3)
        node_1 = ListNode(val=3, next=node_2)

        # Establishes the cycle
        node_4.next = node_2

        assert Solution().hasCycle(node_1) is True

    def test_input_2(self):
        node_2 = ListNode(val=2, next=None)
        node_1 = ListNode(val=3, next=node_2)

        # Establishes the cycle
        node_2.next = node_1

        assert Solution().hasCycle(node_1) is True

    def test_input_3(self):
        node_1 = ListNode(val=1, next=None)

        assert Solution().hasCycle(node_1) is False

if __name__ == '__main__':
    unittest.main()
