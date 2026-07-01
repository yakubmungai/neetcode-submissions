'''
#U: input is string 's' of only uppercase letters, and an integer k.
    output is an integer, length of longest substring which contains
    ONLY ONE distinct character. 

    Objective: We can choose up to k characters of the string and replace
               them with any other uppercase English character.

#P: 
                 XX
    Input: s = "XYYXBN", k = 0 , max_len = 4
                l
                   r
    Output: 4

    Strategy:
        initialize a left pointer
        initialize a curr_len variable
        initialize a max_len variable
        initialize a data structure to hold res letters

        for r in range(len(s)):
            if r not in res string:
                if k is 0:
                    left = right
                    right += 1
                k -= 1
            res.append(r)
            curr_len += 1           
#I:


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
'''

'''
#U (Understand)
Goal: Find the longest substring where, with at most k replacements, all characters are the same.

Strategy: Iterate through every possible character (A–Z) and treat it as the "target." For each target, find the longest window that can be formed by replacing non-target characters.

Benefit: This avoids the max(count.values()) calculation inside the loop, making the window logic extremely straightforward.

#P (Plan)
Identify Targets: Get all unique characters in the string (charSet).

Loop Targets: For every character c in charSet:

Reset left = 0 and count = 0 (where count is the number of times c appears in the current window).

Use a right pointer to iterate through the string.

If s[right] == c, increment count.

Check Condition: The number of characters to replace is (window_size - count). If this is > k, we must shrink the window.

If s[left] == c, decrement count as you move left forward.

Update max_res with the current window size (right - left + 1).

Return: max_res.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        count = defaultdict(int)
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_f = max(count.values())

            while ((right - left + 1) - max_f) > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
        