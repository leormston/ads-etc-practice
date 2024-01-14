# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        ptr = head
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        arr = arr[::-1]
        head = ListNode(arr[0])
        ptr = head
        for val in arr[1:]:
            ptr.next = ListNode(val)
            ptr = ptr.next
        return head