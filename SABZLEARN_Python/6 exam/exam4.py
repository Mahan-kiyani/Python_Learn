# from math import sqrt
# def jazr(num):
    
#     if sqrt(num) % 1 == 0:
#         return True
#     else:
#         return False
    
    
def jazr2(num):
    
    for i in range(1, num//2):
        if i ** 2 == num:
            return True
        
    else:
        return False
    
num = int(input('Enter Number : '))
print(f'javab is {jazr2(num)}')