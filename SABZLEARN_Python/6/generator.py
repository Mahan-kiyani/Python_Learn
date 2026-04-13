# tamrinat fasl 6 sabzlearn = generator
# --------------------------------------------

# def my_enumerate(li):
#     for i in range(len(li)):
#         yield li[i], i
        

# lst = ['a', 'b', 'c', 'd']
# x = my_enumerate(lst)
# ---------------------1----------------------

# def fibo():
#     yield (a := 0)
#     yield (b := 1)
#     while True:
#         yield a + b
#         a, b = b, a+b
        
# fib = fibo()

# for _ in range(14):
#     print(next(fib))
# ---------------------2----------------------

# def sum_gen(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#         yield sum
        

# s_g = sum_gen([1, 2, 3, 4, 5, 6, 7])
# for i in s_g:
#     print(i)
# ---------------------3----------------------

# def str_reverse(st) -> str:
#     for i in reversed(range(len(st))):
#         yield st[i]
        
        
# s_r = str_reverse('mahan')
# for j in s_r:
#     print(j)
# ---------------------4----------------------

# def my_gen(even_or_odd='e'):
#     if even_or_odd == 'e':
#         start = 0
#     else:
#         start = 1
        
#     while True:
#         yield (start) 
#         start += 2
        
# for i in my_gen('o'):
#     if i > 100:
#         break
#     print(i)
# ---------------------5----------------------

# def num_gen():
#     num = 1
#     while True:
#         s = ''
#         for _ in range(num):
#             s += f'{num}\t'
#         yield s   
#         num += 1
        

# x = num_gen()
    
# for _ in range(10):
#     print(next(x))
# ---------------------6----------------------