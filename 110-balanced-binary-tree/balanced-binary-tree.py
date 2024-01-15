class Solution:
    def isBalanced(self, root):
        return self.dfs_height(root) != -1
    
    def dfs_height(self, root):
        if root is None:
            return 0
        
        left_height = self.dfs_height(root.left)
        if left_height == -1:
            return -1
        
        right_height = self.dfs_height(root.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
