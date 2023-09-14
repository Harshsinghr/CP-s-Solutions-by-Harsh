#                                   LEETCODE 94. Binary Tree Inorder Traversal
#-----------------------------------------------------------------------------------------------------------------------------
#       Given the root of a binary tree, return the preorder traversal of its nodes' values.
#       Example 1:
#       Input: root = [1,null,2,3]
#       Output: [1,2,3]
#       Example 2:
I#      nput: root = []
#       Output: []
#       Example 3:
#       Input: root = [1]
#      Output: [1]
#       Constraints:
#       The number of nodes in the tree is in the range [0, 100].
#       -100 <= Node.val <= 100
#-----------------------------------------------------------------------------------------------------------------------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #nlr
        res=[]
        stack=[]
        curr=root
        while(curr!=None or len(stack)>0):
            while(curr!=None):
                res.append(curr.val)
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            curr=curr.right
        return res
        
#-----------------------------------------------------------------------------------------------------------------------------
