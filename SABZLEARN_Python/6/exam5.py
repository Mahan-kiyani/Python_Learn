li = [2, 8283, 82, 83, 99, 10, 32, 54, 3, 6,8,4,2,6,7]

zoj = len(list(filter(lambda x: x % 2 == 0, li)))
fard = len(list(filter(lambda x: x % 2 != 0, li)))

print(f'zoj = {zoj}\nfard = {fard}')

