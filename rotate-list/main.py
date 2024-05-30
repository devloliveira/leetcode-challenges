"""
https://leetcode.com/problems/rotate-list/description/

Given the head of a linked list, rotate the list to the right by k places.
"""

from typing import Optional, List
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_size_and_tail_and_before_tail(node: ListNode) -> ListNode:
    current_node = node
    prev_node = None
    index = 0
    while current_node.next is not None:
        prev_node = current_node
        current_node = current_node.next
        index += 1

    if current_node:
        index += 1

    return (index, prev_node, current_node)


class Solution:

    def rotate_trinity(self, head, before_tail, tail):
        tail.next  = head
        before_tail.next = None
        return tail, before_tail

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If there is no list, returns None
        if not head:
            return None

        rotations = 0
        size, before_tail, tail = get_size_and_tail_and_before_tail(head)

        # If the list has only one element, no rotation is needed.
        # Returns the head
        if not before_tail:
            return head

        if k > size:
            k = (k % size)

        current_head = head
        while rotations < k:
            current_head, tail = self.rotate_trinity(current_head, before_tail, tail)
            _, before_tail, tail = get_size_and_tail_and_before_tail(current_head)
            rotations += 1
        return current_head


class Test_solution(unittest.TestCase):

    def _to_list(self, node: ListNode) -> List[int]:
        values = list()
        current_node = node
        while current_node is not None:
            values.append(current_node.val)
            current_node = current_node.next
        return values

    def _to_nodelist(self, lst: List[int]) -> List[ListNode]:
        nodes = list()
        for n in lst:
            node = ListNode(val=n, next=None)
            if nodes:
                nodes[-1].next = node
            nodes.append(node)
        return nodes

    def test_input_1(self):
        lst = [1,2,3,4,5]
        expected = [4,5,1,2,3]
        returned = Solution().rotateRight(self._to_nodelist(lst)[0], k=2)
        assert self._to_list(returned) == expected

    def test_input_2(self):
        lst = [0,1,2]
        expected = [2,0,1]
        returned = Solution().rotateRight(self._to_nodelist(lst)[0], k=1)
        assert self._to_list(returned) == expected

    def test_input_3(self):
        lst = [0,1,2]
        expected = [2,0,1]
        returned = Solution().rotateRight(self._to_nodelist(lst)[0], k=4)
        assert self._to_list(returned) == expected

    def test_input_4(self):
        lst = [1,2,3]
        expected = [2,3,1]
        returned = Solution().rotateRight(self._to_nodelist(lst)[0], k=2)
        assert self._to_list(returned) == expected

# Start tests
unittest.main()
