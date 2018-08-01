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


# dfs vs bfs and stack and queue 


BFS explores/processes the closest vertices first and then moves outwards away from the source. Given this, you want to use a data structure that when queried gives you the oldest element, based on the order they were inserted. A queue is what you need in this case since it is first-in-first-out(FIFO). Whereas a DFS explores as far as possible along each branch first and then bracktracks. For this, a stack works better since it is LIFO(last-in-first-out)



https://stackoverflow.com/questions/3929079/how-can-i-remember-which-data-structures-are-used-by-dfs-and-bfs

https://medium.freecodecamp.org/all-you-need-to-know-about-tree-data-structures-bceacb85490c

# 七种树
https://www.cnblogs.com/shiguangrenran/p/8143694.html
