class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        self.queue.pop()
        
    def isEmpty(self):
        if self.isEmpty:
            self.queue.pop
        return "stack is empty"
            
    def size(self):
        return len(self.queue)
    
    def traverse(self):
        for i in self.queue:
            print(i)
    
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.dequeue()
q.traverse()

        