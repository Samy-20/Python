# # stack is a collection of element that folows last-in-first-out principle

# stack = []

# # push
# stack.append('A')
# stack.append('B')
# stack.append('C')

# print("Stack:", stack)

# # pop
# stack.pop()
# print("Stack:", stack)

# # peek 
# peek_element = stack[-1]
# print("peek", peek_element)

# # isEmpty
# isEmpty = not bool(stack)
# print(isEmpty)

# # size
# size = len(stack)
# print(size)


# create a stack using a class 

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
        
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
s = Stack()
s.push('a')
s.push('d')
s.pop()
s.pop()
s.pop()

print(s.stack)
print(s.isEmpty())

