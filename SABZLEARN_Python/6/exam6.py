li = []
for i in range(5):
    name, age = input('Name and age: ').split('-')
    li.append((name, age))

li.sort(key=lambda li: li[1])
print(li)