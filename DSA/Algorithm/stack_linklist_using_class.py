class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stcak:
    def __init__(self):
        self.head = None # denote a top of stack if head -> none means stack is empty
        self.size = 0 # track total number of elements in stack
        
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head # type: ignore
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty:
            return"Stack is empty"
        pop_value = self.head.value # type: ignore
        self.head = self.head.next # type: ignore
        self.size -= 1
        return pop_value.value
        
    def isEmpty(self):
        return self.size == 0
        
    def peek(self):
        if self.isEmpty:
            print("Stack is empty")
        return self.head.value # type: ignore
        
    def sizeStack(self):
        return self.size
    
    def traverse(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end = "->")
            currentNode = currentNode.next
        print()
        
s1 = Stcak()
s1.push(1)  
s1.push(3)
s1.pop()
s1.traverse()
print(s1.peek())
print(s1.sizeStack())

