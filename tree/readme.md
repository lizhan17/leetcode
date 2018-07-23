# Basic information
Unlike linked lists, one-dimensional arrays and other linear data structures, which are canonically traversed in linear order, trees may be traversed in multiple ways. They may be traversed in depth-first or breadth-first order. There are three common ways to traverse them in depth-first order: in-order, pre-order and post-order.[1] Beyond these basic traversals, various more complex or hybrid schemes are possible, such as depth-limited searches like iterative deepening depth-first search.
(ref wiki)



# deep first order of inorder 
inorder tree traversal is a traversal of a tree where each node is visited once. preorder, postorder and level order are different methods.

you would normally build a tree based on requrements and the traverse the tree depending on the order you wanted to visit each node.

inorder can be used on binary trees built from mathematical expressions - the order of traversal will ensure the correct order of calculation of all components of an expression.



# 94. Binary Tree Inorder Traversal


recursive way
``` python
 def inorderTraversal(self, root):
        return self.inorderTraversal(root.left)+[root.val]+self.inorderTraversal(root.right) if root else []
```
