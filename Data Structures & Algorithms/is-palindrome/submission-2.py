'''
#U: input is a string s, and output is a boolean whether or
not it's a palindrome.

palindrome - a string that reads the same forward and backward,
does not matter if capital or not.

input: "Was it a car or a cat I saw?"

output: true

#P:
Strategy: 

    initialize two pointers, one at start and one at end.

    while right > left:
        if either pointer is not between ascii 97-122, or 65-90 then move pointers

        compare the letters at the two pointers (compare their ord()),
        if equal then move pointers, if not return false immediately.

    return true
#I:
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while right > left:
            # 1. Skip if left is not alphanumeric (48-57: 0-9, 65-90: A-Z, 97-122: a-z)
            if not ((48 <= ord(s[left]) <= 57) or (65 <= ord(s[left]) <= 90) or (97 <= ord(s[left]) <= 122)):
                left += 1
            # 2. Skip if right is not alphanumeric
            elif not ((48 <= ord(s[right]) <= 57) or (65 <= ord(s[right]) <= 90) or (97 <= ord(s[right]) <= 122)):
                right -= 1
            # 3. Compare using .lower() directly on the characters
            else:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
        return True



        

        