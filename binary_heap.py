# Array is the best way to implement

class Heap:
    def __init__(self, size):
        self.list = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
    
    def peekofHeap(rootNode):
        if not rootNode:
            return 
        else:
            return rootNode.list[1]
    
    def sizeofHeap(rootNode):
        if not rootNode:
            return 
        else:
            rootNode.heapSize
    
# Binary Heap Traversals ---------------
def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        for i in range(rootNode.heapSize):
            print(rootNode.list[i])

# Insert other traversals....


# Insert in Binary Heap ---------------



