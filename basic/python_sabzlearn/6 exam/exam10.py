lst = ['12', 'sara', '12.78', '2.9', 'melani', 'kimia', '21']

s = lambda x: x.replace('.', '').isdigit()
print(list(filter(s, lst)))