# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    
        node_tolist = []
        ## get the python list of a listnode
        for a in lists:
            while a:
                node_tolist.append(a.val)
                a = a.next
        node_tolist.sort()
        root = list_tonode = ListNode(0)
        ## each ele in list is a node in return data
        for ele in node_tolist:
            list_tonode.next = ListNode(ele)
            list_tonode = list_tonode.next
        
        return root.next
