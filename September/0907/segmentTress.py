class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None
        self.mark = False


class Tree:
    def __init__(self, maxCord):
        self.root = Tree.build([1]*(maxCord+1), 0, maxCord)

    @staticmethod
    def build(nums, start, end):
        if start > end:
            return None

        root = Node(start, end)

        if start == end:
            root.sum = nums[start]
            return root

        mid = (start+end)//2
        root.left = Tree.build(nums, start, mid)
        root.right = Tree.build(nums, mid+1, end)
        root.sum = root.left.sum+root.right.sum

        return root

    @staticmethod
    def update(root, start, end):
        if start > root.end or end < root.start:
            return
        if root.start >= start and end >= root.end:
            root.mark = True
            root.sum = 0
            return

        root.left.mark |= root.mark
        root.right.mark |= root.mark
        if root.left.mark:
            root.left.sum = 0
        if root.right.mark:
            root.right.sum = 0
        Tree.update(root.left, start, end)
        Tree.update(root.right, start, end)
        root.sum = root.left.sum+root.right.sum

    @staticmethod
    def query(root, start, end):
        if start > root.end or end < root.start:
            return 0
        if root.start >= start and end >= root.end:
            return root.sum

        root.left.mark |= root.mark
        root.right.mark |= root.mark
        if root.left.mark:
            root.left.sum = 0
        if root.right.mark:
            root.right.sum = 0

        return Tree.query(root.left, start, end)+Tree.query(root.right, start, end)


l, m = map(int, input().split())
tr = Tree(l)
for _ in range(m):
    u, v = map(int, input().split())
    Tree.update(tr.root, u, v)

print(Tree.query(tr.root, 0, l))
