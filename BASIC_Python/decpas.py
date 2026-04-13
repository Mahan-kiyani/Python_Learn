from functools import wraps

def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if args[0] in blacklist:
            print('this user is blocked')
        else:
            func(*args, **kwargs)

    return inner

@decorator
def print_pas(name):
    '''this function for print name and paswords'''
    print(f'{name}:{paswords[name]}')


paswords = {'mak': '328dshsd01', 'kimi': '3729482989', 'sara': '11312'}
blacklist = {'sara'}

print_pas('sara')
print_pas('mak')