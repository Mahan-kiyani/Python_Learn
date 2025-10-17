from random import choices

lst = ['borna', 'mahan', 'ali', 'neamat', 'omid', 'radman']
num = int(input('num: '))
gyggfdsa    
dic_lis = ['name', 'score', 'game']
lst = []
for i in range(num):
    dic = {}
    dic['name'] = input('name: ')
    dic['score'] = input('score: ')
    dic['game'] = []
    
for i in range(num):    
    for j in range(3):
        print(f'{dic_lis[j]}:{dic[dic_lis[j]]}')
    
# ghore keshi 
# for i in range(len(lst) // 2):
#     x = choices(lst, k=2)
#     print(f'{x[0]} vs {x[1]}')
#     try:
#         lst.remove(x[0])
#         lst.remove(x[1])
#     except ValueError:
#         pass
    
# lis = [
#     {'name': 'mahan', 'score': 3, 'game': ['omid'] },
#     {'name': 'borna', 'score': 3, 'game': ['omid'] },
#     {'name': 'ali', 'score': 3, 'game': ['omid'] },
#     {'name': 'neamat', 'score': 3, 'game': ['omid'] },
#     {'name': 'mahan', 'score': 3, 'game': ['omid'] },
#     {'name': 'mahan', 'score': 3, 'game': ['omid'] },
#     {'name': 'mahan', 'score': 3, 'game': ['omid'] }
#     ]