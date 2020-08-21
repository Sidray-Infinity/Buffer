class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if (self != None):
            self.left.__str__()
            print(self.val)
            self.right.__str__()
        return ""

        
if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)

    print(root1)