class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # analize: we don't know the length of the list
        # reverse from head?
        cnt = 0
        head2 = head
        root = p = ListNode(0)
        # go through the head node 
        while head:
            head = head.next
            cnt +=1 # print (cnt == 5)
        # head point to the last node 
        # it is a singly node we can't step back all we can is just go throught it
        
        
        ## now head point to None
        ## now we add head2 nodes to the root,p node
        p=p.next
        
        while cnt-n > 0:
            p.val = head2.val
            head2 = head2.next
            p = p.next
            cnt -=1
       
        # test1     it stops after 3 times and cnt = 5-3=2 and cnt-n =0  # now we already have what in the head2 p node 
        # p.val =4 and p.next is none 
        
        head2 = head2.next
        p.val = head2.val
        
        while head2:
            p.val = head2.val # it seems same
            head2 = head2.next
            p = p.next
        
            
        # lets return the next code 
        return root.next
