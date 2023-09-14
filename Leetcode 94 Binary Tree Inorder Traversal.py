#                                   LEETCODE 94. Binary Tree Inorder Traversal
#-----------------------------------------------------------------------------------------------------------------------------
#       Given the root of a binary tree, return the inorder traversal of its nodes' values.
#       Example 1:
#       Input: root = [1,null,2,3]
#       Output: [1,3,2]
#       Example 2:
#       Input: root = []
#       Output: []
#       Example 3:
#       Input: root = [1]
#       Output: [1]
#-----------------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        curr=root
        while(curr!=None or len(stack)>0):
            while(curr!=None):
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            res.append(curr.val)
            curr=curr.right
        return res
#-----------------------------------------------------------------------------------------------------------------------------
