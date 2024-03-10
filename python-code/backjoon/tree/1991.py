class TreeNode:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    def setLeftNode(self, left_node):
        self.left_node = left_node

    def setRightNode(self, right_node):
        self.right_node = right_node


def preorder(head):
    if head is None:
        return

    print(head.value, end="")
    preorder(head.left_node)
    preorder(head.right_node)


def inorder(head):
    if head is None:
        return

    inorder(head.left_node)
    print(head.value, end="")
    inorder(head.right_node)


def postorder(head):
    if head is None:
        return

    postorder(head.left_node)
    postorder(head.right_node)
    print(head.value, end="")


n = int(input())
cache = {}
head = None
for _ in range(n):
    root, left, right = map(str, input().split())

    root_node = None
    if root in cache:
        root_node = cache[root]
    else:
        root_node = TreeNode(root, None, None)
        head = root_node
        cache[root] = root_node

    if left == '.':
        left_node = None
    else:
        left_node = TreeNode(left, None, None)
    cache[left] = left_node

    if right == '.':
        right_node = None
    else:
        right_node = TreeNode(right, None, None)
    cache[right] = right_node

    root_node.setLeftNode(left_node)
    root_node.setRightNode(right_node)

preorder(head)
print()
inorder(head)
print()
postorder(head)
