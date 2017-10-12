"""
4.2: Given a sorted (increasing order) array with unique integer
elements, write an algorithm to create a binary search tree with minimal
height.
"""
import math

from binary_tree import TreeNode


def minimal_tree(array):
    """
    0 1 2 3 4
    len = 5
    len / 2 = 2
    median = 2 good

    0 1 2 3
    len = 4
    len / 2 - 2
    median = 2 BAD
    """
    if len(array) == 0:
        return None
    elif len(array) == 1:
        return TreeNode(array[0])
    else:
        mid_index = (len(array) - 1) // 2
        root = TreeNode(array[mid_index])

        root.left = minimal_tree(array[:mid_index])
        root.right = minimal_tree(array[(mid_index + 1):])

        return root


def test_minimal_tree():
    assert minimal_tree([]) == None

    for i in range(1, 500):
        assert minimal_tree(range(i)).height() == min_possible_height(i)


def min_possible_height(num_nodes):
    height = -1
    total = 0
    while num_nodes > total:
        height += 1
        total += 2**height
    return height
