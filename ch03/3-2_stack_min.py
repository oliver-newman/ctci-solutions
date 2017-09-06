"""
3.2 Stack Min: How would you design a stack which, in addition to `push` and
`pop`, has a function `min` which returns the minimum element? `push`, `pop`,
and `min` should all operate in O(1) time.
"""
import pytest


class StackFullException(Exception):
    pass

class StackEmptyException(Exception):
    pass


class MinStack:
    """Pretends that Python lists act like arrays."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.values = [None] * capacity
        self.index_mins = [None] * capacity

    def push(self, value):
        if self.size >= self.capacity:
            raise StackFullException()

        if self.size > 0:
            self.index_mins[self.size] = min(value, self.min())
        else:
            self.index_mins[self.size] = value

        self.values[self.size] = value
        self.size += 1

    def pop(self):
        if self.size <= 0:
            raise StackEmptyException()
        self.size -= 1
        return self.values[self.size]

    def min(self):
        if self.size <= 0:
            raise StackEmptyException()
        return self.index_mins[self.size - 1]


def test_stack_min():
    stack = MinStack(3)
    with pytest.raises(StackEmptyException) as exc_info:
        stack.pop()
    with pytest.raises(StackEmptyException) as exc_info:
        _ = stack.min()

    stack.push(5)
    assert stack.min() == 5
    assert stack.pop() == 5

    for i in [4, 5, 2]:
        stack.push(i)

    assert stack.min() == 2
    stack.pop()
    assert stack.min() == 4

    stack.push(3)
    assert stack.min() == 3

    with pytest.raises(StackFullException) as exc_info:
        stack.push(1)
    assert stack.min() == 3
