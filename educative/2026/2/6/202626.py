# https://www.educative.io/interview-prep/coding/valid-palindrome-ii


# First solution
def palindrome_check(substring):
    l, r = 0, len(substring) - 1
    while l < r:
        if substring[l] == substring[r]:
            pass
        else:
            return False
        l += 1
        r -= 1
    return True


def is_palindrome(string):
    index = 0
    while index < len(string):
        substring = string[0:index] + string[index + 1 : len(string)]
        print(substring)
        if palindrome_check(substring):
            return True
        index += 1
    return False


# https://leetcode.com/problems/valid-palindrome-ii/
# Optimal solution


class Solution:
    def palindrome_check(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.palindrome_check(
                    s, left + 1, right
                ) or self.palindrome_check(s, left, right - 1)

            left += 1
            right -= 1
        return True
