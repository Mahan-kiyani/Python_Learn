def tekrar(num, Multy):
    stage = 0
    for i in num:
        if i == Multy:
            stage += 1
            
    return stage

num = input('num: ')
multy = input('Multy: ')

print(tekrar(num, multy))