
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
      
      
      
# mythird sol

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#  the  second solution is to check each node until we find
# core logic is that a head node is its descentant node
        cur = head
        while(cur):
            child = cur.next
            while(child):
                if(id(cur) == id(child)):
                    return cur
                else:
                    child = child.next
                    if child is not None:
                        print("cur:")
                        print(cur.val)
                        print(child.val)
                   
            #end while  go to next pointer
            cur = cur.next
        #end while we didn't find such a special node
        return None
 
## leetcode solution https://leetcode.com/problems/linked-list-cycle-ii/solution/
     class Solution(object):
    def getIntersect(self, head):
        tortoise = head
        hare = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1

      
