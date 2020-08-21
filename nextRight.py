class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def mark(root):
    if(root != None):
        mark(root.right)
        mark(root.left)
        print(root.val)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right= Node(3)
    root.left.right = Node(5)
    root.left.left = Node(4)
    root.right.right= Node(7)

    mark(root)