"""
2.7: Given two singly linked lists, determine if the two lists intersect.
Return the intersecting node.
"""
from linked_list import LinkedList


def lists_intersect(ll1, ll2):
    """
    Time: O(m + n)
    Space: O(1)
    """
    len1, len2 = len(ll1), len(ll2)
    if len2 > len1:
        len1, len2 = len2, len1
        ll1, ll2 = ll2, ll1
    
    if ll1.get_tail() is ll2.get_tail() is not None:
        index1 = 0
        curr1, curr2 = ll1.head, ll2.head
        while len1 - index1 > len2:
            curr1 = curr1.next
            index1 += 1
        while curr1 is not curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1
    else:
        return None
    

def test_lists_intersect():
    test_cases = [
        (([], []), None),
        (([1], [2]), None),
        (([1], [1]), None),
        (([0, 1], [1]), None),
    ]
    for case, expected in test_cases:
        case = (LinkedList(lst) for lst in case)
        assert lists_intersect(*case) is expected

    # Couldn't think of a good easy way to construct many True test cases
    end = LinkedList(range(0, 10))
    ll1 = LinkedList(range(10, 20))
    ll1.get_tail().next = end.head
    assert lists_intersect(end, ll1) is end.head

    ll2 = LinkedList(range(20, 40))
    ll2.get_tail().next = end.head
    assert lists_intersect(ll1, ll2) is end.head
