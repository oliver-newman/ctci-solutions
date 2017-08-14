from linked_list import LinkedList, LinkedListNode


def is_palindrome(ll):
    reversed_ll = reversed(ll)
    curr = ll.head
    rev_curr = reversed_ll.head
    while curr:
        if curr.val != rev_curr.val:
            return False
        curr = curr.next
        rev_curr = rev_curr.next
    return True


def reversed(ll):
    new_head = None
    curr = ll.head
    while curr:
        new_head = LinkedListNode(curr.val, new_head)
        curr = curr.next

    reversed_ll = LinkedList()
    reversed_ll.head = new_head
    return reversed_ll


def is_palindrome_stack(ll):
	slow = fast = ll.head
	stack = []
	while fast and fast.next:
		stack.append(slow.val)
		slow = slow.next
		fast = fast.next.next
	if fast:
		slow = slow.next
	while slow:
		if stack.pop() != slow.val:
			return False
		slow = slow.next
	return True


TEST_CASES = [
    (LinkedList([]), True),
    (LinkedList([1]), True),
    (LinkedList([1,1]), True),
    (LinkedList([1,2,1]), True),
    (LinkedList([10,5,5,10]), True),
    (LinkedList([4,3,10,3,4]), True),
    (LinkedList([1,2]), False),
    (LinkedList([1,2,3]), False),
    (LinkedList([1,2,3,1]), False),
]


def test_is_palindrome():
    for case in TEST_CASES:
        assert is_palindrome(case[0]) == case[1]


def test_is_palindrome_stack():
	for case in TEST_CASES:
		assert is_palindrome_stack(case[0]) == case[1]
