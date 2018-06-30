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
    
    
    
    
    
    # my wrong anser
    class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        ## sol thought
        
        ## we need to work on the linked list itself
        ## step through the node
        ## if we found the head.next val = head.val just go to another head
        ## else we found the unique node add to the output
        ## use prev and cur and 
        
        cur= root = ListNode(0)
        
        cur.next = head
        tmp = 0
        
        ## i d better change the linked list inline
        
        if (head.next is None):
            return root.next

        while(head and head.next):
            
            ## edge case head
            if(head.next is not None and head.val != head.next.val):
                cur.next = head
                head = head.next
                cur = cur.next
                
            elif head.next is None and head.val != cur.val:
                cur.next = head
                
                return root.next
                
            else: #(head.next is not None and head.val ==head.next.val): # head.val = head.next val
                tmp = head.val
                while (head and tmp == head.val):
                    head = head.next
                if (head.next is None and head.val != tmp):
                    cur.next = head
                    return root.next
                if (head is None):
                    return root.next
