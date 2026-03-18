queue = []

# Enqueue
queue.append("A")
print(queue)

# Dequeue -> return a first elemnt of queue
queue.pop()
print(queue)

# Peek -> return a first element of queue
peek = queue[0]
print(peek)

# Size
size = len(queue)
print(size)

# isEmpty
if size == 0:
    print("stack is empty")
else:
    pass

