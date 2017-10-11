"""
3.5: Write a program to sort a stack such that the smallest elements are on the
top. You can use an additional temporary stack, but you may not copy the
elements into any other data structure (such as an array).
"""
import random


class Stack(list):
    def push(self, item):
        self.append(item)

    def peek(self):
        return self[-1]

    def is_empty(self):
        return len(self) == 0


def sort_stack(stack):
    # NOTE: even if len() isn't available as an operation to stack, we can
    # easily determine the length in O(n) time by popping all the elements of
    # the stack into temp_stack and back into stack, counting them as we go.

    temp_stack = Stack()

    while not stack.is_empty():
        curr_item = stack.pop()

        while not temp_stack.is_empty() and temp_stack.peek() > curr_item:
            stack.push(temp_stack.pop())

        temp_stack.push(curr_item)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


def test_sort_stack():
    stack = Stack(random.randrange(100) - 50 for i in range(1000))
    solution = sorted(stack, key=lambda x: -x)
    sort_stack(stack)
    assert stack == solution
