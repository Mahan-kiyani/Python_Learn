def funk(a, b, c):
    
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print('----------------------')
    
# Normal
# name = Value
# normal + name = Value
# *iterable (str, list, tuple, set)

funk(3, 1, 4)
funk(a=2, c=5, b=9)
funk(1, 4, c=8)

lst = [7, 9, 2]
funk(*lst)

d = {'b' : 6, 'a' : 2, 'c' : 9}

funk(**d)