
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
                counter = 0
                while current is not None:
                    if counter == index -1: 
                        nextNode = current.next
                        current.next = newNode 
                        newNode.next = nextNode
                        return 
                    else: 
                        current = current.next 
                        counter += 1
                return print("Index not found")


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
                counter = 0
                while current is not None:
                    if counter == index -1:
                        nextNode = current.next
                        current.next = nextNode.next
                        return 
                    current = current.next
                    counter += 1
                return print("Index not found")
                

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
    def nthToLast(self, n):
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
        

# Remove Nth to last & return its head
def removeNthFromEnd(self, head: Node, n: int) -> Node:
        pointer1 = head
        pointer2 = head
        
        for i in range(n):
            pointer2 = pointer2.next
        
        if pointer2 == None:
            return head.next
            
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        pointer1.next = pointer1.next.next
        return head
    

# Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than x. 

# O(n) time complexity & o(1) space complexity 
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


# You have two numbers represented by a linked list, where each node contains a single digit. 
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list. 

# O(n) time complexity & o(1) space complexity 

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

# start solution: (CLASS NEEDS AN "ADD" FUNCTION FOR THIS TO WORK)
                
        def sumLists(llA, llB):
            nodeA = llA.head
            nodeB = llB.head 
            carry = 0 
            ll = SLinkedList()

            while nodeA or nodeB:
                result = carry
                if nodeA:
                    result += nodeA.value
                    nodeA = nodeA.next 
                if nodeB:
                    result += nodeB.value 
                    nodeB = nodeB.next 
                ll.add(int(result) % 10)
                carry = result / 10
            
            if carry > 1:
                ll.add(int(carry) % 10)

            return ll 


# Reverse Linked List Iteratively

# O(n) time complexity & o(1) space complexity 
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev # return the new head reference 


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur = head
        prev = None
        while m > 1:
            prev = cur
            cur = cur.next
            m = m - 1
            n = n - 1

        # The two pointers that will fix the final connections.
        tail = cur
        con = prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head



# Practice 
def addTwoLists(llA, llB):
    nodeA = llA.head
    nodeB = llB.head
    carry = 0
    ll = LinkedList()

    while nodeA or nodeB:
        result = carry 
        if nodeA:
            result += nodeA.val
            nodeA = nodeA.next
        if nodeB:
            result += nodeB.val
            nodeB = nodeB.next
        ll.add(int(result) %10)
        carry = result / 10 
    
    if carry >= 1:
        ll.add(int(carry) % 10)
    
    return ll

def reverse(self):
    current = self.head
    prev = None 

    while current:
        next = current.next 
        current.next = prev
        prev = current
        current = next 
    
    return prev

def sumTwoLists(lla, llB):
    nodeA = llA.head
    nodeB = llB.head
    carry = 0
    ll = LinkedList()

    while nodeA or nodeB:
        result = carry 
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
                



# Practice 

def reverse(rootNode):
    current = rootNode 
    prev = None

    while current: 
        next = current.next
        current.next = prev
        prev = current 
        current = next 
    return prev 


def reverse(rootNode):
    current = rootNode
    prev = None
    while current: 
        next = current.next
        current.next = prev
        prev = current 
        current = next 
    return prev 