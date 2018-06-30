"""
ref leetcode
https://leetcode.com/problems/remove-duplicates-from-sorted-list/discuss/123059/Python-O(n)-solution-with-explanation-52-ms




The solution is every intuitive. We traverse linked list. We keep track of value of the last unique node and two pointers: pointer to the previous node and pointer to the current node. We're gonna have 2 cases:

Value of current node == value of the last unique node. We change next pointer of unique node = next node after current. We don't change prev pointer, since it points to the last unique node and it didn't change in this step.
Value of current node != value of the last unique node. In this case, we set out unique value = value of current node. And we advance both pointers, previous and current, to the next node.




"""

## this is other's sol
class Solution:
    def deleteDuplicates(self, head):
        """ Removes duplicates from sorted linked list.
        Returns pointer to the head node.
        Time complexity: O(n). Space complexity: O(1),
        n is length of the linked list.
        """
        unique_val = None  # current unique node value
        prev = None
        curr = head
        while curr:
            if curr.val == unique_val:  # duplicate is found
                prev.next = curr.next
                curr = curr.next  # change only curr pointer
            else:  # new unique value
                unique_val = curr.val
                prev = curr
                curr = curr.next
        return head
