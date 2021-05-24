
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current = self.head 
        while current: 
            yield current 
            current = current.next 
    
    def __str__(self):
        values = [str(x.value) for x in self]
        return "->".join(values)
    
    def add(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode 
        else:
            self.tail.next = newNode 
            self.tail = newNode


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    
    if carry > 1:
        ll.add(int(carry) % 10)
    
    return ll

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(7)


llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(9)
print(llA)
print(llB)
print(sumList(llA, llB))
