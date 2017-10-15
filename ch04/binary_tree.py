class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return 'TreeNode(val={0}, left={1}, right={2})'.format(
                self.val, self.left, self.right)

    __repr__ = __str__

    @classmethod
    def from_list(cls, levels):
        if len(levels) == 0 or levels[0][0] is None:
            return None

        tree = TreeNode(levels[0][0])
        current_level_nodes = [tree]

        for i in range(1, len(levels)):
            assert len(levels[i]) == 2**i

            next_level_nodes = []

            for j in range(0, len(levels[i]), 2):
                left = None if levels[i][j] is None else TreeNode(levels[i][j])
                right = None if levels[i][j + 1] is None else TreeNode(levels[i][j + 1])

                if left:
                    current_level_nodes[j // 2].left = left
                if right:
                    current_level_nodes[j // 2].right = right

                next_level_nodes.append(left)
                next_level_nodes.append(right)

            current_level_nodes = next_level_nodes

        return tree


    # For testing purposes only
    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return 1 + self.right.height()
        elif self.right is None:
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())
