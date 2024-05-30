"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional, List
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_tail(head: ListNode) -> ListNode:
    current_node = head
    try:
        while current_node.next is not None:
            current_node = current_node.next
    except AttributeError:
        current_node = None
    return current_node


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        found_tail = False
        iter1 = list1
        while iter1 is not None:
            iter2 = iter1

            while iter2 is not None:
                # The first time the second iterator finds a tail, it is definitely
                # the fail of the first list. So, we can connect it to the 
                # head of the second list.
                # This will basically make join list1 into list2.
                if iter2.next is None and found_tail is False:
                    found_tail = True
                    iter2.next=list2

                if iter2.val < iter1.val:
                    tmp_val = iter1.val
                    iter1.val = iter2.val
                    iter2.val = tmp_val
                iter2 = iter2.next

            iter1 = iter1.next

        return list1


def to_node_list(list1: List[int]) -> ListNode:
    nodes:List[ListNode] = []

    for n in list1:
        current_node = ListNode(val=n, next=None)

        try:
            nodes[-1].next = current_node
        except IndexError:
            pass

        nodes.append(current_node)

    return nodes[0] if nodes else None


def to_array(head: ListNode) -> List[int]:
    result: List[int] = []
    current_node = head
    while current_node is not None:
        result.append(current_node.val)
        current_node = current_node.next
    
    return result


class Test_solution(unittest.TestCase):
    def test_input_1(self):
        list1 = [1,2,4]
        list2 = [1,3,4]
        result = Solution().mergeTwoLists(to_node_list(list1), to_node_list(list2))

        assert to_array(result) == [1,1,2,3,4,4]

    def test_input_2(self):
        list1 = []
        list2 = []
        result = Solution().mergeTwoLists(to_node_list(list1), to_node_list(list2))

        assert to_array(result) == []

    def test_input_3(self):
        list1 = []
        list2 = [0]
        result = Solution().mergeTwoLists(to_node_list(list1), to_node_list(list2))

        assert to_array(result) == [0]

    def test_input_4(self):
        list1 = [1,3,4]
        list2 = [1,2,5,6]

        result = Solution().mergeTwoLists(to_node_list(list1), to_node_list(list2))

        assert to_array(result) == [1,1,2,3,4,5,6]

    def test_input_5(self):
        list1 = [2]
        list2 = [1]

        result = Solution().mergeTwoLists(to_node_list(list1), to_node_list(list2))

        assert to_array(result) == [1,2]


if __name__ == '__main__':
    unittest.main()

