import os
import time
os.system('clear')

def funk(a, *c, k=0, b=81):
    
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'k = {k}')
    print('----------------------')
    
def fundict(**d):
    
    print(f'd(a) = {d}')
# Normal
# default value
# normal + default value
# *name

funk(2, 43, 5, 3, k=0)
fundict(a=32, b=12, c=90)
