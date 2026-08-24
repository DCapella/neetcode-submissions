# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        values.sort()

        res = node = ListNode(0)
        for val in values:
            cur = ListNode(val)
            node.next = cur
            node = node.next
        return res.next

        