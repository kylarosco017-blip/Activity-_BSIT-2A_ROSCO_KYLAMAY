# Sample Runs

These are example interactions. Your exact prompts may appear on separate lines depending on the terminal.

## 1. Array Stack: Push and Overflow

```text
Choose stack implementation:
1. Array Stack
2. Linked Stack
Enter choice: 1
Enter stack capacity: 2

Choose an operation: 1
Enter value to push: A
A was pushed onto the stack.
Current state: Stack (bottom -> top): ['A']

Choose an operation: 1
Enter value to push: B
B was pushed onto the stack.
Current state: Stack (bottom -> top): ['A', 'B']

Choose an operation: 1
Enter value to push: C
Error: Stack overflow: cannot push onto a full stack.
Current state: Stack (bottom -> top): ['A', 'B']
```

## 2. Stack Underflow

```text
Choose an operation: 2
Error: Stack underflow: cannot pop from an empty stack.
Current state: Stack (bottom -> top): []
```

## 3. Circular Array Queue Wrap-Around

```text
Capacity: 3
Enqueue A
Enqueue B
Enqueue C
Dequeue -> A
Dequeue -> B
Enqueue D
Enqueue E
Current logical queue: ['C', 'D', 'E']
```

## 4. Queue Overflow and Underflow

```text
Error: Queue overflow: cannot enqueue into a full queue.
Error: Queue underflow: cannot dequeue from an empty queue.
```

## 5. Balanced Parentheses

```text
Enter an expression containing parentheses: {[()]}
Result: The parentheses are balanced.
```

```text
Enter an expression containing parentheses: {[(])}
Result: The parentheses are NOT balanced.
```

## 6. Print Queue

```text
Job ID: P01
Number of pages: 3
Job P01 added to the print queue.
Job ID: P02
Number of pages: 5
Job P02 added to the print queue.
Job ID:
Print order (first in, first out):
Wait order 1: Job P01 (3 page(s)) is now printing.
Wait order 2: Job P02 (5 page(s)) is now printing.
All print jobs have been processed.
```
