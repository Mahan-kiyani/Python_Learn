def Max(*args):
    
    max_num = float('-inf')
    for i in args[0]:

        if i > max_num:
            max_num = i
        
    return max_num

def Min(*args):
    
    min_num = float('inf')
    for i in args[0]:
        if i < min_num:
            min_num = i
        
    return min_num

print(Max([2, 72, 12, 231, 344, 2, 8, 9, 234]))