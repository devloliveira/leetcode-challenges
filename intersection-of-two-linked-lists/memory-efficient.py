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


def get_length(head: ListNode)-> int:
    index = 0
    current_node = head
    while current_node is not None:
        current_node = current_node.next
        index += 1
    return index


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_list_a = get_length( headA )
        len_list_b = get_length( headB )

        if len_list_a > len_list_b:
            delta = len_list_a - len_list_b
        else:
            delta = len_list_b - len_list_a

        while delta > 0:
            if len_list_a > len_list_b:
                headA = headA.next
            elif len_list_b > len_list_a:
                headB = headB.next
            delta -= 1

        get_node_id = lambda node: hex( id( node ) )
        iter_node_a = headA
        iter_node_b = headB
        while iter_node_a is not None:
            node_a_id = get_node_id( iter_node_a )
            node_b_id = get_node_id( iter_node_b )
            if node_a_id == node_b_id:
                return iter_node_a

            iter_node_a = iter_node_a.next
            iter_node_b = iter_node_b.next

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
