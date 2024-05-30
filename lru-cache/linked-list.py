### IN PROGRESS
"""
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""

import unittest
import time
from typing import List, Dict


class Node:
    def __init__(self, key, val, weight, _next):
        self.key = key
        self.val = val
        self.weight = weight
        self._next = _next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head_node: Node = None
        self.last_node: Node = None
        self.least_used_node: Node = None
        self.size_nodes = 0
        self.current_weight = 0

    def get(self, key: int) -> int:
        # Get the index from the access array
        # based on the key.
        iter_node = self.head_node
        while iter_node is not None:
            if iter_node.key == key:
                self.current_weight += 1
                iter_node.weight = self.current_weight
                return iter_node.val
            iter_node = iter_node._next
        return -1

    def put(self, key: int, value: int) -> None:
        self._create_update_node(key, value)

    def _get_least_used_node(self) -> Node:
        iter = self.head_node
        least_node = None

        while iter is not None:
            if iter.weight == self.current_weight - self.capacity:
                least_node = iter
                break
            iter = iter._next

        return least_node

    def _create_update_node(self, key, val):
        iter = self.head_node
        while iter is not None:
            if iter.key == key:
                iter.val = val
                break
            iter = iter._next

        # If iter is None, that means the node does not exist.
        if iter is None:
            if self.size_nodes < self.capacity:
                if not self.head_node:
                    self.size_nodes += 1
                    self.current_weight += 1
                    self.head_node = Node(key=key, val=val, weight=self.current_weight, _next=None)
                    self.last_node = self.head_node
                else:
                    self.size_nodes += 1
                    self.current_weight += 1
                    node = Node(key=key, val=val, weight=self.current_weight, _next=None)
                    self.last_node._next = node
                    self.last_node = node
            else:
                # We should update the key,val and weight of least used 
                # node
                self.current_weight += 1
                node = self._get_least_used_node()
                node.key = key
                node.val = val
                node.weight = self.current_weight
        else:
            # Node already existed. We should update its weight
            self.current_weight += 1
            iter.weight = self.current_weight

        return iter


class Test_solution(unittest.TestCase):

    def test_input_1(self):
        solution = LRUCache(2)
        solution.put(1, 1)
        solution.put(2, 2)
        assert solution.get(1) == 1
        solution.put(3, 3)
        assert solution.get(2) == -1
        solution.put(4, 4)
        assert solution.get(1) == -1
        assert solution.get(3) == 3
        assert solution.get(4) == 4

    def test_input_2(self):
        solution = LRUCache(2)
        solution.put(2, 1)
        solution.put(2, 2)
        assert solution.get(2) == 2
        solution.put(1, 1)
        solution.put(4, 1)
        assert solution.get(2) == -1

    def test_input_3(self):
        solution = LRUCache(2)
        solution.put(2, 1)
        solution.put(1, 1)
        solution.put(2, 3)
        #import pdb; pdb.set_trace()
        solution.put(4, 1)
        assert solution.get(1) == -1
        assert solution.get(2) == 3

unittest.main()