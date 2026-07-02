# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
#U: input is two heads of sorted linked lists. output is head of a linked list

    objective: merge two sorted input lists into one sorted linked list
#P:

    Initialize: Create a dummy = ListNode(0) and a tail = dummy. The tail pointer will always track the
                last node of your new, merged list.

    Comparison Loop: Use while list1 and list2: (this handles the case where both lists have items).

    Attach: * If list1.val <= list2.val: tail.next = list1, then list1 = list1.next.

              Else: tail.next = list2, then list2 = list2.next.

    Advance Tail: Always move your tail pointer forward after attaching: tail = tail.next.

    The Remainder: After the loop, one list might still have nodes left. Simply point tail.next
                   to the remaining list (list1 or list2).

    Return: Return dummy.next (because the actual merged list starts after the dummy).
#I:
'''


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next
        