"""
https://leetcode.com/problems/defanging-an-ip-address/
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


import unittest

class TestSolution(unittest.TestCase):
    def test_input_1(self):
        assert Solution().defangIPaddr('1.1.1.1') == '1[.]1[.]1[.]1'

    def test_input_2(self):
        assert Solution().defangIPaddr('255.100.50.0') == '255[.]100[.]50[.]0'

if __name__ == '__main__':
    unittest.main()