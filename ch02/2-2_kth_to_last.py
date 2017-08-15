from linked_list import LinkedList


def kth_to_last(ll, k):
    """
    kth_to_last([1, 2, 3, 4, 5], 2) = LinkedListNode(4)
    """
    list_length = length(ll)
    if k <= 0 or k > list_length:
        return None
    index = list_length - k
    curr = ll.head
    for i in range(index):
        curr = curr.next
    return curr.val
        

def length(ll):
    curr = ll.head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    return count


def test_kth_to_last():
    test_cases = [
        (([0], 1), 0),
        (([0], 0), None),
        (([0], 2), None),
        (([0, 1], 1), 1),
        (([0, 1], 2), 0),
        (([0, 1, 2, 3, 4], 5), 0),
        (([0, 1, 2, 3, 4], 2), 3),
    ]
    for case, expected in test_cases:
        assert kth_to_last(LinkedList(case[0]), case[1]) == expected
