# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev1, curr1 = None, list1
        prev2, curr2 = None, list2
        curr = dummy
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1:
            curr.next = curr1
        else:
            curr.next = curr2
        return dummy.next
            
        