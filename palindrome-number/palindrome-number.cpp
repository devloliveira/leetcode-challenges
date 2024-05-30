// https://leetcode.com/problems/palindrome-number/

#include <iostream>
#include <string>
#include <sstream>


class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0)
            return false;

        std::string string_x = "";
        std::stringstream stream;
        stream << x;
        stream >> string_x;

        int len_digits = string_x.size();
        int i = 0;
        int j = len_digits - 1;
        bool is_palindrome = true;
        while( i < len_digits ) {
            if ( string_x[i] != string_x[j] ) {
                is_palindrome = false;
                break;
            }

            i += 1;
            j -= 1;
        }

        return is_palindrome;
    }
};


int
main(int argc, char* argv[]) {
    bool result = Solution().isPalindrome( std::stoi(argv[1]) );
    std::cout << result << "\n";
}