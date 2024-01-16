# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ptr = head
        arr = []
        while ptr:
            arr.append(ptr.val)
            ptr = ptr.next
        if len(arr) == 1:
            return True
        if len(arr) % 2 == 0:
            return arr[0: int(len(arr)/ 2)] == arr[int(len(arr)/ 2):][::-1]
        else:
            return arr[0: int(len(arr)/ 2)] == arr[int(len(arr)/ 2)+1:][::-1]