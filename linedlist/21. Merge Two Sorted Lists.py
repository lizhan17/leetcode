class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        
        p2 = l2
        
        root = q = ListNode(0)
        
        while(p1 or p2):
            if(p1.val>p2.val):
                q.next = ListNode(p2.val)   # add p2 to q and 
                p2 = p2.next   # p2 go to next node in l2
   .            q = q.next
            else:
                q.next = ListNode(p1.val) # add p1 to q
                p1 = p1.next
                q = q.next
        
        return root.next
