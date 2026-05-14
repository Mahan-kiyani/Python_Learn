#cspell: disable

import random

class Bank:
    acc_numbers = set()
    
    def __init__(self, name):
        self.name = name
        
        self.acc_id = None
        while True:
            if (an := random.randrange(10000 , 100000)) not in self.acc_numbers:
                self.acc_numbers.add(an)
                self.acc_id = an
                break
            
        self.balance = 0
        
    def __str__(self):
        return f'{self.name} : {self.acc_id}'
    
    def display(self):
        print(40 * '-')
        print(f'your account balance is {self.balance}')
        print(40 * '-')
    
    def deposit(self):
        amount = float(input('Enter amount to deposit: '))
        self.balance += amount
        self.display()
        
    def withdraw(self):
        amount = float(input('Enter amount to withdraw: '))
        if amount > self.balance:
            print('mojoodi nakafi')
        else:
            self.balance -= amount
        self.display()  
        
acc1 = Bank('Mahan')
acc2 = Bank('kimia')

acc1.deposit()
acc1.withdraw()
