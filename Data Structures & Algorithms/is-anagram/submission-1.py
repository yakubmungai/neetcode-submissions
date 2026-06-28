class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ascii_array = [0] * 256

        for char in s:
            ascii_array[ord(char)] += 1

        for char in t:
            ascii_array[ord(char)] -= 1

        for count in ascii_array:
            if count != 0:
                return False
        return True

# Space Complexity: O(1)
# Time Complexity: O(n)
        


            