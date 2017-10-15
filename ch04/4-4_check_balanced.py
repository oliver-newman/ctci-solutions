"""
4.4: Implement a function to check if a binary tree is balanced (the heights of
the two subtrees of any node never differ by more than one).
"""
from binary_tree import TreeNode


def is_balanced(tree):
    balanced, _ = check_subtree_heights(tree)
    return balanced


def check_subtree_heights(tree):
    if tree is None:
        balanced = True
        height = -1
    else:
        left_balanced, left_height = check_subtree_heights(tree.left)
        right_balanced, right_height = check_subtree_heights(tree.right)

        balanced = (left_balanced and right_balanced and
                    abs(left_height - right_height) <= 1)
        height = max(left_height, right_height) + 1

    return balanced, height


def test_is_balanced():
    tree1 = TreeNode.from_list([
        [0],
        [1, None],
        [2, None, None, None]])

    assert not is_balanced(tree1)

    tree2 = TreeNode.from_list([
        [0],
        [1, 1],
        [2, None, None, None]])

    assert is_balanced(tree2)

    tree3 = TreeNode.from_list([
        [0],
        [1, 1],
        [2, None, None, None],
        [3, None, None, None, None, None, None, None]])

    assert not is_balanced(tree3)

    tree4 = TreeNode.from_list([
        [0],
        [1, 1],
        [2, 2, 2, None],
        [3, None, None, None, None, None, None, None]])

    assert is_balanced(tree4)
