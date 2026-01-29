name = ["hello", "bro", "sam"]

it = iter(name)
for i in range(3):
    print(next(it))
    i += 1
    