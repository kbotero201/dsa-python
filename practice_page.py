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
    



