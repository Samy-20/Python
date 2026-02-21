# 🔴 PROBLEM (Advanced)
# Task:
# Create a program that:
# Opens a file
# Reads data
# Handles file not found error
# Ensures file is always closed using finally

try:
    fileName = "demo.txt"
except FileNotFoundError:
    print("These file was not found")
else:
    f = open(fileName, "r")
    print(f.read())
finally:
    try:
        f.close()
        print("File  close successfully")
    except:
        pass