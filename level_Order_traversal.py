
from collections import deque
def levelOrder(root):
    #Write your code here
    q = deque([root])
    
    while len(q):
        root = q.popleft()
        print(root, end = " ")
        
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
