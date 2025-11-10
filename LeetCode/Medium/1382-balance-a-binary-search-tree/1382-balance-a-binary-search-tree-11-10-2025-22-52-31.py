# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        li=[]
        def balanceTree(tree):
            if tree==None:
                return
            balanceTree(tree.left)
            li.append(tree.val)
            balanceTree(tree.right)
        balanceTree(root)

        def buildbalancetree(values):
            if not values:
                return None
            
            mid_index=len(values)//2
            root_node= TreeNode(values[mid_index])

            root_node.left=buildbalancetree(values[:mid_index])

            root_node.right=buildbalancetree(values[mid_index+1:])
            return root_node

        return buildbalancetree(li)