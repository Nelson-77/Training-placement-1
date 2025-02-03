# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root: return False
        def is_recurion(root, target, is_true):
            if not root and is_true:
                if target == 0:
                    return True
            if not root:
                return False


            left = is_recurion(root.left, target-root.val, not root.left and not root.right)
            if left:
                return True
            right = is_recurion(root.right, target-root.val, not root.left and not root.right)
            if right:
                return True

            return False

        return is_recurion(root, targetSum, True)
