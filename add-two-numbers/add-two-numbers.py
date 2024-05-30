# https://leetcode.com/problems/add-two-numbers/

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""

import unittest
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list_from_number(number: str, reverse=False) -> ListNode:
    digit_array = [
        c
        for c in number
    ]

    if reverse:
        digit_array.reverse()

    nodes = []
    for digit in digit_array:
        nodes.append(ListNode(val=int(digit)))

    i = 0
    while i < len(nodes) - 1:
        nodes[i].next = nodes[i+1]
        i += 1

    return nodes


def listnode_to_string(head: ListNode) -> int:
    digits = [str(head.val)]
    iter: ListNode = head
    while iter.next is not None:
        iter = iter.next
        digits.append(str(iter.val))

    return ''.join(digits)


def listnode_to_number(head: ListNode) -> int:
    return int(''.join(listnode_to_string(head)))


def reverse_digits(number: int) -> int:
    digit_array = [
        c
        for c in str(number)
    ]

    digit_array.reverse()

    return int(''.join(digit_array))


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            first_number = listnode_to_string(l1)
            second_number = listnode_to_string(l2)

            reversed_first = reverse_digits(first_number)
            reversed_second = reverse_digits(second_number)

            result = reversed_first + reversed_second
        elif l1:
            first_number = listnode_to_number(l1)
            result = reverse_digits(first_number)
        elif l2:
            second_number = listnode_to_number(l1)
            result = reverse_digits(second_number)

        return build_linked_list_from_number(str(result), reverse=True)[0]


class Test__build_linked_list(unittest.TestCase):
    def test__input1(self):
        nodes = build_linked_list_from_number('123')
        assert len(nodes) == 3
        assert nodes[0].val == 1
        assert nodes[1].val == 2
        assert nodes[2].val == 3

    def test__input2(self):
        nodes = build_linked_list_from_number('0')
        assert len(nodes) == 1
        assert nodes[0].val == 0


class Test__listnode_to_number(unittest.TestCase):
    def test__input1(self):
        nodes = build_linked_list_from_number('123')
        assert listnode_to_number(nodes[0]) == 123

    def test__input2(self):
        nodes = build_linked_list_from_number('123', reverse=True)
        assert listnode_to_number(nodes[0]) == 321

    def test__input3(self):
        nodes = build_linked_list_from_number('0')
        assert listnode_to_number(nodes[0]) == 0


class Test__Solution(unittest.TestCase):
    def test_case_1(self):
        l1 = build_linked_list_from_number('243')
        l2 = build_linked_list_from_number('564')
        solution_head = Solution().addTwoNumbers(l1[0], l2[0])
        assert listnode_to_number(solution_head) == 708

    def test_case_2(self):
        l1 = build_linked_list_from_number('0')
        l2 = build_linked_list_from_number('0')
        solution_head = Solution().addTwoNumbers(l1[0], l2[0])
        assert listnode_to_number(solution_head) == 0

    def test_case_3(self):
        l1 = build_linked_list_from_number('9999999')
        l2 = build_linked_list_from_number('9999')
        solution_head = Solution().addTwoNumbers(l1[0], l2[0])
        assert listnode_to_number(solution_head) == 89990001

    def test_case_4(self):
        l1 = build_linked_list_from_number('086568357')
        l2 = build_linked_list_from_number('678085897')
        solution_head = Solution().addTwoNumbers(l1[0], l2[0])
        assert listnode_to_number(solution_head) == 6556442551

    def test_case_5(self):
        l1 = build_linked_list_from_number('123')
        solution_head = Solution().addTwoNumbers(l1[0], None)
        assert listnode_to_number(solution_head) == 123


if __name__ == '__main__':
    unittest.main()
