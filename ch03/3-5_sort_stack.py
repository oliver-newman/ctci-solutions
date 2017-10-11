"""
3.5: Write a program to sort a stack such that the smallest elements are on the
top. You can use an additional temporary stack, but you may not copy the
elements into any other data structure (such as an array).
"""
import random


def sort_stack(stack):
    # NOTE: even if len() isn't available as an operation to stack, we can
    # easily determine the length in O(n) time by popping all the elements of
    # the stack into temp_stack and back into stack, counting them as we go.

    temp_stack = []
    max_item = None

    for i in range(len(stack)):
        while len(stack) > i:
            curr_item = stack.pop()

            if (max_item is None) or (curr_item > max_item):
                if max_item is not None:
                    temp_stack.append(max_item)
                max_item = curr_item
            else:
                temp_stack.append(curr_item)

        stack.append(max_item)
        max_item = None

        while temp_stack:
            stack.append(temp_stack.pop())


def test_sort_stack():
    stack = [random.randrange(100) - 50 for i in range(100)]
    solution = sorted(stack, key=lambda x: -x)
    sort_stack(stack)
    assert stack == solution

