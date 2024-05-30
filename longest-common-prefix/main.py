from typing import Optional, List

def get_prefix(str1, str2) -> str:
    str1_size = len(str1)
    str2_size = len(str2)

    prefix = list()
    i = 0
    done = False
    while not done:

        try:
            if str1[i] != str2[i]:
                done = True
            else:
                prefix.append(str1[i])
        except IndexError:
            done = True
        i += 1
    return ''.join(prefix)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        if len(strs) == 1:
            return strs[0]

        array_len = len(strs)

        longest_prefix = get_prefix(strs[0], strs[1])
        if not longest_prefix:
            return ''

        i = 0
        while i < array_len:
            longest_prefix = get_prefix(longest_prefix, strs[i])
            if not longest_prefix:
                break
            i += 1
        return longest_prefix

