# Generate student reports dynamically using keyword arguments.

def student_report(**kwargs):
    print("student Report")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

student_report(
    name = "sam",
    age = 20,
    course = "B.Tech",
    marks = 85
)


# Output - 

# student Report
# name : sam
# age : 20
# course : B.Tech
# marks : 85