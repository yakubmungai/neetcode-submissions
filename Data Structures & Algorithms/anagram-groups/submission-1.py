#class Solution:
 #   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Iterate through array of strings
            # For each string,
                # Set the corresponding ascii string to 1 if letter in string
                    # Iterate through all other strings
                        # For all the other strings, decrement if letter in string
                    
                    # Check is ascii string is all 0
                        # If yes then add to 2D Array

  #      ascii_arr = [0] * 255
    
   #     for i in range(len(strs)):
    #        for char in strs[i]:
     #           ascii_arr[ord[char]] = 1

#            for j in range(i+1,len(strs)):
 #               for char in strs[j]:
  #                  if ascii_arr[ord(char)] == 1:
   #                     ascii_arr[ord(char)] = 0
            
    #        for k in range(len(strs)):
     #           if ascii_arr[k] != 0:
      #              return False
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

# Create a dictionary where the frequency count of each word is the key
# Note: convert ascii 0-255 to letter indexes 0-25