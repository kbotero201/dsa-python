class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# def insertNode(rootNode, nodeValue):
#     if nodeValue == rootNode.data:
#         return "This nodeValue already exists"
#     else: 
#         if rootNode.data == None:
#             rootNode.data = nodeValue
#         elif nodeValue < rootNode.data:
#             if rootNode.leftChild is None:
#                 rootNode.leftChild = BSTNode(nodeValue)
#             else:
#                 insertNode(rootNode.leftChild, nodeValue)
#         else:
#             if rootNode.rightChild is None:
#                 rootNode.rightChild = BSTNode(nodeValue)
#             else:
#                 insertNode(rootNode.rightChild, nodeValue)
#         return "The node has been successfully inserted"

def insertNode(rootNode, value):
    newNode = BSTNode(value)
    if rootNode.data == None: 
        rootNode.data = value
        return print("The node has been successfully inserted")
    current = rootNode
    while True:
        if value == current.data: 
            return print("Duplicate Value")
        if value < current.data:
            if current.leftChild == None:
                current.leftChild = newNode
                return print("The node has been successfully inserted")
            current = current.leftChild
        else:
            if current.rightChild == None:
                current.rightChild = newNode
                return print("The node has been successfully inserted")
            current = current.rightChild


# def searchNode(rootNode, nodeValue):
#     try:
#         if rootNode.data == nodeValue:
#             print("The value is found")
#         elif nodeValue < rootNode.data:
#             if rootNode.leftChild.data == nodeValue:
#                 print("The value is found")
#             else:
#                 searchNode(rootNode.leftChild, nodeValue)
#         else:
#             if rootNode.rightChild.data == nodeValue:
#                 print("The value is found")
#             else:
#                 searchNode(rootNode.rightChild, nodeValue)
#     except:
#         print("Not found")
#         pass



def searchNode(rootNode, value):
    if rootNode.data == None:
        return print("Error - Node without value")
    current = rootNode
    while current:
        if current.data == value:
            return print("Found")
        elif value < current.data:
            if current.leftChild.data == value:
                return print("Found")
            current = current.leftChild
        else:
            if current.rightChild.data == value:
                return print("Found")
            current = current.rightChild
        return print("Not found")


newBST = BSTNode(None)
searchNode(newBST, 70) 

insertNode(newBST, 70)
insertNode(newBST, 70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST, 30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)

searchNode(newBST, 70)

#print(deleteBST(newBST))
#levelOrderTraversal(newBST)


