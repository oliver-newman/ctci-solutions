"""
4.3: Given a binary tree, design an algorithm which creates a linked list of
all the nodes at each depth.
"""
from binary_tree import TreeNode


def list_of_depths(tree):
    levels = []

    next_level = [] if tree is None else [tree]

    while len(next_level) > 0:
        levels.append(next_level)

        current_level = next_level
        next_level = []

        for node in current_level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

    return levels


def test_list_of_depths():
    tree = TreeNode(0)
    next_level = [tree]

    for i in range(1, 6):
        current_level = next_level
        next_level = []

        for node in current_level:
            node.left = TreeNode(i)
            next_level.append(node.left)
            node.right = TreeNode(i)
            next_level.append(node.right)
    
    depth_list = list_of_depths(tree)
    for i in range(6):
        for node in depth_list[i]:
            print(node.val)
            assert node.val == i
        print("")


if __name__ == '__main__':
    test_list_of_depths()
