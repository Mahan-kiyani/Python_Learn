#Temperature Converter

def c_f(celsius: float) -> float:
    return (1.8 * celsius) + 32


def f_c(fahrenheit: float) -> float:
    return (fahrenheit - 32) * (5 / 9)


choice = int(input('''\
1)fahrenheit to celsius
2)selcius to fahrenheit

what do you want:

'''))

if choice == 1:
    degree = float(input('Fahrenheit degree: '))
    print(f_c(degree))
    
elif choice == 2:
    degree = float(input('Celsius degree: '))
    print(c_f(degree))
    
else: 
    print('Error!!!\n Your Answer is incorrect')