"""
Binary Search Tree
"""

class Solution:
    def searchBST(self, root: TreeNode, val:int) -> TreeNode:

        current_Node = root

        while current_Node:
            if current_Node == val:
                return current_Node
            elif val < current_Node:
                current_Node = current_Node.left
            else:
                current_Node = current_Node.right
        return None
