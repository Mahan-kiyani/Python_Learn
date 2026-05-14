import os
import time
os.system('clear')

def funk1(a, b, /, c, k):
    
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'k = {k}')
    print('----------------------')
    
    
def funk2(a, *, b, c):
    
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print('----------------------')
    
funk1(1, 2,c=4, k=7)
#print(funk1(a=1, b=2, c=4, k=7)) Error

funk2(1, b=12, c=13)
