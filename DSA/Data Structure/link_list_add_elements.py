class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traverse(head):
    current = head
    
    while current != None:
        print(current.data, end="-")
        current = current.next
        
def appendElement(head, data):
    newNode = Node(data)
    
    # list is empty
    if head is None:
        return newNode
    
    current = head
    
    #
    while current.next != None:
        current = current.next
 
    current.next = newNode
    return head 
        

def insertAtPosition(head, position, data):
    current = head
    newNode = Node(data)
    
    if current.next != position-1:
        current.next = newNode.data 
    

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

# appendElement(n1, 5)
insertAtPosition(n1, 3, 7)
traverse(n1)         
        
