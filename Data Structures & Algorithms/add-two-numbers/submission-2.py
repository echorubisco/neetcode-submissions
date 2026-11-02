# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        quotient = 0
        node = head
        while l1 or l2:
            if l1 and l2:
                sum = l1.val+l2.val+quotient
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                sum = l2.val+quotient
                l2 = l2.next
            elif not l2:
                sum = l1.val+quotient
                l1 = l1.next
            node.next = ListNode(sum%10)
            quotient = sum//10
            node = node.next
        if quotient > 0:
            node.next = ListNode(quotient)
        return head.next