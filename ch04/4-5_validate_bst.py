"""
4.5: Determine whether a binary tree is a binary search tree.
"""
from binary_tree import TreeNode


def is_bst(tree):
    return are_bst_nodes_in_range(tree, None, None)


def are_bst_nodes_in_range(tree, min_val, max_val):
    """
    Returns true if tree is a BST and all nodes have value greater than
    min_val and less than or equal to max_val.
    """
    if tree is None:
        return True

    if ((min_val is None or tree.val > min_val) and
        (max_val is None or tree.val <= max_val)):
        return (are_bst_nodes_in_range(tree.left, min_val, tree.val) and
                are_bst_nodes_in_range(tree.right, tree.val, max_val))
    else:
        return False


def test_is_bst():
    tree1 = TreeNode.from_list([])

    assert is_bst(tree1)

    tree2 = TreeNode.from_list([
        [1]
    ])

    assert is_bst(tree2)

    tree3 = TreeNode.from_list([
        [1],
        [0, 2]
    ])

    assert is_bst(tree3)

    tree4 = TreeNode.from_list([
        [1],
        [1, 2]
    ])

    assert is_bst(tree4)

    tree5 = TreeNode.from_list([
        [1],
        [2, 2]
    ])

    assert not is_bst(tree5)

    tree6 = TreeNode.from_list([
        [1],
        [None, 2],
        [None, None, None, 3]
    ])

    assert is_bst(tree6)
