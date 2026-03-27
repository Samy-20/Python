class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
def deleteSpecificNode(head, deleteNode):
    if head == deleteNode:
        return head.next
    
    current = head
    
    while current.next and current.next != deleteNode:
        current = current.next  

def smallestData(head):
    minVal = head.data # starting elment are store in minval
    current = head.next # current node element are store in current 
    while current:
        if current.data < minVal: # compare the current.data with minVal
            minVal = current.data 
        current = current.next
    return minVal
    
def traverse(head):
    current = head # head is a varible which denote a starting point of linklist
    while current != None: # these loop are execute until the curret node is not get Null or we can use "while current:"
        print(current.data, end = " -> ")
        current = current.next
    print("NULL")

n1 = Node(3)
n2 = Node(2)
n3 = Node(0)
n4 = Node(4)

n1.next = n2 # type:  ignore
n2.next = n3 # type: ignore
n3.next = n4 # type: ignore

traverse(n1)
print("Smallest data is : ", smallestData(n1))
deleteSpecificNode(n1,n1)
traverse(n1)



