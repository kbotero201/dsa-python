
class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
    
    #O(n) time complexity & O(1) space complexity 
    def traverse(self):
        if self.head == None:
            return None 
        else: 
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next 
    
    #O(n) time complexity & O(1) space complexity 
    def search(self, value):
        if self.head == None: 
            return None
        current = self.head
        while current is not None:
            if value == current.value:
                return current
            else: 
                current = current.next 
        return None

    #O(n) time complexity & O(1) space complexity 
    def getIndex(self, index):
        if self.head == None:
            return None
        current = self.head
        counter = 0
        while current is not None:
            if index == counter:
                return current
            else: 
                current = current.next 
                counter += 1
        return None

    #O(n) time complexity & O(1) space complexity 
    def set(self, index, value):
        if index < 0 or self.head == None:
            return None
        current = self.head
        counter = 0
        while current is not None:
            if index == counter:
                current.value = value
                return True
            else: 
                current = current.next 
                counter += 1
        return False 


    #O(n) time complexity & O(1) space complexity 
    #can insert in the front, end(-1), and at any index.
    def insert(self, index, value):
        newNode = Node(value)
        if self.head == None: 
            self.head = newNode
            self.tail = newNode
        else: 
            if index == 0:
                newNode.next = self.head
                self.head = newNode
            elif index == -1:
                self.tail.next = newNode
                self.tail = newNode
            else: 
                current = self.head
                nextNode = current.next
                counter = 0
                while current is not None:
                    if index == counter -1:
                        current.next = newNode 
                        newNode.next = nextNode
                        return "Inserted"
                    else: 
                        current = current.next 
                        counter += 1
                return "Index not found"


    #O(n) time complexity & O(1) space complexity 
    def deleteIndex(self, index):
        if self.head == None:
            return "List is empty"
        else: 
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: 
                    self.head = self.head.next 
            elif index == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: 
                    current = self.head 
                    while current is not None:
                        if current.next == self.tail:
                            break
                        current = current.next
                    current.next = None 
                    self.tail = current
            else: 
                current = self.head
                nextNode = current.next
                counter = 0
                while current is not None:
                    if index == counter -1:
                        current.next = nextNode.next
                        return "Deleted"
                    current = current.next
                    counter += 1
                return "Index not found"

                

# SLL Challenges -------------------------------
# Remove Duplicates (using set): 

#O(n) time complexity & o(n) space complexity 
    def removeDups(self):
        if self.head == None: 
            return "Empty"
        else: 
            current = self.head 
            visited = set([current.value])
            while current.next:
                if current.next.value in visited:
                    current.next = current.next.next
                else: 
                    visited.add(current.next.value)
                    current = current.next
            return self # or return whatever 



# Remove Duplicates (without temporay buffer):

# O(n2) time complexity & o(1) space complexity 
    def removeDups2(self):
        if self.head == None: 
            return "Empty"

        current = self.head 
        while current: 
            runner = current
            while runner.next:
                if runner.next.value == current.value:
                        runner.next = runner.next.next
                else: 
                    runner = runner.next 
            current = current.next 
        return self # or return whatever 


# Return Nth to last:

# O(n) time complexity & o(1) space complexity 
    def  nthToLast(self, n):
        pointer1 = self.head
        pointer2 = self.head 

        for i in range(n):
            if pointer2 is None: 
                return None
            pointer2 = pointer2.next

        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next 
        return pointer1
        








    