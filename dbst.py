class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def height(node):

        # Base Case : Tree is empty
        if node is None:
            return 0

        return 1 + max(height(node.left), height(node.right))

    def diameter(root):

        # Base Case when tree is empty
        if root is None:
            return 0

        # Get the height of left and right sub-trees
        lheight = height(root.left)
        rheight = height(root.right)

        # Get the diameter of left and irgh sub-trees
        ldiameter = diameter(root.left)
        rdiameter = diameter(root.right)

        # Return max of the following tree:
        # 1) Diameter of left subtree
        # 2) Diameter of right subtree
        # 3) Height of left subtree + height of right subtree +1
        return max(lheight + rheight + 1, max(ldiameter, rdiameter))


N , root = map(int , input().split())
ll=node(root)
arr=[]
for _ in range(N-1):
    arr.append([input() , int(input())])
for n in arr:
    for k in n[0].strip():
        temp=ll
        if k=='L':
            temp=temp.left
        elif k=='R':
            temp=temp.right
    temp=node(n[1])
print(ll.diameter())
