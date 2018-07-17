


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
    
        cur = head
       
        while cur and cur.next:
            if (cur.next.val >= cur.val):
                cur = cur.next
            else:
                if(head.val >= cur.next.val): # the todo element is smaller than the head of the ordered part
                    # we just set the cur.next to be the head,we don't need to change cur
                    tmp = cur.next
                    cur.next = cur.next.next
                    tmp.next = head
                    head = tmp
                    
                else: # the cur.next ele is bigger than the head and smalle than the tail of ordered part
                    
                    comparing_node = head
                    prev = None
                    while(comparing_node.val < cur.next.val):
                        prev = comparing_node
                        comparing_node = comparing_node.next
                    tmp2 = cur.next
                    
                    cur.next = cur.next.next
                    
                    prev.next = tmp2  # we use tmp2 to just insert one node is very important
                    tmp2.next = comparing_node
                    # we don't need to  change cur.next pointer
        
        return head
    
    
    
    ### ref leetcode
        def insertionSortList(self, head):
        cur = dummy = ListNode(0)
        while head:
            if cur and cur.val > head.val: 
                cur = dummy
            while cur.next and cur.next.val < head.val: 
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next
