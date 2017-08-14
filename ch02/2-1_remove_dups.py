from linked_list import LinkedList


def remove_dups(ll):
    """
    Remove duplicates from an unsorted linked list.
    """
    seen = set()
    curr = ll.head
    prev = None
    while curr:
        if curr.val in seen: # only possible if prev is not none
            prev.next = curr.next
        else:
            seen.add(curr.val)
            prev = curr
        curr = curr.next


def remove_dups_without_hash(ll):
    """
    Remove duplicates from an unsorted linked list without using a hash buffer.
    """
    curr = ll.head
    while curr:
        runner = curr.next
        runner_prev = curr
        while runner:
            if runner.val == curr.val:
                runner_prev.next = runner.next
            else:
                runner_prev = runner
            runner = runner.next
        curr = curr.next
                


TEST_CASES = [
        ([], []),
        ([1], [1]),
        ([1,2], [1,2]),
        ([1,2,3], [1,2,3]),
        ([1,1], [1]),
        ([1,1,1], [1]),
        ([2,1,1], [2,1]),
        ([1,2,3,4,5,3], [1,2,3,4,5]),
        ([3,4,5,3], [3,4,5]),
        ([3,3,4,4,5,5,1,1], [3,4,5,1]),
        ([3,3,4,4,5,5,1,4,1], [3,4,5,1])
]


def test_remove_dups():
    for case in TEST_CASES:
        ll = LinkedList(case[0])
        remove_dups(ll)
        assert ll == LinkedList(case[1])


def test_remove_dups_without_hash():
    for case in TEST_CASES:
        ll = LinkedList(case[0])
        remove_dups_without_hash(ll)
        assert ll == LinkedList(case[1])
