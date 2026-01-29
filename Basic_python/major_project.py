
def add_student(student_id, name, *marks, **details):
    total = sum(marks)
    student = {
        "student_id" : student_id,
        "name" : name,
        "marks" : marks,
        "total" : total,
        "detail" : details,
    }
    
    
    
# choice = 1

# match choice:
#     case 1 :
#         # Add student
#     case 2:
#         # view student
#     case 3:
#         # search student
#     case 4:
#         # delete student
#     case 5:
#         # exit
        