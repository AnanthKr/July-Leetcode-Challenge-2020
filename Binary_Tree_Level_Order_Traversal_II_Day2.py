Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

Python3 program:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        #breadthfirstsearch
        q = deque([(root,0)])
        output,temp,prev_level = [],[],0
        while q:
            node,level = q.popleft()
            if node:
                if level != prev_level:
                    output.append(temp)
                    temp = []
                    prev_level = level
                temp += [node.val]
                q.append((node.left,level+1))
                q.append((node.right,level+1))
        if temp: output.append(temp)
            
        return output[::-1]
