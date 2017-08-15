"""
2.7: Given two singly linked lists, determine if the two lists intersect.
Return the intersecting node.
"""
from linked_list import LinkedList


def lists_intersect(ll1, ll2):
    len1, len2 = len(ll1), len(ll2)
    if len2 > len1:
        len1, len2 = len2, len1
        ll1, ll2 = ll2, ll1
    tail1, tail2 = get_tail(ll1), get_tail(ll2)
    
    if tail1 is tail2 is not None:
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
    

def get_tail(ll):
    curr = ll.head
    while curr and curr.next:
        curr = curr.next
    return curr
    

def test_lists_intersect():
    assert False
