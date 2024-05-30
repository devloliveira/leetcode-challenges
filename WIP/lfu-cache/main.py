"""
IN PROGRESS
https://leetcode.com/problems/lfu-cache/
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

    LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
"""

import unittest


class DataNode:
    def __init__(self, key, val, use_counter, _prev=None, _next=None):
        self.key = key
        self.val = val
        self.use_counter = use_counter
        self.prev = _prev
        self.next = _next


class LFUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.total_nodes = 0
        self.capacity = capacity
        self.size = 0

    def _move_to_end(self, node):
        if node != self.head and node != self.tail:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

        elif self.head != self.tail and node == self.head:
            new_head = self.head.next
            new_head.prev = None

            self.tail.next = node

            node.prev = self.tail
            node.next = None

            self.tail = node
            self.head = new_head


    def get(self, key: int) -> int:
        iter = self.head
        while iter != None:
            if iter.key == key:
                iter.use_counter += 1
                self._move_to_end(iter)
                return iter.val
            iter = iter.next
        return -1

    def put(self, key: int, value: int) -> None:
        iter = self.head
        has_key = False

        least_used_node = None
        while iter != None:
            if not least_used_node:
                least_used_node = iter
            elif least_used_node.use_counter > iter.use_counter:
                least_used_node = iter
            if iter.key == key:
                has_key = True
                iter.val = value
                iter.use_counter += 1
                break

            iter = iter.next

        # This is a new key
        if not has_key:
            node = DataNode(key=key, val=value, use_counter=1, _prev=None, _next=None)
            if self.total_nodes < self.capacity:
                self.total_nodes += 1
                if not self.head:
                    self.head = node
                    self.tail = node
                else:
                    node.prev = self.tail
                    self.tail.next = node
                    self.tail = node
            else:
                # Evict least used key
                if self.capacity > 1:
                    is_at_edge = False
                    if least_used_node == self.head:
                        is_at_edge = True
                        self.tail.next = node
                        node.prev = self.tail
                        self.tail = node

                        self.head = self.head.next
                        self.head.prev = None
                    if least_used_node == self.tail:
                        is_at_edge = True
                        prev_node = self.tail.prev
                        prev_node.next = node
                        node.prev = prev_node
                        self.tail = node

                    if not is_at_edge:
                        prev_node = least_used_node.prev
                        next_node = least_used_node.next

                        prev_node.next = next_node
                        next_node.prev = prev_node
                else:
                    self.head = node
                    self.tail = node

    def dbg(self):
        iter = self.head
        print(f'Head: {self.head.key} | Tail: {self.tail.key}')
        while iter != None:
            print(f'({self.total_nodes}) {iter.key} - {iter.val} - {iter.use_counter} ({iter.prev})')
            iter = iter.next


class Test_solution(unittest.TestCase):

    def _parse_input(self, ops, values):
        capacity = values[0][0]
        i = 1
        lfu = LFUCache(capacity)
        results = [None]
        while i < len(ops):
            op = ops[i]
            if op == 'put':
                key, value = values[i]
                lfu.put(key, value)
                results.append(None)
            elif op == 'get':
                value = values[i][0]
                result = lfu.get(value)
                results.append(result)
            i += 1
        return results

    def test_input_1(self):
        expected = [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
        returned = self._parse_input(
            ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
        )
        assert expected == returned

    def test_input_2(self):
        lfu = LFUCache(1)
        lfu.put(1, 1)
        assert lfu.get(1) == 1
        assert lfu.get(2) == -1
        lfu.put(2, 2)
        assert lfu.get(1) == -1
        assert lfu.get(2) == 2
        lfu.put(3, 3)
        assert lfu.get(1) == -1
        assert lfu.get(2) == -1
        assert lfu.get(3) == 3

    def test_input_3(self):
        lfu = LFUCache(3)
        lfu.put(1, 1)
        assert lfu.get(1) == 1 # usg 2
        assert lfu.get(2) == -1
        lfu.put(2, 2)
        assert lfu.get(1) == 1 # usg 3
        assert lfu.get(2) == 2 # usg 2
        lfu.put(3, 3)
        assert lfu.get(1) == 1 # usg 4
        assert lfu.get(2) == 2 # usg 3
        assert lfu.get(3) == 3 # usg 2
        lfu.put(4, 4)
        assert lfu.get(1) == 1 # usg 5
        assert lfu.get(2) == 2 # usg 4
        assert lfu.get(3) == -1
        assert lfu.get(4) == 4

    def test_input_4(self):
        lfu = LFUCache(3)
        lfu.put(1, 1)
        lfu.put(2, 2)
        lfu.put(3, 3)
        assert lfu.get(1) == 1
        assert lfu.get(2) == 2
        assert lfu.get(3) == 3
        lfu.put(4, 4)
        assert lfu.get(1) == -1
        lfu.put(5, 5)
        assert lfu.get(4) == -1
        assert lfu.get(2) == 2
        assert lfu.get(3) == 3
        assert lfu.get(5) == 5

    def test_input_5(self):
        lfu = LFUCache(2)
        lfu.put(2, 1)
        lfu.put(3, 2)

        assert lfu.head.key == 2
        assert lfu.tail.key == 3

        assert lfu.get(3) == 2

        assert lfu.head.key == 2
        assert lfu.tail.key == 3

        assert lfu.get(2) == 1
        assert lfu.head.key == 3
        assert lfu.tail.key == 2


        lfu.put(4, 3)
        assert lfu.head.key == 2
        assert lfu.tail.key == 4

        assert lfu.get(2) == 1
        assert lfu.get(3) == -1
        assert lfu.get(4) == 3

    def test_input_6(self):
        expected = [None,None,None,None,None,None,-1,None,19,17,None,-1,None,None,None,-1,None,-1,5,-1,12,None,None,3,5,5,None,None,1,None,-1,None,30,5,30,None,None,None,-1,None,-1,24,None,None,18,None,None,None,None,14,None,None,18,None,None,11,None,None,None,None,None,18,None,None,-1,None,4,29,30,None,12,11,None,None,None,None,29,None,None,None,None,17,-1,18,None,None,None,-1,None,None,None,20,None,None,None,29,18,18,None,None,None,None,20,None,None,None,None,None,None,None]
        returned = self._parse_input(
            ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
            [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
        )

        assert expected == returned

unittest.main()
"""

["LFUCache","put",   "put",  "put",   "put",   "put",   "get",  "put",   "get",  "get",  "put",   "get",  "put",   "put",  "put",   "get",  "put",   "get",  "get",  "get",  "get",  "put",   "put",  "get",  "get",  "get",  "put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"],
[   [10],   [10,13],[3,17],  [6,11],  [10,5],  [9,10],  [13],   [2,19],  [2],    [3],    [5,25],  [8],    [9,22],  [5,5],  [1,30],  [11],   [9,12],  [7],    [5],    [8],    [9],    [4,30],  [9,3],  [9],    [10],   [10],   [6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

"""