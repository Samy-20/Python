"""10-4. Guest: Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt."""

from pathlib import Path

path = Path("FILES AND EXCEPTIONS\guest.txt")


name = "sam"
path.write_text("welcome name")
content = path.read_text()
content = content.replace("name", name)
path.write_text(content)
print(content)


