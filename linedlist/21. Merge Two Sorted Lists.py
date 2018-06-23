class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        

        root = q = ListNode(0)
        
        while(l1 or l2):
            if(l1.val>l2.val):
                q.next = ListNode(l2.val)   # add p2 to q and 
                l2 = l2.next   # p2 go to next node in l2
                q = q.next
            else:
                q.next = ListNode(l1.val) # add p1 to q
                l1 = l1.next
                q = q.next
        
        return root.next
