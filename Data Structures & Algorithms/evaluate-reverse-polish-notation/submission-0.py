'''
#U: input is an array of strings 'token', output is a integer res

    Constraints:
        - 1 <= tokens.length <= 1000.
        - tokens[i] is "+", "-", "*", or "/", or a string 
          representing an integer in the range [-200, 200].
    
    Example:
        Input: tokens = ["1","2","+","3","*","4","-"]

        stack = [1, 2, +]                

#P:
    Strategy: 
        initialize the stack (list)

        for loop to iterate through list:
            if integer is operand (+, -, *, /):
                begin to pop to get digits
                process the operation and store the result
            add to stack
        return result
#I:
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())    
            elif i == "-":
                a , b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif i == "*":
                a , b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif i == "/":
                a , b = stack.pop(), stack.pop()
                stack.append(int((float(b) / a)))
            else:
                stack.append(int(i))
        return stack[0]

                
        