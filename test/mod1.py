def func1(n):
    print(list(range(n)))
    
def func2(s):
    c = 0
    for i in s:
        if i == "a":
            c += 1
    print(c)