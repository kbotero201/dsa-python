
class BSTNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 


# Insert Node Into Binary Search Tree -----------

# Iterative Solution (JS)
# O(log n) time complexity & O(log n) space complexity 
def insert(rootNode, value):
    newNode = BSTNode(value)
    if rootNode.value == None: 
        rootNode.value = value
        return 
    current = rootNode
    while True:
        if value == current.value: 
            return "Duplicate Value"
        if value < current.value:
            if current.left == None:
                current.left = newNode
                return
            current = current.left
        else:
            if current.right == None:
                current.right = newNode
                return
            current = current.right
         
# Recursive solution
# O(log n) time complexity & O(log n) space complexity 
def insertNode(rootNode, value):
    if value == rootNode.value:
        return "This value already exists"
    else: 
        if rootNode.value == None:
            rootNode.value = value
        elif value < rootNode.value:
            if rootNode.left is None:
                rootNode.left = BSTNode(value)
            else:
                insertNode(rootNode.left, value)
        else:
            if rootNode.right is None:
                rootNode.right = BSTNode(value)
            else:
                insertNode(rootNode.right, value)
        return "The node has been successfully inserted"



# Search In Binary Search Tree -----------

# Iterative Solution (JS)
# O(log n) time complexity & O(log n) space complexity 
def search(rootNode, value):
    if rootNode.data == None:
        return "Error = node without value"
    current = rootNode
    while current:
        if current.value == value:
            return "Found"
        if value < current.value:
            if current.left.value == value:
                return "Found"
            current = current.left
        else:
            if current.right.value == value:
                return "Found"
            current = current.right
    return "Value not found"

            
# Recursive solution
# O(log n) time complexity & O(log n) space complexity 
def search(rootNode, value):
    try:
        if rootNode.value == value:
            return "The value is found"
        elif value < rootNode.value:
            if rootNode.left.value == value:
                return "The value is found"
            else:
                search(rootNode.left, value)
        else:
            if rootNode.right.value == value:
                return "The value is found"
            else:
                search(rootNode.right, value)
    except:
        return "Not found"


# Delete Node In Binary Search Tree -----------

# Psuedo:
# Leaf node: set the parent's child (right/left) to NULL.
# Has one child: Just set the child of the node to be deleted to its parent's child.
# Has two children: Basically have to re-order the whole subtree here by pruning the subtree to by finding new children for the node to be deleted.

# Recursive Solution
# O(log n) time complexity & O(log n) space complexity 
def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data 
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


# Delete Entire Binary Search Tree -----------
def deleteBST(rootNode):
    rootNode.value = None
    rootNode.left = None
    rootNode.right = None
    return "The BST has been successfully deleted"


# Traverse Binary Search Tree (Depth First Search) -----------
# O(n) time complexity & O(n) space complexity 

# Root Node => Left Subtree => Right Subtree
def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.value)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

# Left Subtree => Root Node => Right Subtree
def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.left)
    print(rootNode.value)
    inOrderTraversal(rootNode.right)

# Left Subtree => Right Subtree => Root Node
def postOrderTraversal(rootNode):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.value)


# Traverse Binary Search Tree (Breadth First Search/ Level Order Traversal) (uses Queue) -----------
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



# Practice
def insert(rootNode, val):
    if rootNode.val == None:
        rootNode.val = val
    newNode = Node(val)
    current = rootNode
    while True:
        if current.val == val:
            return "Duplicate"
        if val < current.val:
            if current.left == None:
                current.left == newNode 
                return "Inserted"
            current = current.left 
        else:
            if current.right == None: 
                current.right = newNode 
                return "Inserted"
            current = current.right 

        
def searchBST(rootNode, val):
    try:
        if rootNode.val == val:
            return "Found"
        elif val < rootNode.left.val:
            if rootNode.left.val == val:
                return "Found"
            else: 
                searchBST(rootNode.left, val)
        else:
            if rootNode.right.val == val:
                return "Found"
            else:
                searchBST(rootNode.right, val)
    except:
        return "Val not found"



# Iterative 
def insert(rootNode, val):
    if rootNode.val == None:
        rootNode.val == val 
        return
    newNode = BSTNode(val)
    current = rootNode
    while True: 
        if current.val == val:
            return "Duplicate"
        if val < current.val:
            if current.left == None:
                current.left == newNode
                return "Inserted"
            current = current.left
        else: 
            if current.right == None: 
                current.right = newNode
                return "Inserted"
            current = current.right  

# Recursive
def InsertR(rootNode, val):
    if rootNode.val == val:
        return "Duplicate"
    else: 
        if rootNode.val == None: 
            rootNode.val == val
        elif val < rootNode.val: 
            if rootNode.left == None: 
                rootNode.left = BSTNode(val)
            else: 
                InsertR(rootNode.left, val)
        else: 
            if rootNode.right == None:
                rootNode.right = BSTNode(val)
            else:
                InsertR(rootNode.right, val)
        return "Inserted"



def search(rootNode, val):
        if rootNode.val == val:
            return "Found"
        current = rootNode
        while current: 
            if current.val == val:
                return "Found"
            if val < current.val:
                if current.left.val == val:
                    return "Found"
                current = current.left
            else: 
                if current.right.val == val:
                    return "Found"
                current = current.right
        return "Not Found"

    
