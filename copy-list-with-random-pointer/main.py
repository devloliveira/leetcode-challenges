"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the
list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value
set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes
in the copied list such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes
x and y in the copied list, x.random --> y.

Return the head of the copied linked list.
"""

from typing import Optional, List
import unittest


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def build_basic_copy(self, node: 'Node') -> 'Node':
        if node:
            copy_node = Node(
                x=node.val,
                next=self.build_basic_copy(node.next),
                random=None
            )

            self.nodes_map[id(node)] = copy_node

            return copy_node
        return None

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        self.nodes_map = dict()
        self.build_basic_copy(head)

        iternode = head
        while iternode is not None:
            mirror_node = self.nodes_map[id(iternode)]

            if iternode.random:
                mirror_random_node = self.nodes_map[id(iternode.random)]
                mirror_node.random = mirror_random_node

            iternode = iternode.next
        
        return self.nodes_map[id(head)]


class Test_solution(unittest.TestCase):

    def test_input_1(self):
        node_1 = Node(1)
        node_2 = Node(2)

        node_1.next = node_2
        node_2.next = None
        node_1.random = node_2
        node_2.random = node_1

        returned_node_1 = Solution().copyRandomList(node_1)

        assert returned_node_1.val == 1
        assert returned_node_1.next.val == 2
        assert returned_node_1.random.val == 2
        assert returned_node_1.next.random.val == 1

    def test_input_2(self):
        node_1 = Node(1)
        node_2 = Node(2)

        node_1.next = node_2
        node_2.next = None
        node_1.random = node_2
        node_2.random = node_2

        returned_node_1 = Solution().copyRandomList(node_1)
        returned_node_2 = returned_node_1.next

        assert returned_node_1.val == 1
        assert returned_node_1.next.val == 2
        assert returned_node_1.random.val == 2

        assert returned_node_1.next.next is None
        assert returned_node_2.random.val == 2

    def test_input_3(self):
        assert Solution().copyRandomList(None) is None


if __name__ == '__main__':
    unittest.main()
