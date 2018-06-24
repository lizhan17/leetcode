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
look out the order of these ponter


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
