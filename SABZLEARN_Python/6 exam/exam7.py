li = [1, 2, 3, 43, 54, 32, 13, 17, 98, 100]

print(list(filter(lambda x: x % 2 == 0, li)))
print(list(filter(lambda x: x % 2 != 0, li)))
