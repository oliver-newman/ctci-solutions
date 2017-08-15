def lists_intersect(ll1, ll2):
	len1 = 0
	curr1 = ll1.head
	while curr1 and curr1.next:
		len1 += 1
		curr1 = curr1.next

	len2 = 0
	curr2 = ll2.head
	while curr2 and curr2.next:
		len2 += 1
		curr2 = curr2.next
	
	if curr1 is None or curr2 is None:
		return False
	

def test_lists_intersect():
	assert False
