from pathlib import Path

path = Path('FILES AND EXCEPTIONS\pi_txt.txt')
content = path.read_text()
# content = content.rstrip() # remove all blank line from terminal afetr the content show on terminal
# print(content)

lines = content.splitlines()
# for line in lines:
#     print(line)

pi_string = ''
for line in lines:
    pi_string += line
    
# print(pi_string)
# print(len(pi_string))


birthday = '2643'
if birthday in pi_string:
    print("Your birthday is appear")
else:
    print("not apper")