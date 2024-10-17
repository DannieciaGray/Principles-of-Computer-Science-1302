class TreeNode:
    def __init__(self,value,left = None, right = None): # None is a default val
        self.val = value    # value of current node
        self.left = left    # represents left subtree
        self. right = right # represents right subtree 

root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")

"""
DISCUSS IN NEXT CLASS
How can you extend the "TreeNode" class to represent a general tree
(>2 children/ up  to N children)
"""