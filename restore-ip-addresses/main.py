"""
https://leetcode.com/problems/restore-ip-addresses/description/

A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive)
and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
"""

from typing import List

class IPUtils:
    def is_valid_ipv4(self, msg):
        groups = msg.split('.')
        try:
            assert len(groups) == 4
            assert all([
                group.isdigit() and (int(group) >= 0 and int(group) <= 255)
                for group in groups
            ])
            assert all([
                (group.startswith('0') and len(group) == 1) or (not group.startswith('0'))
                for group in groups
            ])

            return True
        except AssertionError:
            return False


class Solution(IPUtils):

    def get_group(self, msg: str, start_index: int=0):
        try:
            return msg[start_index], msg[start_index:start_index+2], msg[start_index:start_index+3]
        except IndexError:
            return ''

    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        for g1 in self.get_group(s, start_index=0):
            for g2 in self.get_group(s, start_index=len(g1)):
                for g3 in self.get_group(s, start_index=len(g1+g2)):
                    for g4 in self.get_group(s, start_index=len(g1+g2+g3)):
                        if len(g1+g2+g3+g4) == len(s):
                            ip = f'{g1}.{g2}.{g3}.{g4}'
                            if self.is_valid_ipv4(ip):
                                ips.append(ip)
        return list(set(ips))


import unittest
class Test__solution(unittest.TestCase):

    def test_input_1(self):
        s = '25525511135'
        expected = set(["255.255.11.135","255.255.111.35"])
        returned = Solution().restoreIpAddresses(s)
        assert expected == set(returned), f'{expected} != {set(returned)}'

    def test_input_2(self):
        s = '0000'
        expected = set(["0.0.0.0"])
        returned = Solution().restoreIpAddresses(s)
        assert expected == set(returned), f'{expected} != {set(returned)}'

    def test_input_3(self):
        s = '101023'
        expected = set(["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])
        returned = Solution().restoreIpAddresses(s)
        assert expected == set(returned), f'{expected} != {set(returned)}'

if __name__ == '__main__':
    unittest.main()
