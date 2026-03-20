class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
        
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.rear = self.front = new_node
            self.length += 1
            return 
        self.rear.next = new_node # type: ignore
        self.rear = new_node
        self.length += 1
        
    def dequeue(self):
        if self.isEmpty():
            return "Quueue is Empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        
        if self.front is None:
            self.rear = None
        return temp.data  # type: ignore

    def traverse(self):
        current = self.front
        while current:
            print(current.data, end=' ')
            current = current.next
        print()
        
    def isEmpty(self):
        return self.length == 0
    
    def peek(self):
        print(self.front.data) # type: ignore

q = Queue()
q.enqueue('A')
q.enqueue('B')
q.enqueue('C')
q.traverse()
print(q.dequeue())
q.traverse()
q.peek()