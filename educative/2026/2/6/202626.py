# https://www.educative.io/interview-prep/coding/valid-palindrome-ii


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
