# simple Calculator, Python code





while True:
    
    operation = input('Enter your operation: ')
    num_1 = int(input('Enter number: '))
    num_2 = int(input('Enter number: '))
    
    match operation:
        case '+':
            reslt = num_1 + num_2
        
        case '-':
            reslt = num_1 - num_2
            
        case '*':
            reslt = num_1 * num_2
        case '/':
            reslt = num_1 / num_2
            
    break 


if isinstance(reslt, int):
    print(reslt)