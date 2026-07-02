# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
#U: input is head of a linkedlist, output is a boolean

    objective: find out if there is a cycle, return True or False

#P:                         loop
    input: 1 -> 2 -> 3 -> 4 -> 2
    Strategy:

        Initialize: Create two pointers, slow and fast, both starting at head.

        The Race: Use a while loop that continues as long as the fast car and fast.next 
                  are not None (because the fast car needs to be able to move two steps ahead).

        Move:

            slow = slow.next (1 step)

            fast = fast.next.next (2 steps)

            Collision: If slow == fast, they have met inside a loop. Return True.

        Termination: If the loop finishes (because fast or fast.next hit None), there is no loop. Return False.

#I:
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
        