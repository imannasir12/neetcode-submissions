# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_search_arr = []
        q_search_arr = []

        # 2. BS for both nodes in the tree, track visited nodes for both in respective arrays
        x = root
        while x:
            p_search_arr.append(x)
            if x.val == p.val: break
            if p.val < x.val:
                x = x.left
            else:
                x = x.right
        y = root
        while y:
            q_search_arr.append(y)
            if y.val == q.val: break
            if q.val < y.val:
                y = y.left
            else:
                y = y.right
        # 3. Traverse arrays and look for the lowest common value
        curr_min = p_search_arr[0]
        for i in range(min(len(p_search_arr), len(q_search_arr))):
            next_val_p = p_search_arr[i]
            next_val_q = q_search_arr[i]

            if next_val_p == next_val_q:
                curr_min = next_val_p
            
        return curr_min
