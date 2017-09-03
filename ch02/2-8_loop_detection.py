"""
2.8: Given a circular linkedlist, implement an algorithm that returns the node
at the beginning of the loop.
Example:
                         5
0 -> 1 -> 2 -> 3 -> 4 -> 5
     ^                   |
     \___________________/

6                        
0 -> 1 -> 2 -> 3 -> 4 -> 5
^                        |
\________________________/

                    4                    
0 -> 1 -> 2 -> 3 -> 4 -> 5
          ^              |
          \______________/

                              6
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 0
                    ^         |
                    \_________/
"""
import pytest
from linked_list import LinkedList


def find_loop(ll):
    """
    Space: O(1)
    Time: O(n)
    """
    collision_node = find_collision_node(ll)

    if collision_node is None:
        return None

    start_node = ll.head
    loop_node = collision_node

    while start_node is not loop_node:
        start_node = start_node.next
        loop_node = loop_node.next

    return start_node

    
def find_collision_node(ll):
    slow = fast = ll.head
    index = 0
    while fast and fast.next:
        if index > 0 and slow is fast:
            return slow
        slow = slow.next
        fast = fast.next.next
        index += 1
    return None
    

@pytest.fixture
def test_cases():
    raw_cases = [
        ([], None),
        ([1,2,3,4,5], None),
        ([1], 0),
        ([1,2], 0),
        ([1,2,3], 1),
        ([1,1,1], 1),
        ([1,2,3], 2),
        (['a','b','c','d','e'], 2),
    ]
    constructed_cases = []
    for case, expected in raw_cases:
        ll = LinkedList(case)
        if expected is None:
            loop_node = None
        else:
            loop_node = ll.node_at(expected)
            ll.get_tail().next = loop_node
        constructed_cases.append((ll, loop_node))
    return constructed_cases


def test_find_loop(test_cases):
    for case, expected in test_cases:
        assert find_loop(case) is expected
