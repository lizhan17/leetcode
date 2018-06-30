
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # go through the linked list
        # we compare the curr value with x 
        # if value smaller than x
        # we add it to the linked list
        # else we add it to anothe linked list
        
        # finnaly we just combine the two linked list and return    dummy1.last.next = dummy2.next
        
        prev1 = dummy1 = ListNode(0)
        prev2 = dummy2 = ListNode(0)
        
        
        curr = head    
         
        
        while(curr):
            if curr.val < x:
           
             prev1.next = curr    # we add curr to prev1(result linked list)
                curr = curr.next     # we go on next curr
                prev1 = prev1.next   # we update the prev1 
            else: 
                prev2.next = curr
                curr = curr.next
                prev2 = prev2.next
        
        prev1.next = dummy2.next
        prev2.next = None     # prev2 is related to curr may exsitng dead link
        return dummy1.next
