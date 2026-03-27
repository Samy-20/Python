
def minimum_marks(marks):
    min_marks = marks[0]
    for i in marks:
        if i < min_marks:
            min_marks = i
    return min_marks
    
def average_marks(mark, n):
    i = sum(mark) / n
    return i

def highest_marks(mark):
    high_mark = mark[0]
    for i in mark:
        if i > high_mark:
            high_mark = i
    return high_mark

def display(choice, n):
    for i in n:
        print("")
        
    match choice:
        case 1:
            print("Minimum marks got by student: ", minimum_marks(marks))
            
        case 2:
            print("Maximum marks got: ", highest_marks(marks))
        
        case 3:
            print("Average marks got: ", average_marks(marks, n))
            
             

marks = []
n = int(input("Enter the number of students: "))
for i in range(n):
    x = int(input(f"Enter the marks of student {i+1}: "))
    marks.append(x)

# marks = [10, 20, 30,22, 11]

display(1, n)
