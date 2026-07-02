'''
#U:
    Objective: Design a stack that supports push, pop, top, and getMin operations, all in O(1) time.

    The Challenge: Tracking the current minimum when the stack contents change, especially when the 
                   minimum value is popped.
#P:
    Strategy:

      State Management: Keep a stack for the relative values and a self.min variable to track the absolute 
                        minimum value currently in the stack.

    Push Strategy:
        - If the stack is empty, store 0 and set self.min = val.

        - If not empty, store the difference (val - self.min).

        - If the new val is smaller than the current min, update self.min = val.  

    Pop Strategy:

        - Retrieve the relative value (pop).

        - If the popped value is negative, it means the popped value was the current minimum. 
          We must "undo" the minimum change by calculating self.min = self.min - pop to restore 
          the previous minimum.

    Top Strategy:

        - If the relative value is positive, the actual value is self.min + relative_value.

        - If the relative value is 0 or negative, the actual value is self.min.

        - GetMin Strategy: Simply return the tracked self.min.
#I:
'''


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        # stack empty
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack: return

        pop = self.stack.pop()

        # If pop < 0, we are removing the current minimum
        if pop < 0:
            # Restore the previous minimum
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        # If relative value is > 0, the real value is min + diff
        if top > 0:
            return top + self.min
        else:
            # If relative value is <= 0, the min is the top value
            return self.min

    def getMin(self) -> int:
        return self.min
        
