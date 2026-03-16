"""10-5. Guest Book: Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called guest_book.txt. Make sure each entry appears on a new line in the file."""
 
from pathlib import Path

path = Path("FILES AND EXCEPTIONS\guest_book.txt")



list = ["sam", "ram", "mahesh"]

# for name in list:
#     change = f"welcome, {name}"
#     content = path.write_text(change)
    
# print(path.read_text())
    
y = 5
for x in y:  
    change += "hello world"
    path.write_text(change)

print(path.read_text())