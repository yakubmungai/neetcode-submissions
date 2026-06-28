class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}

        for number in nums:
            if number in frequency_dict:
                frequency_dict[number] += 1
            else:
                frequency_dict[number] = 1

    # Code for sorting, (Learn sorting through a dictionary)

    # Code from ChatGPT

    
     # Step 2: Use a heap to find the top k frequent elements
        # Use (-frequency, number) to simulate a max-heap
        # Note: In Python, heap is a min-heap by default
        heap = []
        for number, frequency in frequency_dict.items():
            heapq.heappush(heap, (-frequency, number))
        
        # Step 3: Extract the top k elements
        top_k_elements = []
        for _ in range(k):
            top_k_elements.append(heapq.heappop(heap)[1])
        
        return top_k_elements

        


        