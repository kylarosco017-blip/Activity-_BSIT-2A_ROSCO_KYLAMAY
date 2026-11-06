# Analysis Question

**Why does the linked-list stack push at the head instead of the tail, and why must the array queue be circular?**

A linked-list stack pushes at the head because the head can be updated directly, so the push operation takes O(1) time. If we push at the tail of a singly linked list, we may need to travel through the list to find the last node, which takes O(n) time. The array queue must be circular so that empty spaces created at the front after dequeue operations can be reused. It allows the front and rear positions to wrap around to the beginning of the array using the modulo operator, avoiding wasted space and unnecessary shifting of elements.
