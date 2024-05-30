// https://leetcode.com/problems/longest-common-prefix/

/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:
    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

*/
#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>


std::string extract_pattern(std::string a, std::string b) {
    int i = 0;
    std::string pattern = "";

    int a_size = a.size();
    int b_size = b.size();

    while( i < a_size && i < b_size ) {
        if( a[i] == b[i] )
            pattern += a[i];

        i += 1;
    }

    return pattern;
}


std::string extract_pattern_from_list(std::vector <std::string> array) {
    std::string current_pattern = "";

    if( array.size() >= 2 ) {
        current_pattern = extract_pattern(array[0], array[1]);
    } else {
        current_pattern = array[0];
    }

    int i = 0;
    while( i < (array.size() - 1) ) {
        current_pattern = extract_pattern(current_pattern, array[i+1]);
        i += 1;
    }

    return current_pattern;
}


class Solution {
public:
    std::string longestCommonPrefix(std::vector<std::string>& strs) {
        return extract_pattern_from_list(strs);
    }
};



int main(int argc, char *argv[]) {
    std::vector <std::string> array;

    array.push_back("abc");
    array.push_back("abcde");
    array.push_back("a");
    array.push_back("ab");
    array.push_back("shoiz");

    std::cout << Solution().longestCommonPrefix(array) << "\n";
}