# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1

        def dfs(node, curr):
            if not node:
                return 0

            curr += node.val
            count = prefix[curr - targetSum]

            prefix[curr] += 1
            count += dfs(node.left, curr)
            count += dfs(node.right, curr)
            prefix[curr] -= 1

            return count

        return dfs(root, 0)