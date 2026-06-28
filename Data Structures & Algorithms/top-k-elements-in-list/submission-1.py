'''
U: input is an integer array, and an int k, output is list of k most frequent in the array.

P: I'll initialize  a seen hashmap with num as key and frequency as value. I'll convert that hashmap to
a list then sort it by frequencies then output k most frequent.

I:
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_map = {}
        res = []

        for num in nums:
            if num not in seen_map:
                seen_map[num] = 0
            seen_map[num] += 1
        
        items_list = list(seen_map.items())
        items_list.sort(key=lambda item: item[1], reverse=True)

        for num, val in items_list:
            res.append(num)
            k = k - 1
            if k == 0:
                return res

        