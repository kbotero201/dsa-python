
class BSTNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 



# Iterative Solution (JS)
# O(log n) time complexity & O(log n) space complexity 
def insert(rootNode, value):
    newNode = BSTNode(value)
    if rootNode == None: 
        rootNode = newNode
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
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(value)
            else:
                insertNode(rootNode.leftChild, value)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(value)
            else:
                insertNode(rootNode.rightChild, value)
        return "The node has been successfully inserted"


