from linked_list import LinkedList


def delete_middle_node(node):
    node.val = node.next.val
    node.next = node.next.next
    

def node_at_index(ll, index):
    curr = ll.head
    for i in range(index):
        curr = curr.next
    return curr


def test_delete_middle_node():
    test_cases = [
        (([0,1,2], 1), [0,2]),
        (([0,1,2,3], 1), [0,2,3]),
        (([0,1,2,3,4,5,6,7], 1), [0,2,3,4,5,6,7]),
        (([0,1,2,3,4,5,6,7], 3), [0,1,2,4,5,6,7]),
        (([0,1,2,3,4,5,6,7], 5), [0,1,2,3,4,6,7]),
    ]
    for case, expected in test_cases:
        ll = LinkedList(case[0])
        node = node_at_index(ll, case[1])
        delete_middle_node(node)
        assert ll == LinkedList(expected)
