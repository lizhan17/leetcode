# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        
        # we break the linked list , so just remember many nodes 
        
        def findNode(head,m): # is ok for all m from [1,length of list]
            curr = head
            while curr and m>1:
                curr= curr.next
                m = m-1
            return curr
        
    ### the tail must be none
        def getLastNode(head):  
            curr = head
            while curr.next :
                curr = curr.next
            return curr
    
    ## we must guarantee the tail is None 
        def reverse(head):
            prev = None  # prev is none 
            current = head # cur is the head 
            while(current is not None):
                next = current.next  # we got the next pointer first
                current.next = prev # we change the curent to prev pointer
                prev = current  # we change the prev to curent
                current = next # we change the current to next
            head = prev
            return head       
        
        
        dummy = ListNode(0)
        dummy.next = head # just add the list to dummy
   
        nthNode = findNode(head,n)
        
        mthNode = findNode(head,m) # return head
    
        
        if m== 1:
            mthPrevNode = dummy
        else: 
            mthPrevNode = findNode(head,m-1)  #
        #mthPrevNode.next = None #break mthPrevNode

        
        nPlus1thNode = nthNode.next 
        # n+1 maybe None
       
        
        nthNode.next = None # break the nthNode
        
        newMthNode = reverse(mthNode)
        
        mthPrevNode.next = newMthNode  # connect the reversed head to the front part of list
        
        newNthNode = mthNode  # we get the nth node
        
        newNthNode.next =  nPlus1thNode # connect the nthnode to the back part of list
        
        return dummy.next
