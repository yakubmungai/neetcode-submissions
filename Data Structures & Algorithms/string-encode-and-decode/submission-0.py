class Solution:

    def encode(self, strs: List[str]) -> str:
        # Initialize an empty string to build the encoded result
        res_string = ""
        
        # Iterate through each word in the list of strings
        for word in strs:
            # Append the length of the word, a delimiter (#), and the word itself to the result string
            res_string += str(len(word)) + "#" + word
        
        # Return the final encoded string
        return res_string

    def decode(self, s: str) -> List[str]:
        # Initialize an empty list to store the decoded strings
        res = []
        
        # Initialize index i to 0, which will be used to traverse the encoded string
        i = 0  

        # Loop until we have processed the entire encoded string
        while i < len(s):
            # Initialize j to the current value of i
            j = i
            
            # Traverse the encoded string to find the delimiter (#) that marks the end of the length prefix
            while s[j] != '#':
                # Increment j to move to the next character
                j += 1
            
            # Convert the substring s[i:j] (which contains the length) to an integer
            length = int(s[i:j])
            
            # Update i to point to the first character of the actual word (right after the # delimiter)
            i = j + 1
            
            # Update j to point to the end position of the current word (i + length)
            j = i + length
            
            # Append the substring s[i:j] (the actual word) to the result list
            res.append(s[i:j])
            
            # Update i to j to start processing the next encoded string in the next iteration
            i = j
        
        # Return the list of decoded strings
        return res
