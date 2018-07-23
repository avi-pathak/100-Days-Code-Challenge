'''idea is enqueu the right child of every node bnode at the same time procees the node fron the front of the queue'''
def levelOrder(self,root):
            queue = [root] if root else []
            while queue:
                node = queue.pop()
                print(node.data, end=" ")
                if node.left: queue.insert(0,node.left)
                if node.right: queue.insert(0,node.right)
