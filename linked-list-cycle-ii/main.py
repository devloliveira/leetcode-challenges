"""
https://leetcode.com/problems/linked-list-cycle-ii/description/
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""

from typing import Optional
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_nodes_map = {}
        current_node = head
        while current_node is not None:
            node_id = id(current_node)
            if node_id in visited_nodes_map:
                return visited_nodes_map[node_id]
            else:
                visited_nodes_map[node_id] = current_node

            current_node = current_node.next
        
        return None



class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Test_solution(unittest.TestCase):

    def test_input_1(self):
        node_4 = ListNode(val=-4, next=None)
        node_3 = ListNode(val=0, next=node_4)
        node_2 = ListNode(val=2, next=node_3)
        node_1 = ListNode(val=3, next=node_2)

        # Establishes the cycle
        node_4.next = node_2

        assert Solution().detectCycle(node_1) == node_2

    def test_input_2(self):
        node_2 = ListNode(val=2, next=None)
        node_1 = ListNode(val=3, next=node_2)

        # Establishes the cycle
        node_2.next = node_1

        assert Solution().detectCycle(node_1) == node_1

    def test_input_3(self):
        node_1 = ListNode(val=1, next=None)

        assert Solution().detectCycle(node_1) is None

    def test_input_4(self):
        node_4 = ListNode(val=-4, next=None)
        node_3 = ListNode(val=0, next=node_4)
        node_2 = ListNode(val=2, next=node_3)
        node_1 = ListNode(val=3, next=node_2)

        assert Solution().detectCycle(node_1) is None

if __name__ == '__main__':
    unittest.main()
