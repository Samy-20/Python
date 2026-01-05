# list a muable datatype
# always list is bind with []

# l = list(["Elantra", "golf GTI", "civic type-r", "Cherelote"]) 
# l.append("Pajero")
# print(l)
# l.remove("Pajero")
# print(l)


# Extend list

# formula = ["Formula E", "Formula F1"]
# hacthback = ["Polo GTI", "Civiv type-R"]
# formula.extend(hacthback)
# print(formula)

# # hacthback.clear()
# # print(hacthback)

# for i in formula:
#     print(i)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)