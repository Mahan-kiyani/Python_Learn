def Sum(lst):
    Sum = 0
    for num in lst:
        Sum += num
        
    return Sum

lst = [2, 43, 12, 54, -12, 32, 43]

print(Sum(lst))
