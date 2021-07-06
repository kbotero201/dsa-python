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
