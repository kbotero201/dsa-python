class Node: 
    def __init__(self, value=None):
        self.value = value
        self.next = None

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
        removedNode = self.head 
        if self.head == self.tail:
            self.head = None 
            self.tail = None 
        else: 
            self.head = self.head.next 
        return removedNode

    def peek(self):
        if self.head == None:
            return "This queue is empty"
        else: 
            return self.head




   
                
            