from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_state(structure):
    """Print the current contents of a stack or queue."""
    print("Current state:", structure)


def stack_menu():
    print("\nChoose stack implementation:")
    print("1. Array Stack")
    print("2. Linked Stack")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        capacity = read_positive_integer("Enter stack capacity: ")
        stack = ArrayStack(capacity)
    elif choice == "2":
        stack = LinkedStack()
    else:
        print("Invalid implementation choice.")
        return

    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        if isinstance(stack, ArrayStack):
            print("5. Check if full")
            print("6. Return to main menu")
        else:
            print("5. Return to main menu")

        action = input("Choose an operation: ").strip()
        try:
            if action == "1":
                value = input("Enter value to push: ")
                stack.push(value)
                print(f"{value} was pushed onto the stack.")
                show_state(stack)
            elif action == "2":
                print("Removed:", stack.pop())
                show_state(stack)
            elif action == "3":
                print("Top element:", stack.peek())
                show_state(stack)
            elif action == "4":
                print("Is empty?", stack.is_empty())
                show_state(stack)
            elif action == "5" and isinstance(stack, ArrayStack):
                print("Is full?", stack.is_full())
                show_state(stack)
            elif (action == "6" and isinstance(stack, ArrayStack)) or (
                action == "5" and isinstance(stack, LinkedStack)
            ):
                break
            else:
                print("Invalid operation choice.")
        except (IndexError, OverflowError) as error:
            print("Error:", error)
            show_state(stack)


def queue_menu():
    print("\nChoose queue implementation:")
    print("1. Circular Array Queue")
    print("2. Linked Queue")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        capacity = read_positive_integer("Enter queue capacity: ")
        queue = ArrayQueue(capacity)
    elif choice == "2":
        queue = LinkedQueue()
    else:
        print("Invalid implementation choice.")
        return

    while True:
        print("\n--- QUEUE MENU ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek front")
        print("4. Check if empty")
        if isinstance(queue, ArrayQueue):
            print("5. Check if full")
            print("6. Return to main menu")
        else:
            print("5. Return to main menu")

        action = input("Choose an operation: ").strip()
        try:
            if action == "1":
                value = input("Enter value to enqueue: ")
                queue.enqueue(value)
                print(f"{value} was added to the rear of the queue.")
                show_state(queue)
            elif action == "2":
                print("Removed:", queue.dequeue())
                show_state(queue)
            elif action == "3":
                print("Front element:", queue.peek_front())
                show_state(queue)
            elif action == "4":
                print("Is empty?", queue.is_empty())
                show_state(queue)
            elif action == "5" and isinstance(queue, ArrayQueue):
                print("Is full?", queue.is_full())
                show_state(queue)
            elif (action == "6" and isinstance(queue, ArrayQueue)) or (
                action == "5" and isinstance(queue, LinkedQueue)
            ):
                break
            else:
                print("Invalid operation choice.")
        except (IndexError, OverflowError) as error:
            print("Error:", error)
            show_state(queue)


def read_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")


def balanced_parentheses(expression):
    """Return True when (), [], and {} are correctly balanced."""
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}

    for character in expression:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack.pop() != matching[character]:
                return False

    return len(stack) == 0


def parentheses_exercise():
    expression = input("\nEnter an expression containing parentheses: ")
    if balanced_parentheses(expression):
        print("Result: The parentheses are balanced.")
    else:
        print("Result: The parentheses are NOT balanced.")


def print_queue_exercise():
    """Simulate print jobs being processed in FIFO order."""
    from collections import deque

    jobs = deque()
    print("\nEnter print jobs. Leave the Job ID blank to finish.")
    while True:
        job_id = input("Job ID: ").strip()
        if not job_id:
            break
        pages = read_positive_integer("Number of pages: ")
        jobs.append({"id": job_id, "pages": pages})
        print(f"Job {job_id} added to the print queue.")

    if not jobs:
        print("There are no print jobs.")
        return

    print("\nPrint order (first in, first out):")
    wait_order = 1
    while jobs:
        job = jobs.popleft()
        print(
            f"Wait order {wait_order}: Job {job['id']} "
            f"({job['pages']} page(s)) is now printing."
        )
        wait_order += 1
    print("All print jobs have been processed.")


def main():
    while True:
        print("\n====== STACKS AND QUEUES ACTIVITY ======")
        print("1. Use a Stack")
        print("2. Use a Queue")
        print("3. Balanced Parentheses Exercise")
        print("4. Print Queue Simulation")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            stack_menu()
        elif choice == "2":
            queue_menu()
        elif choice == "3":
            parentheses_exercise()
        elif choice == "4":
            print_queue_exercise()
        elif choice == "5":
            print("Program ended. Thank you!")
            break
        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()
