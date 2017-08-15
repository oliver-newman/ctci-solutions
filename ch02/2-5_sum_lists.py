from linked_list import LinkedList, LinkedListNode


def sum_lists_forward(list1, list2):
    """
    Returns sum of list1 and list2 as if the ones digit were in the first node.
    [7, 1, 6] + [5, 9, 2] -> [2, 1, 9]
    """
    overflow = 0
    node1 = list1.head
    node2 = list2.head
    new_list = LinkedList()
    new_tail = None
    while node1 or node2 or overflow:
        node1_val = node1.val if node1 else 0
        node2_val = node2.val if node2 else 0
        overflow, digit_sum = divmod(node1_val + node2_val + overflow, 10)
        if new_list.head:
            new_tail.next = LinkedListNode(digit_sum)
            new_tail = new_tail.next
        else:
            new_list.head = LinkedListNode(digit_sum)
            new_tail = new_list.head
        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None
    return new_list


def sum_lists_backward(list1, list2):
    """
    Returns sum of list1 and list2 as if the ones digit were in the last node.
    [6, 1, 7] + [2, 9, 5] -> [9, 1, 2]
    """
    reverse(list1)
    reverse(list2)
    sum_list = sum_lists_forward(list1, list2)
    reverse(sum_list)
    return sum_list


def reverse(ll):
    new_head = None
    curr = ll.head
    while curr:
        next = curr.next
        curr.next = new_head
        new_head = curr
        curr = next
    ll.head = new_head


def test_sum_lists_forward():
    test_cases = [
        (([], []), []),
        (([0], []), [0]),
        (([], [1, 2]), [1, 2]),
        (([9], [1]), [0, 1]),
        (([7, 1, 6], [5, 9, 2]), [2, 1, 9]),
        (([7, 1, 6], [5, 9, 4]), [2, 1, 1, 1]),
        (([7, 1, 6], [5, 9, 2, 5]), [2, 1, 9, 5]),
    ]
    for case, expected in test_cases:
        args = (LinkedList(lst) for lst in case)
        assert sum_lists_forward(*args) == LinkedList(expected)


def test_sum_lists_backward():
    test_cases = [
        (([], []), []),
        (([0], []), [0]),
        (([], [2, 1]), [2, 1]),
        (([9], [1]), [1, 0]),
        (([6, 1, 7], [2, 9, 5]), [9, 1, 2]),
        (([6, 1, 7], [4, 9, 5]), [1, 1, 1, 2]),
        (([6, 1, 7], [5, 2, 9, 5]), [5, 9, 1, 2]),
    ]
    for case, expected in test_cases:
        args = (LinkedList(lst) for lst in case)
        assert sum_lists_backward(*args) == LinkedList(expected)
