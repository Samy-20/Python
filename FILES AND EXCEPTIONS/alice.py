from pathlib import Path

path = Path('FILES AND EXCEPTIONS/alice.txt')

try:
    contents = path.read_text(encoding='utf-8')
    print(contents)
except FileNotFoundError:
    print(f"File {path} not exist")\
        
        