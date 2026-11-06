# Module 5 Laboratory Activity: Stacks and Queues

## Description
This Python program demonstrates stacks and queues using both arrays and linked lists. It also includes a balanced-parentheses checker and a print queue simulation.

## Files
- `array_stack.py` — fixed-size array stack with push, pop, peek, is_empty, and is_full.
- `linked_stack.py` — linked-list stack with push, pop, peek, and is_empty.
- `array_queue.py` — circular array queue with enqueue, dequeue, peek_front, is_empty, and is_full.
- `linked_queue.py` — linked-list queue with enqueue, dequeue, peek_front, and is_empty.
- `test_driver.py` — menu-driven program and application exercises.
- `analysis.md` — written answer to the analysis question.
- `sample_runs.md` — sample interactions and error-handling examples.

## Requirements
- Python 3
- No external packages are required.

## How to Run
1. Download all `.py` files into the same folder.
2. Open a terminal or command prompt in that folder.
3. Run:

   `python test_driver.py`

4. Follow the menu options.

## How to Test Error Handling
- For an array stack, choose a small capacity (such as 2), push two values, then try to push a third value to see stack overflow.
- Try to pop from an empty stack to see stack underflow.
- For an array queue, choose a small capacity (such as 2), enqueue two values, then try to enqueue a third value to see queue overflow.
- Try to dequeue from an empty queue to see queue underflow.

## Circular Queue Wrap-Around Test
For an array queue with capacity 3:
1. Enqueue A, B, and C.
2. Dequeue A and then B.
3. Enqueue D and E.
4. The logical queue should now be C, D, E. The rear index wraps around to the beginning of the array.

## Notes
The menu displays the current contents of the data structure after each successful operation and after handled underflow or overflow errors. The linked-list implementations do not have a fixed capacity; they are limited by available memory.
