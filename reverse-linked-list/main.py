"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input
head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

from typing import Optional, List
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head

        nodes = []
        while current_node is not None:
            nodes.append(current_node)
            current_node = current_node.next

        current_node = None
        i = 0
        j = len(nodes) - 1
        while i < j:
            tmp_val = nodes[i].val
            nodes[i].val = nodes[j].val
            nodes[j].val = tmp_val

            i += 1
            j -= 1

        return nodes[0] if nodes else None


class Test_solution(unittest.TestCase):
    def test_first_input(self):
        node_5 = ListNode(val=5, next=None)
        node_4 = ListNode(val=4, next=node_5)
        node_3 = ListNode(val=3, next=node_4)
        node_2 = ListNode(val=2, next=node_3)
        node_1 = ListNode(val=1, next=node_2)

        returned_node = Solution().reverseList(head=node_1)
        returned_values = []
        current_node = returned_node
        while current_node is not None:
            returned_values.append(current_node.val)
            current_node = current_node.next

        assert returned_values == [5,4,3,2,1]

    def test_second_input(self):
        node_1 = ListNode(val=1, next=None)

        returned_node = Solution().reverseList(head=node_1)
        returned_values = []
        current_node = returned_node
        while current_node is not None:
            returned_values.append(current_node.val)
            current_node = current_node.next

        assert returned_values == [1]

    def test_third_input(self):
        assert Solution().reverseList(head=None) is None


if __name__ == '__main__':
    unittest.main()
