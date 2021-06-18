
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

# DFS (Depth First Search) -----------
# O(n) time complexity & O(n) space complexity 

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.value)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.left)
    print(rootNode.value)
    inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.value)

# BFS (Breadth First Search/ Level Order Traversal) -----------
class QueueNode:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def isEmpty(self):
        if self.head == None: 
            return True 
        else:
            return False
    
    def enqueue(self, value):
        newNode = QueueNode(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode 
        else:
            self.tail.next = newNode 
            self.tail = newNode
    
    def dequeue(self):
        if self.head == None:
            return 
        remNode = self.head
        if self.head == self.tail:
            self.head = None 
            self.tail = None 
        else: 
            self.head = self.head.next
        return remNode

# O(n) time complexity & O(n) space complexity 
def BFS(rootNode):
    if not rootNode:
        return 
    else: 
        queue = Queue()
        queue.enqueue(rootNode)
        while not (queue.isEmpty()):
            root = queue.dequeue()
            print(root.data.value)
            if root.data.left is not None:
                queue.enqueue(root.data.left)
            if root.data.right is not None:
                queue.enqueue(root.data.right)




# Searching for a node in Binary Tree -----------
# We will use level order traversal for better performance:
# Note: Queue always perfroms better than stacks/recursion  

# O(n) time complexity & O(n) space complexity 
def searchBT(rootNode, value):
    if not rootNode:
        return 
    else: 
        queue = Queue()
        queue.enqueue(rootNode)
        while not (queue.isEmpty()):
            root = queue.dequeue()
            if root.data.value == value:
                return "Sucess"
            if root.data.left is not None:
                queue.enqueue(root.data.left)
            if root.data.right is not None:
                queue.enqueue(root.data.right)
        return "Value Not Found"


# Inserting node in Binary Tree -----------
# O(n) time complexity & O(n) space complexity 
def insert(rootNode, newNode):
    if not rootNode: 
        rootNode = newNode 
    else:
        queue = Queue()
        queue.enqueue(rootNode)
        while not (queue.isEmpty()):
            root = queue.dequeue()
            if root.data.left is not None:
                queue.enqueue(root.data.left)
            else: 
                root.data.left = newNode
                return "Inserted"
            if root.data.right is not None:
                queue.enqueue(root.data.right)
            else:
                root.data.right = newNode
                return "Inserted"


# Deleting a node in Binary Tree -----------




# Deleting Entire Binary Tree -----------
# O(1) time complexity & O(1) space complexity 
def deleteBT(rootNode):
    rootNode.value = None 
    rootNode.left = None
    rootNode.right = None
    return "The Binary Tree Has Been Deleted"



