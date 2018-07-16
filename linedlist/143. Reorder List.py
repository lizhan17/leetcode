# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next and head.next.next:   #check if the list has two more nodes
            
            # partition the nodes into two parts
            pre, slow, fast = ListNode(None), head, head
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next
            pre.next = None
            
            # reverse the second half
            temp = None
            while slow:
                nxt = slow.next
                slow.next = temp
                temp = slow
                slow = nxt
                
            # reorder two parts
            dummy = head
            while dummy and temp:
                nxt= dummy.next
                dummy.next,dummy,temp = temp, temp, nxt143. Reorder List
