# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
#U: input is head of a linkedlist, output is head of same linkedlist
    
    objective: remove the nth node from list

#P:                  p c
    Input: head = [1,2,3,4], n = 2

    Output: [1,2,4]

    Strategy: 
        
        #P (Plan): The Runner Technique
            The "Dummy" Anchor: Create a dummy node that points to head. 
            This allows you to handle cases where the head is the node being removed 
            without needing complex if statements.

            The Gap: Create two pointers, left and right. Position them so that the right 
            pointer is exactly n steps ahead of left (starting right at the head and left 
            at dummy).

            The Slide: Advance both pointers one step at a time until the right pointer 
            reaches None. Because of the n-step gap, the left pointer will now be resting 
            on the node immediately before the target node.

            The Extraction: Perform the removal: left.next = left.next.next. This "skips" 
            the target node, effectively deleting it from the chain.

            The Result: Return dummy.next (the actual head of the list, which remains valid 
            even if the original head was deleted).
#I:
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left, right = dummy, head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next
        

        left.next = left.next.next
        return dummy.next

        



        