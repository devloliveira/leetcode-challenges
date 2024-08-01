"""
https://leetcode.com/problems/validate-ip-address/description/

Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

    1 <= xi.length <= 4
    xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
    Leading zeros are allowed in xi.

For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
"""


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        strategies = (
            (self.validate_ipv4, 'IPv4'),
            (self.validate_ipv6, 'IPv6'),
        )

        for strategy, strategy_name in strategies:
            try:
                strategy(queryIP)
                return strategy_name
            except AssertionError:
                pass

        return 'Neither'

    def validate_ipv4(self, queryIP: str):
        groups = queryIP.split('.')
        assert len(groups) == 4
        assert all(group.isdigit() for group in groups)
        assert all([
            not group.startswith('0') or (group.startswith('0') and len(group) == 1)
            for group in groups
        ])

        int_groups = [int(group) for group in groups]
        assert all([
            (group >= 0 and group <= 255)
            for group in int_groups
        ])

    def validate_ipv6(self, queryIP: str):
        valid_numbers = [str(i) for i in range(10)]
        valid_lower_chars = ['a', 'b', 'c', 'd', 'e', 'f']
        valid_upper_chars = ['A', 'B', 'C', 'D', 'E', 'F']
        valid_characters = valid_numbers + valid_lower_chars + valid_upper_chars

        groups = queryIP.split(':')
        assert len(groups) == 8
        assert all([
            len(group) >= 1 and len(group) <= 4
            for group in groups
        ])

        for group in groups:
            for char in group:
                assert char in valid_characters


import unittest


class Test_solution(unittest.TestCase):
    def test_input_1(self):
        assert Solution().validIPAddress('172.16.254.1') == 'IPv4'

    def test_input_2(self):
        assert Solution().validIPAddress('2001:0db8:85a3:0:0:8A2E:0370:7334') == 'IPv6'

    def test_input_3(self):
        assert Solution().validIPAddress('256.256.256.256') == 'Neither'

    def test_input_4(self):
        assert Solution().validIPAddress('255.255.255.0') == 'IPv4'

if __name__ == '__main__':
    unittest.main()