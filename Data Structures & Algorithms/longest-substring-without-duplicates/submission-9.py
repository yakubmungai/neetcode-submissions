'''
#U: input is string 's', output is a integer 'length'.

    objective: find the length of the longest substring without duplicate characters.
               a substring is a contiguous sequence of characters within a string.
    
    CONSTRAINTS: 
        - 0 <= s.length <= 1000
        - s may consist of printable ASCII characters.

#P:
    Strategy: 
        For every letter i, we decide to add it to length if we have not seen it before.

        initialize two pointers, left and right.
        initialize a integer len_cont.
        initialize a seen set.
        add left to seen

        if len(s) is 0:
            return 0
        if len(s) is 1:
            return 1

        while right < len(s) - 1:
            if right not in seen:
                add right to seen set
                increment len_cont variable.
            else:
                len_cont = 1
            
            left = right
            right += 1    


 s="dvdf"  seen = {'d','v', }  len_cont = 2
      lr
    
    output = 3  
#I:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,1
        seen = set()
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        seen.add(s[left])
        print(seen)
        len_cont = 1
        max_len_cont = 0

        # I need to store max_ len so far
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                len_cont += 1
                right += 1
                print("A")
            else:
                len_cont = 1
                left = right
                right += 1 
                print("B")
            print(seen)
            if len_cont > max_len_cont:
                max_len_cont = len_cont
        return max_len_cont
'''

'''
#U (Understand)
Goal: Find the length of the longest substring that contains no duplicate characters.

Constraints: String length up to 1000; can contain any printable ASCII character.

Key Insight: A "sliding window" is needed. The window is defined by a left and right pointer. 
If we encounter a duplicate, we must "shrink" the window from the left until it is valid again, 
rather than resetting the whole thing.

#P (Plan)
Initialize: *Two pointers: left = 0, right = 0.

A seen set to track characters currently in the window.

max_len = 0 to store the longest valid window found.

Iterate: Use a for loop to move the right pointer through every character in the string.

Conflict Resolution: *Before adding s[right] to the set, check if it's already there.

While it's a duplicate, remove s[left] from the set and move left forward. This removes the 
"old" duplicate, making room for the new one.

Update Window: *Add s[right] to the seen set.

Calculate current length: right - left + 1.

Update max_len if the current length is greater.

Return: The max_len.

#I:
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            curr_length = right - left + 1
            max_len = max(curr_length, max_len)
        return max_len






            
        