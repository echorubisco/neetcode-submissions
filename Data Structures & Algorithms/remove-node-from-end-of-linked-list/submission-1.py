# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        length = 0
        pointer = head
        node = head
        while node:
            length += 1
            node = node.next
        if length == n:
            return head.next
        for _ in range(length-n-1):
            pointer = pointer.next
        if pointer.next:
            pointer.next = pointer.next.next
        return head
        