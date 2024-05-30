import unittest
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_nodelist(array: List[int]) -> ListNode:
    nodes = list()
    for n in array:
        node = ListNode(val=n, next=None)
        if nodes:
            nodes[-1].next = node
        nodes.append(node)
    return nodes[0] if nodes else None


def to_list(head: ListNode) -> List[int]:
    array = list()
    iter = head
    while iter is not None:
        try:
            array.append(iter.val)
            iter = iter.next
        except AttributeError:
            break
    return array


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = list()
        for head in lists:
            array.extend( to_list(head) )
        array.sort()
        return to_nodelist( array )


class Test_solution(unittest.TestCase):
    def test_input_1(self):
        lists = [[1,4,5],[1,3,4],[2,6]]
        expected = [1,1,2,3,4,4,5,6]

        processed_lists = [
            to_nodelist(lists[0]),
            to_nodelist(lists[1]),
            to_nodelist(lists[2]),
        ]
        returned = Solution().mergeKLists(processed_lists)
        
        assert to_list(returned) == expected

    def test_input_2(self):
        lists = []
        expected = []

        processed_lists = []
        returned = Solution().mergeKLists(processed_lists)
        
        assert to_list(returned) == expected

    def test_input_3(self):
        lists = []
        expected = []

        processed_lists = [[]]
        returned = Solution().mergeKLists(processed_lists)
        
        assert to_list(returned) == expected

unittest.main()

