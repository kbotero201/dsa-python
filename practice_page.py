# Stack 
class Node: 
    def __init__(self, val):
        self.val = val 
        self.next = None

class Stack: 
    def __init__(self):
        self.head == None 
        self.tail == None
    
    def push(self, val):
        newNode = Node(val)
        if self.head == None: 
            self.head = newNode
            self.tail = newNode
        else: 
            newNode.next = newNode
            self.head = newNode
        return 
      
    def pop(self):
        if self.head == None: 
            return "Empty"
        remNode = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return remNode
        
    def peek(self):
        if self.head == None:
            return "Empty"
        else:
            return self.head 

#Queue
class Queue:
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def enqueue(self, val):
        newNode = Node(val)
        if self.head == None: 
            self.head = newNode 
            self.tail = newNode
        else: 
            self.tail.next = newNode
            self.tail = newNode 
    
    def dequeue(self):
        if self.head == None:
            return "Empty"
        remNode = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
        return remNode
    
    def peek(self):
        if self.head == None: 
            return
        else: 
            return self.head

#SLL 
class SLL:
    def __init__(self):
        self.head = None 
        self.tail = None

    def traverse(self):
        if self.head == None:
            return 
        else:
            current = self.head 
            while current:
                print(current.val)
                current = current.next

    def search(self, val):
        if self.head == None: 
            return 
        current = self.head
        while current: 
            if current.val == val:
                return "Found"
            current = current.next
        return "Value not found"

    def set(self, index, val):
        if index < 0 or self.head == None:
            return 
        idx = 0
        current = self.head 
        while current:
            if index == idx:
                current.val = val
                return
            current = current.next 
            idx += 1
        return "Index not found"

    def insert(self, index, val):
        if index < 0 or self.head == None:
            return
        newNode = Node(val)
        counter = 0
        current = self.head 
        while current:
            if index -1 == counter:
                next = current.next
                current.next = newNode
                newNode.next = next 
                return 
            current = current.next
            counter += 1
        return "Index not found"


    def deleteIndex(self, index):
        if index < 0 or self.head == None:
            return
        counter = 0
        current = self.head
        while current:
            if counter == index -1:
                current.next = current.next.next
                return
            current = current.next
            counter += 1
        return "Index not found"
    

def removeNthFromEnd(self, rootNode, n):
    node1 = rootNode
    node2 = rootNode

    for i in range(n):
        node2 = rootNode.next
    
    if node2 == None:
        return rootNode.next

    while node2.next:
        node1 = node1.next
        node2 = node2.next
    
    node1.next = node1.next.next
    return rootNode

def partition(self, x):
    current = self.head 
    self.tail = self.head 

    while current:
        nextNode = current.next 
        current.next = None 
        if current.value < x:
            current.next = self.head 
            self.head = current
        else: 
            self.tail.next = current 
            self.tail = current
        current = nextNode 

    if self.tail.next is not None:
        self.tail.next = None  

def reverse(self):
    current = self.head 
    prev = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next 
    return prev 

def sumTwoLists(llA, llB):
    nodeA = llA.head
    nodeB = llB.head
    carry = 0
    ll = LinkedList()

    while nodeA and nodeB:
        result = 0
        if nodeA:
            result += nodeA.val
            nodeA = nodeA.next
        if nodeB:
            result += nodeB.val
            nodeB = nodeB.next
        ll.add(int(result) % 10)
        carry = result / 10 

    if carry >= 1:
        ll.add(int(carry) % 10)
    
    return ll 
        

#BST 
def addBSTNode(rootNode, val):
    if rootNode.val == None:
        rootNode.val = val 
    newNode = Node(val)
    current = rootNode
    while True:
        if current.val == val:
            return "Dup"
        if val < current.val:
            if current.left == None:
                current.left = newNode 
            current = current.left
        else: 
            if current.right == None:
                current.right = val
            current = current.right
        return "Node inserted" 

def searchBST(rootNode, val):
    if rootNode == None:
        return 
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
    return "Value not found"

#BST Breath First Search 
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

#Sorting 
def bubbleSort(list):
    for i in range(len(list) -1):
        for j in range(len(list) - i -1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)

def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    print(list)

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j + 1] = key 
    print(list)


def bucketSort(list):
    numOfBuckets = round(math.sqrt(len(list)))
    maxValue = max(list)
    arr = []

    for i in range(numOfBuckets):
        arr.append([])
    for j in list:
        index_b = math.ceil(j* numOfBuckets/maxValue)
        arr.[index_b -1].append(j)
    
    for i in range(numOfBuckets):
        arr[i] - insertionSort(arr[i])
    
    k = 0
    for i in range(numOfBuckets):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k += 1
    return list 

def mergeSort(array):
    if len(array) <= 1:
        return array 
    midpoint = int(len(array)/2)

    left, right = mergeSort(array[:midpoint]), mergeSort(array[midpoint:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result 


# Find distinct pairs 
def findPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]: # for distinct pairs 
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

myList = [1,2,3,2,3,4,5,6]

#Two Sum problem 
def twoSum2(self, nums, target):
        buffer = {}
        for i, num in enumerate(nums):
            m = target - num
            if m in buffer:
                return [buffer[m], i]
            else:
                buffer[num] = i

#Heap Traversals
def levelOrderTraversal(rootNode):
    if not rootNode:
        return 
    else:
        for i in range(rootNode.heapSize):
            print(rootNode.list[i])

def insertNode(rootNode, value, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.list[rootNode.heapSize + 1] = value
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "Value Inserted"


#Anagram 
def isAnagram2(s, t):
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        
        for val in dic.values():
            if val != 0:
                return False
        
        return True

#Reverse String 
def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# Node 
class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None
