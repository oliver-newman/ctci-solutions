"""
2.8: Given a circular linkedlist, implement an algorithm that returns the node
at the beginning of the loop.
"""
from linked_list import LinkedList


def find_loop_with_hash(ll):
	"""
	Time: O(n), where n is the length of the list before it loops back.
	Space: O(n)
	"""
	seen = set()
	curr = ll.head
	while curr:
		if curr in seen:
			break
		else:
			seen.add(curr)
		curr = curr.next
	return curr


def find_loop_without_hash(ll):
	pass


def test_find_loop_with_hash():
	assert False


def test_find_loop_without_hash():
	assert False
	