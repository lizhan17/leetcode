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

 ## why I am wrong
## I use head as the cur 
## I should use c
"""
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, dummy.next
        while curr :

"""

        
 ## sol from others with my analyis
## ref  https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28398/clean-python-solution-involving-dummy-node
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, dummy.next
        
        while curr:
            ##
            if curr.next and curr.val == curr.next.val:
                val_to_rem = curr.val
                
                while curr and curr.val == val_to_rem:
                    curr = curr.next
                    
                prev.next = curr
                
            else:
                prev, curr = curr, curr.next
                
        return dummy.next
