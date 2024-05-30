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
from typing import List, Dict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapping: Dict[int] = dict()
        self.access_array: List[int] = list()
        self.total_keys = 0

    def refresh_access_array(self, key):
        self.access_array.insert(0, key)
        i = 1
        done = False
        while not done:
            try:
                if self.access_array[i] == key:
                    self.access_array.pop(i)
                    done = True
                else:
                    i += 1
            except IndexError:
                # The key does not exist !?
                done = True

    def evict_key(self, key):
        del self.mapping[key]
        self.access_array.remove(key)
        self.total_keys -= 1

    def get(self, key: int) -> int:
        # Get the index from the access array
        # based on the key.
        try:
            value = self.mapping[key]
            self.refresh_access_array(key)
        except KeyError:
            value = -1
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.access_array:
            if self.total_keys == self.capacity:
                key_to_remove = self.access_array[-1]
                self.evict_key( key_to_remove )

            self.mapping[key] = value
            self.total_keys += 1
            self.access_array.insert(0, key)
        else:
            self.mapping[key] = value
            self.refresh_access_array(key)


class Test_solution(unittest.TestCase):
    def test_input_1(self):
        solution = LRUCache(2)
        solution.put(2, 1)
        solution.put(2, 2)
        assert solution.get(2) == 2
        solution.put(1, 1)
        solution.put(4, 1)
        assert solution.get(2) == -1

    def test_input_2(self):
        solution = LRUCache(2)
        solution.put(2, 1)
        solution.put(1, 1)
        solution.put(2, 3)
        #import pdb; pdb.set_trace()
        solution.put(4, 1)
        assert solution.get(1) == -1
        assert solution.get(2) == 3


unittest.main()