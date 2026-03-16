from pathlib import Path

path = Path('FILES AND EXCEPTIONS\learning_python.txt')

content = path.read_text()

for line in content:
    print(line)

print(content)