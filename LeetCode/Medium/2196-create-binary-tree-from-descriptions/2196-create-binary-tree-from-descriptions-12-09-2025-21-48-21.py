# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        childs=set()
        nodes={}
        for parent, child, isLeft in descriptions:
            if child not in nodes:
                nodes[child]=TreeNode(child)
            
            if parent not in nodes:
                nodes[parent]=TreeNode(parent)
            childs.add(child)

            if isLeft==1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        root=(nodes.keys()-childs).pop()
        return nodes[root]
        # now=0
        # root=TreeNode()
        # print(root)
        # parents=list()
        # def find(x):
        #     parent
        # for des in descriptions:
        #     tmp=TreeNode(des[0])
        #     if des[2]==0:
        #         tmp.right=des[1]
        #     if des[2]==1:
        #         tmp.left=des[1]