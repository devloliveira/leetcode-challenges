# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 10^5
    0 <= Node.val <= 100
"""

from typing import List
import unittest


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodesFromList(head: ListNode, k: int) -> List:
    head_index = k-1
    tail_index = len(head) - k

    head_value = head[head_index]
    tail_value = head[tail_index]

    head[head_index] = tail_value
    head[tail_index] = head_value

    return head


def build_from_list(array: List[int]) -> ListNode:
    nodes = []
    for n in array:
        nodes.append(ListNode(val=n))

    i = 0
    while i < (len(nodes)-1):
        nodes[i].next = nodes[i+1]
        i += 1

    return nodes[0]


def convert_to_list(head: ListNode):
    array = [head.val]
    iter = head
    while iter.next is not None:
        iter = iter.next
        array.append(iter.val)

    return array


def get_node_by_index(head: ListNode, k: int) -> ListNode:
    index = 0
    iter = head
    while index < k:
        iter = iter.next
        index += 1

    return iter


def get_length_from_head(head: ListNode) -> ListNode:
    length = 1
    iter = head
    while iter.next is not None:
        iter = iter.next
        length += 1

    return length


def swapNodesFromListNode(head: ListNode, k: int) -> ListNode:
    length = get_length_from_head(head)

    head_index = k-1
    tail_index = length - k

    head_instance = get_node_by_index(head, head_index)
    tail_instance = get_node_by_index(head, tail_index)

    new_head_value = tail_instance.val
    new_tail_value = head_instance.val

    head_instance.val = new_head_value
    tail_instance.val = new_tail_value

    return head


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> List[ListNode]:
        return swapNodesFromListNode(head=head, k=k)


class SolutionWithList:
    def swapNodes(self, head: List, k: int) -> List:
        return swapNodesFromList(head, k)


class Test__SolutionWithList(unittest.TestCase):
    def test__scenario_1(self):
        assert SolutionWithList().swapNodes(head=[1,2,3,4,5], k=2) == [1,4,3,2,5]

    def test__scenario_2(self):
        assert SolutionWithList().swapNodes(head=[7,9,6,6,7,8,3,0,9,5],k=5) == [7,9,6,6,8,7,3,0,9,5]

    def test__scenario_3(self):
        assert SolutionWithList().swapNodes(head=[7,9,6,6,7,8,3,0,9,5],k=3) == [7,9,0,6,7,8,3,6,9,5]

    def test__scenario_4(self):
        assert SolutionWithList().swapNodes(head=[1,2,3],k=3) == [3,2,1]


class Test__Solution(unittest.TestCase):
    def test__get_length_from_head(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3,
                    next=None
                )
            )
        )
        assert get_length_from_head(head) == 3

    def test__get_length_from_head_with_no_next(self):
        head = ListNode(
            val=1,
            next=None
        )
        assert get_length_from_head(head) == 1

    def test__swap_input_1(self):
        head = ListNode(
            val=1,
            next=ListNode(
                val=2,
                next=ListNode(
                    val=3,
                    next=None
                )
            )
        )

        returned_head = Solution().swapNodes(head, k=1)

        returned_list = convert_to_list(returned_head)
        assert returned_list == [3, 2, 1]

    def test__swap_input_2(self):
        head = build_from_list([1,2,3,4,5])

        returned_head = Solution().swapNodes(head, k=2)
        returned_list = convert_to_list(returned_head)

        assert returned_list == [1,4,3,2,5]

    def test__swap_input_3(self):
        head = build_from_list([7,9,6,6,7,8,3,0,9,5])

        returned_head = Solution().swapNodes(head, k=5)
        returned_list = convert_to_list(returned_head)

        assert returned_list == [7,9,6,6,8,7,3,0,9,5]

    def test__swap_input_4(self):
        head = build_from_list([7,9,6,6,7,8,3,0,9,5])

        returned_head = Solution().swapNodes(head, k=3)
        returned_list = convert_to_list(returned_head)

        assert returned_list == [7,9,0,6,7,8,3,6,9,5]


if __name__ == '__main__':
    unittest.main()
