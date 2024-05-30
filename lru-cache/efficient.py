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
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = OrderedDict()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        try:
            self.mapping.move_to_end(key)
            return self.mapping[key]
        except KeyError:
            pass

        return -1

    def put(self, key: int, value: int) -> None:
        is_new_key = True if key not in self.mapping.keys() else False

        if is_new_key:
            if self.size < self.capacity:
                self.size += 1
                self.mapping[key] = value
            else:
                for least_used_key in self.mapping.keys():
                    break
                del self.mapping[least_used_key]
                self.mapping[key] = value
        else:
            self.mapping[key] = value
            self.mapping.move_to_end(key)

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