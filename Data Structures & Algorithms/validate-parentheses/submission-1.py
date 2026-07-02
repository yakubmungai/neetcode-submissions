'''
#U: input is integer string 's' of parentheses (', ')', '{', '}', '[' or ']'.
   output is a boolean True or False

   objective: determine the validity of s, valid if and only if:

        - Every open bracket is closed by the same type of close bracket.
        - Open brackets are closed in the correct order.
        - Every close bracket has a corresponding open bracket of the same type.
#P:

    
#I:
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # keys are closing brackets, values are opening brackets
        brackets_map = {')': '(', '}': '{', ']': '['} 
        stack = []

        for char in s:
            # If a closing bracket found
            if char in brackets_map:
                if stack and stack[-1] == brackets_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                # If an opening bracket found
                stack.append(char)
        
        if stack:
            return False
        else:
            return True
        


            


                                                        
        