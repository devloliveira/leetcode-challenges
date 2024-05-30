"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

from typing import Optional, List
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_length(head: ListNode) -> int:
    i = 0
    current_node = head
    while current_node is not None:
        current_node = current_node.next
        i += 1
    return i


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        visited_nodes = []
        max_kept_nodes = n + 3
        current_node = head
        while current_node is not None:
            if len(visited_nodes) == (max_kept_nodes):
                del visited_nodes[0]

            visited_nodes.append(current_node)

            current_node = current_node.next

        # Calculate the indexes of the nodes we should consider
        target_node_pos = (n*-1)
        prev_node_pos = (n*-1) - 1
        next_node_pos = (n*-1) + 1

        # Once we have the indexes, we should try to get the actual
        # nodes.
        prev_node = None
        next_node = None
        target_node = None

        target_node = visited_nodes[target_node_pos]
        try:
            prev_node = visited_nodes[prev_node_pos]
        except IndexError:
            # We dont have a previous node. That means the target node
            # is likely the head.
            pass

        try:
            assert next_node_pos < 0
            next_node = visited_nodes[next_node_pos]
        except (AssertionError, IndexError):
            # We dont have a node after the target node. That means
            # the target node is likely the tail.
            pass

        # The following blocks establishes the logic of removing the
        # node and returning the correct ListNode.
        if prev_node:

            if next_node:
                prev_node.next = next_node
            else:
                prev_node.next = None

            return head

        else:
            if next_node:
                return next_node
            else:
                return None


class Test_solution(unittest.TestCase):
    def to_node_list(self, list1: List[int]) -> List[ListNode]:
        nodes:List[ListNode] = []

        for n in list1:
            current_node = ListNode(val=n, next=None)

            try:
                nodes[-1].next = current_node
            except IndexError:
                pass

            nodes.append(current_node)

        return nodes if nodes else None


    def to_array(self, head: ListNode) -> List[int]:
        result: List[int] = []
        current_node = head
        while current_node is not None:
            result.append(current_node.val)
            current_node = current_node.next
        
        return result

    def test_input_1(self):
        head = [1,2,3,4,5]
        n = 2

        result = Solution().removeNthFromEnd( self.to_node_list(head)[0], n )
        assert self.to_array(result) == [1,2,3,5]

    def test_input_2(self):
        head = [1]
        n = 1

        result = Solution().removeNthFromEnd( self.to_node_list(head)[0], n )
        assert self.to_array(result) == []

    def test_input_3(self):
        head = [1, 2]
        n = 1

        result = Solution().removeNthFromEnd( self.to_node_list(head)[0], n )
        assert self.to_array(result) == [1]

    def test_input_4(self):
        head = [1,2,3,4]
        n = 4

        result = Solution().removeNthFromEnd( self.to_node_list(head)[0], n )
        assert self.to_array(result) == [2,3,4]


if __name__ == '__main__':
    unittest.main()
