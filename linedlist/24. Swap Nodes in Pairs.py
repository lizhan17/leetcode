"""

important!

for safety 
the end of a node should be None

like 

cur.next = None

because it may be a link like 


pre.next = cur
cur.next = next
next

"""



class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        root = prev = ListNode(0)
        cur = head
        
        prev.next = cur
        
        if(head is None):
            return head
        next = cur.next # ! next maybe none: 0->1->none
        
        ## special case
        ## if 0->1 ok
        ## if 0->1->2 
    
        while next and next.next :
            prev.next = next
            next2 = next.next
            next.next = cur  # 0 2 1 
            cur.next = next2    # we justchange the next not the node 0 2 1 3 4
            
            prev = cur # pre is 1 
            cur = next2 # cur is 3
            next = cur.next # ! next may be none in while loop  # next is 4
            
        
        
        # edge condition
        if(next is None):
            return root.next # unchanged
        else: # next.next is none
            prev.next = next
            next.next = cur
            cur.next = None
            return root.next
        
