# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
#U: input is the 'head' of a linked list. Output is 'head' of reversed list.

    objective: reverse the linkedlist

    CONSTRAINTS:
        - 0 <= The length of the list <= 1000.
        - -1000 <= Node.val <= 1000

 #P:     <-
        0 -> 1  2 -> 3 -> null
  prev curr nxt

   initialize three pointers prev, curr, nxt

   while curr->next is not equal to null
    set nxt to curr's next
    set curr's next to prev
    set prev to curr
    set curr to nxt
   return curr

#I:
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        