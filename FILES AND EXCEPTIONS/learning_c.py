# message = "hello, sam ram is here"
# print(message)

# msg = message.replace("sam", "mahesh")
# print(msg)

from pathlib import Path

path = Path('FILES AND EXCEPTIONS\learning_python.txt')

content = path.read_text()
content = content.replace('python', 'c')
print(content)


# write in a file

# path.write_text("hello these text added through 'write_text()'")
# print(path.read_text())
