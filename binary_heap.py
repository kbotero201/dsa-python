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
# O(log n) time complexity & O(log n) space complexity 
def heapifyTreeInsert(rootNode, index, heapType): #heapType: Min or Max 
    parentIndex = int(index/2)
    if index <= 1:
        return 
    if heapType == "Min":
        if rootNode.list[index] < rootNode.index[parentIndex]:
            temp = rootNode.list[index]
            rootNode.list[index] = rootNode.index[parentIndex]
            rootNode.index[parentIndex] = temp 
            heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.list[index] > rootNode.list[parentIndex]:
            temp = rootNode.list[index]
            rootNode.list[index] = rootNode.index[parentIndex]
            rootNode.index[parentIndex] = temp 
            heapifyTreeInsert(rootNode, parentIndex, heapType)

