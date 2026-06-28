"""
U: input is array of strings, output is anagrams in sublists.

P: I will (
- Initialize a dictionary
- Loop each word in strs.
- For each word, count its characters using list of 26 zeros.
- Convert list into tuple so it can be a key
- Append the word to the matching key in your dictionary.
)


I:
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
            

        