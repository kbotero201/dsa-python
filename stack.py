
# LIFO Method
# O(1) time complexity & O(1) space complexity 


class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

class Stack:
    def __init__(self):
        self.head = None 
        self.tail = None

    def push(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else: 
            newNode.next = self.head 
            self.head = newNode

    def pop(self):
        if self.head == None:
            return None 
        remNode = self.head 
        if self.head == self.tail:
            self.head = None 
            self.tail = None 
        else: 
            self.head = self.head.next 
        return remNode 

    def peek(self):
        if self.head == None: 
            return None
        else: 
            return self.head

    def delete(self):
        self.head = None 