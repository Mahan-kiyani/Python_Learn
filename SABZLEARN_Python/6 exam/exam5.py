lst = [1, 43, 32, 5, 6, 82, 12, 54, 0, 54, 3]

rslt = len(list(filter(lambda x: x % 2 == 0, lst)))

print(f'zoj:{rslt} and fard: {len(lst) - rslt}')