s = input('Enter string: ')

for ch in s:
    
    print(f"{ch} = {bin(ord(ch))} and ascii: {ord(ch)}")