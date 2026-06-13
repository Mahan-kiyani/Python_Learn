from typing import List
from pprint import pprint
import logging
#cspell:disable


class PrintInfoMixin:
    def print_info(self):
        print(self.__class__.__name__)
        print(self.__dict__)
        
        
class UserList(list['User']):
    def search(self, user_name: str) -> List['User']:
        matching_users: List['User'] = []
        for user in self:
            if user_name in user.user_name:
                matching_users.append(user)
                
        return matching_users
    
    def append(self, object):
        if not isinstance(object, User):
            raise TypeError('This list only accept User')
        return super().append(object)


class User(PrintInfoMixin):
    user_list: List['User'] = UserList()
    
    def __init__(self, email: str, user_name: str, psw : str, **kwargs) -> None:
        self.user_name = user_name
        self.email = email
        self.psw = psw
        User.user_list.append(self)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, {self.psw!r})'
    
    def __str__(self):
        return f'{self.user_name}'
        
    
class Seller(User):
    def __init__(self, shaba:int, **kwargs):
        super().__init__(**kwargs)
        self.shaba = shaba
        
    def order(self, order: 'order') -> None:
        print(f'{self.user_name}, from your product {order} was sold')
        
        
class Buyer(User):
    def __init__(self, phone:str, **kwargs):
        super().__init__(**kwargs)
        self.phone = phone   
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, {self.psw!r}, {self.phone!r})'   


class SellerAndBuyer(Seller, Buyer):
    def __init__(self, score, **kwargs):
        super().__init__(**kwargs)
        self.score = score
         
def main():
        
    pass
if __name__ == '__main__':
    main()