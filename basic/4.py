# Number Guessing Game Project

import random

number = random.randint(0, 100)

for _ in range(10):
    
    guess = int(input('Enter a Number you think that is: '))    
    
    if guess < number:
        print('\"\"your guess is lower than\"\"')
        continue
    
    elif guess > number:
        print('\"your guess is Higher than\"')
        continue
    else:
        print('{You won , horraaaa}')
        break