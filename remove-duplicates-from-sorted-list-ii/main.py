"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/1258890643/
"""

from typing import Optional, List
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev_node = None
        current_node = head
        while getattr(current_node, 'next', None) is not None:
            if current_node.val == current_node.next.val:
                iter_node = current_node.next
                while iter_node is not None:
                    if iter_node.val != current_node.val:
                        break
                    iter_node = iter_node.next

                if prev_node is not None:
                    prev_node.next = iter_node
                    current_node = prev_node
                else:
                    head = iter_node
                    current_node = iter_node
                    prev_node = None

            else:
                prev_node = current_node
                current_node = current_node.next if current_node else None
        return head


class Test_solution(unittest.TestCase):
    def to_nodelist(self, array: List[int]) -> List[ListNode]:
        nodes = list()
        for n in array:
            node = ListNode(val=n, next=None)
            if nodes:
                nodes[-1].next = node
            nodes.append(node)
        return nodes

    def to_list(self, head: ListNode) -> List[int]:
        array = list()
        iter = head
        while iter is not None:
            array.append(iter.val)
            iter = iter.next
        return array

    def test_input_1(self):
        _input = [1,2,3,3,4,4,5]
        expected =[1,2,5]
        returned = Solution().deleteDuplicates( self.to_nodelist(_input)[0] )
        returned = self.to_list(returned)

        assert returned == expected, f'{expected} == {returned}'

    def test_input_2(self):
        _input = [1,1,1,2,3]
        expected =[2,3]
        returned = Solution().deleteDuplicates( self.to_nodelist(_input)[0] )
        returned = self.to_list(returned)

        assert returned == expected, f'{expected} == {returned}'

    def test_input_3(self):
        _input = [1,1]
        expected =[]
        returned = Solution().deleteDuplicates( self.to_nodelist(_input)[0] )
        returned = self.to_list(returned)

        assert returned == expected, f'{expected} == {returned}'

    def test_input_4(self):
        _input = []
        expected =[]
        returned = Solution().deleteDuplicates( _input )
        returned = self.to_list(returned)

        assert returned == expected, f'{expected} == {returned}'


unittest.main()
