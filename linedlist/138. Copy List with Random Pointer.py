# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


"""




"""

## https://www.youtube.com/watch?v=xF9goDxk5nM

## refer 

##
## additional  space complexity O(n)

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        dict = {}
        
        curr2 = curr = head
        while curr:
          dict[curr] = RandomListNode(curr.label)
          curr = curr.next 
        #endwhile
        
     
        while curr2:
          dict[curr2].next = dict[curr2.next] # step through to connect new nodes 
          dict[curr2].random = dict[curr2.random] # each random is connect to the same original node
          curr2 = curr2.next
        #endwhile
        return dict.get(head)
