# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ## sol thought
        ## step through the node
        ## if we found the head.next val = head.val just find another head
        ## else we found the unique node add to the output
