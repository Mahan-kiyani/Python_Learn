import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols = '&$@._'
numbers = '0123456789'

all = lower + upper + symbols + numbers

while True:
    select = input('y/n: ').lower()
    if 'y' in select:     
        length = int(input('length of password: '))

        password = ''.join(random.sample(all, length))
        
        print(password)
    else:
        break

    
        
    