'''
#U (Understand)
Goal: Determine if a permutation of s1 exists within s2.
Permutation: A rearrangement of letters. This means the substring in s2 must have the exact same character frequencies as s1.

Key Constraint: The substring must be contiguous (neighboring).

Efficiency: We need a way to compare frequency counts in $O(1)$ time rather than sorting strings every time.

#P (Plan)

Base Case: If len(s1) > len(s2), return False.

Frequency Maps: Create two Hash Maps (dictionaries):
    s1_count: Stores character counts for s1.
    window_count: Stores character counts for the current window of size len(s1) in s2.
    
    Initialize: Fill s1_count and the first window of window_count.
    
    Slide:Loop through s2, adding the next character to the window and removing the oldest character (the one at the left pointer).
    
    Compare the two maps at every step. If they are equal, return True.
    
    Clean Up: If a count drops to 0, del that key from the dictionary so the == comparison works correctly.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])
        
        left = 0
        for right in range(len(s1), len(s2)):
            if s1_count == window_count:
                return True
            
            # Add new character
            window_count[s2[right]] += 1
            # Remove old character
            window_count[s2[left]] -= 1
            
            # Clean up map
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]
                
            left += 1
            
        return s1_count == window_count