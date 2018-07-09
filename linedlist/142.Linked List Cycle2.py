
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
"""
my first sol is just make a diction(hash map)



"""
   

#  my  second solution is to check each node until we find
# core logic is that a head node is its descentant node
        cur = head
        
        while(cur):
            child = cur.next
            while(child):
                if child == cur:
                    return cur
                else: 
                    child =child.next
            #end while  go to next pointer
            cur = cur.next
        #end while we didn't find such a special node
        return None
      
      
      
