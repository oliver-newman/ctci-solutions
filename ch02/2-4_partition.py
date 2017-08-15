from linked_list import LinkedList


def partition(ll, val):
    """
    [5,7,3,5,3,2,4], 4 -> [2,3,3,5,7,5,4]
        
    """
    prev = None
    curr = ll.head
    while curr:
        next_node = curr.next
        if prev and curr.val < val:
            prev.next = curr.next
            curr.next = ll.head
            ll.head = curr
        else:
            prev = curr
        curr = next_node
        


def test_partition():
    test_cases = [
        (([], 5), []),
        (([1], 5), [1]),
        (([1], 1), [1]),
        (([1,5], 4), [1,5]),
        (([5,1], 4), [1,5]),
        (([1,5], 5), [1,5]),
        (([5,1], 5), [1,5]),
        (([5,1,3], 5), [3,1,5]),
        (([5,7,3,5,3,2,4], 4), [2,3,3,5,7,5,4]),
    ]
    for case, expected in test_cases:
        lst, val = case
        ll = LinkedList(lst)
        partition(ll, val)
        assert ll == LinkedList(expected)
