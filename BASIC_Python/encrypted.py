while True:
    option = input(f'choose your option:\n1)Encrypt\n2)Decrypt\n3)Exit\n')
    
    if option is '1':
        s = input('Enter your words:')
        encrypt = ''
        for w in s:
            encrypt += chr(ord(w) * 24 + 30 - 3)
        print(encrypt)
    
    elif option is '2':
        s = input('Enter your words:')
        decrypt = ''
        for w in s:
            decrypt += chr((ord(w) + 3 - 30) // 24)
        print(decrypt)
    else:
        break
    print('-' * 80)