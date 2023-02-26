# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ptr_map={}

        l = head

        while l:
            ptr_map[l] = True

            if l.next in ptr_map:
                return l.next
            
            l = l.next