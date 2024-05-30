"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
"""

from typing import Optional, List
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_ids_first_list = set()
        current_node = headA

        get_node_id = lambda node: hex( id( node ) )
        while current_node is not None:
            node_id = get_node_id( current_node )
            visited_ids_first_list.add( node_id )
            current_node = current_node.next

        current_node = headB
        while current_node is not None:
            node_id = get_node_id( current_node )
            if node_id in visited_ids_first_list:
                return current_node
            current_node = current_node.next

        return None


def to_node_list(list1: List[int]) -> List[ListNode]:
    nodes:List[ListNode] = []

    for n in list1:
        current_node = ListNode(val=n, next=None)

        try:
            nodes[-1].next = current_node
        except IndexError:
            pass

        nodes.append(current_node)

    return nodes if nodes else None


def to_array(head: ListNode) -> List[int]:
    result: List[int] = []
    current_node = head
    while current_node is not None:
        result.append(current_node.val)
        current_node = current_node.next
    
    return result


class Test_solution(unittest.TestCase):

    def test_input_1(self):
        listA = to_node_list([4,1,8,4,5])
        listB = to_node_list([5,6,1,8])

        listB[-1].next = listA[2]

        result = Solution().getIntersectionNode( listA[0], listB[0] )
        assert result.val == 8

    def test_input_2(self):
        listA = to_node_list([1,9,1,2,4])
        listB = to_node_list([3])

        listB[-1].next = listA[3]

        result = Solution().getIntersectionNode( listA[0], listB[0] )
        assert result.val == 2

    def test_input_3(self):
        listA = to_node_list([2,6,4])
        listB = to_node_list([1,5])

        result = Solution().getIntersectionNode( listA[0], listB[0] )
        assert result is None


if __name__ == '__main__':
    unittest.main()
