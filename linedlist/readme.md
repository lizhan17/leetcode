linedlist
https://ocw.mit.edu/courses/civil-and-environmental-engineering/1-00-introduction-to-computers-and-engineering-problem-solving-spring-2012/recitations/MIT1_00S12_REC_12.pdf



What in practice:
- Database: use linked list to solve hashtable collision



BIG Pros:

- A Linked List can grow dynamically.
(To resize an array you have to create a new, larger array, and copy everything over)
- A linked list does NOT need contiguous memory.
(A Java 1-D array has to occupy contiguous memory. When storing large amounts of data,finding back-to-back-to-back… memory can be impossible)



some special tricks:
reverse a k linked list

we use prev and next to store the prev pointer and next pointer
so that we can break the list and maintain the original order


![Alt Text](https://www.geeksforgeeks.org/wp-content/uploads/RGIF2.gif)

```python
def reverse(self):
        prev = None  # prev is none 
        current = self.head # cur is the head 
        while(current is not None):
            next = current.next  # we got the next pointer first
            current.next = prev # we change the curent to prev pointer
            prev = current  # we change the prev to curent
            current = next # we change the current to next
        self.head = prev
```
another way is switch the head each time iteration
```python
reverse list inline(use swap )
swap(1,2)  2 1 3 4 5
swap(2,3)  3 2 1 4 5


https://blog.csdn.net/u012848330/article/details/51570232


```



```python
        dummy = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, dummy.next
        while curr :
```


有些指针 用法
root = ListNode(0)
root.next = prev = head

root 给prev 一个初始值
还可以固定这个linkedlist 最后得到整个list

而prev cur next的操作 要考虑到next cur 会不会是none 

这和base case有关 也和while 里用的传递方法有关
一般要有next.next 一定会出现next is none 的问题
所以用短路
while(next and next.next)

while(cur)

不像for loop 于list.
linkedlist不知道数量 所以 不能用for loop进行遍历


注意！指针之间修改顺序会导致 

 Because in Python, every value is a reference, you can say a pointer, to an object. Objects cannot be values. Assignment always copies the value; two such pointers point to the same object. Hope that helps.
 
 
 ```python
 curr = head
 
 return head
 
 ```


# 第83题 基础讲解 碰上 unique linked list

We traverse linked list. 
We keep track of value of the last unique node and two pointers: pointer to the previous node and pointer to the current node.

# prev pointer 操作
prev.next = curr.next
we didn't change the prev ,we acutually look at the next curr node. we ignore the curr node now, we need to keep a last_unique value


prev = curr

we accually add the curr node to the result linked list
# 92. Reverse Linked List II  连接 剪断 
0 剪短linked list 需要 set  node.next = None 防止出现死链
1 运用 reverse linked list
2 定义几个基础function
3 python function is firstclass function, we can define function inside a function
4 object function or member function must be passed by instance , which is a global variable , have side effets.
  a.foo() a.call()
5 注意特殊情况 input 3->5 1 2 output 5->3  这里我的 是 findNode(0)返回 prev node(dummynode)


## 142 linked list cirular
0
1
2
3

ref:https://www.geeksforgeeks.org/circular-linked-list/
** about special features of circular linked list
0
1
2
## 143 reorder list. split linked list
ref:
https://leetcode.com/problems/reorder-list/discuss/143710/My-python-solution-with-some-comments.-O(1)-space-(easy-to-understand)
我们用两个指针来分割list。一个步长是；另一个的两倍。
同时用一个prev来 分割这个linked list

prev.next = None
```python

if head and head.next and head.next.next:
    pre, slow , fast = ListNode(0), head , head
    while (fast and fast.next):
        pre ,slow, fast = slow, slow.next, fast.next.next
    pre.next = None

```
第二步 我们调转这个链表。
已经有了两个pointer 我们可以直接用iterative方法。
理解很好理解 直接捋一遍。从头到尾。要想实现 我们需要一个额外到next pointer 。这样可以追踪它。

```python
while slow:
    nxt = slow.next
    slow.next = temp
    temp = slow
    slow = nxt
```

```python

prev = None
while(cur):
    next = cur.next
    cur.next = prev
    prev = cur
    cur = next
    

```
