def Mx(*args):
    mx = float('-inf')
    for i in args:
        if i > mx:
            mx = i
        
    return mx

def Mn(*args):
    mn = float('inf')
    for i in args:
        if i < mn:
            mn = i
        
    return mn

print(Mx(1, 76, 32, -12, -123, 323324))
print(Mn(1, 76, 32, -12, -123, 323324))
