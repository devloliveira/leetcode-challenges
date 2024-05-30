"""
https://leetcode.com/problems/add-two-numbers/description/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

"""
Time: Beats 77%
Memory: Beats 48%
"""

from typing import List, Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        iter1 = l1
        iter2 = l2
        carry_on = 0

        result_head = None
        prev_node = None
        while (iter1 is not None) or (iter2 is not None):
            # We use the getattr because both iter1 and iter2 may be None, since the size of both
            # ListNodes are not guarateed to be the same.
            result = getattr(iter1, 'val', 0) + getattr(iter2, 'val', 0) + carry_on
            if result > 9:
                result = result % 10
                carry_on = 1
            else:
                carry_on = 0

            current_node = ListNode(val=result, next=None)
            if not result_head:
                result_head = current_node

            if prev_node:
                prev_node.next = current_node

            prev_node = current_node

            if iter1:
                iter1 = iter1.next
            if iter2:
                iter2 = iter2.next

        # If there is a carry_on number by the time we reach the end of both ListNodes, then
        # we must create a final node containing that carry_on value.
        if carry_on:
            prev_node.next = ListNode(val=carry_on, next=None)

        return result_head


class Test_solution(unittest.TestCase):

    def _to_node_list(self, array: List[int]) -> List[ListNode]:
        nodes = list()
        for n in array:
            node = ListNode(val=n, next=None)

            if nodes:
                nodes[-1].next = node

            nodes.append(node)

        return nodes

    def _to_array(self, head: ListNode) -> List[int]:
        values = list()
        current_node = head
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
        return values

    def test_input_1(self):
        l1 = [2,4,3]
        l2 = [5,6,4]
        expected = [7,0,8]

        returned = Solution().addTwoNumbers( self._to_node_list(l1)[0], self._to_node_list(l2)[0] )

        assert self._to_array(returned) == expected

    def test_input_2(self):
        l1 = [0]
        l2 = [0]
        expected = [0]

        returned = Solution().addTwoNumbers( self._to_node_list(l1)[0], self._to_node_list(l2)[0] )

        assert self._to_array(returned) == expected

    def test_input_3(self):
        l1 = [9,9,9,9,9,9,9]
        l2 = [9,9,9,9]
        expected = [8,9,9,9,0,0,0,1]
        returned = Solution().addTwoNumbers( self._to_node_list(l1)[0], self._to_node_list(l2)[0] )

        assert self._to_array(returned) == expected


if __name__ == '__main__':
    unittest.main()
