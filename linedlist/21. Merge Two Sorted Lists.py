"""
to add the end of list to 
        if(l1):
            q.next = l1
        if(l2):
            q.next = l2
           
     
-- python 
if a is None:
 use is to judge



"""





## my solution 1
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        

        root = q = ListNode(0)
        while(l1 and l2):
            if(l1.val > l2.val):
                q.next = ListNode(l2.val)   # add p2 to q and 
                l2 = l2.next   # p2 go to next node in l2
                q = q.next
            else:
                q.next = ListNode(l1.val) # add p1 to q
                l1 = l1.next
                q = q.next
        if(l1):
            q.next = l1
        if(l2):
            q.next = l2
            
            
        return root.next
    
    
    
    ### solution 2 recursive from leetcode
###     https://leetcode.com/problems/merge-two-sorted-lists/solution/
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
