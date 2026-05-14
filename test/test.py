# pyright: reportInvalidTypeForm=false
#cspell:disable

class Student:
    def __init__(self, name: str = 'None', age: int = None, user_id: int = 0):
        self.name = name
        self.age = age
        self.__user_id = user_id
        
    def __str__(self):
        return f'{self.name}({self.age}) : {self.__user_id}'
        
    def __repr__(self):
        return f'{self.__class__.__name__} - {self.name}({self.age}) : {self.__user_id}'
    def moadel(self):
        self.score = int(input('enter num:'))    


stu = Student('Mahan', 23, 487242089908)
print(repr(stu))