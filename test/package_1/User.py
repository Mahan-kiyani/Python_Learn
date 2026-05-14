from typing import List
from pprint import pprint
#cspell:disable
class UserList(list):
    def search(self, user_name: str) -> List['User']:
        matching_users: List['User'] = []
        for user in self:
            if user_name in user.user_name:
                matching_users.append(user)
                
        return matching_users

class User:
    user_list: List['User'] = UserList()
    def __init__(self, email: str, user_name: str, psw : str) -> None:
        self.user_name = user_name
        self.email = email
        self.psw = psw
        User.user_list.append(self)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.user_name!r}, {self.email!r}, {self.psw!r})'
    
    def __str__(self):
        return f'{self.user_name}'
        
        
class seller(User):
    def order(self, order: 'order') -> None:
        print(f'{self.user_name}, from your product {order} was sold')
            
def main():
        
    user1 = User('gnail', 'mahan', '789') 
    user2 = User('gnail', 'kimia', '798734')
    user3 = User('gnail', 'mahan_kiyani', '00000')
    user4 = User('gnail', 'fati', '339234827')  
    pprint(User.user_list.search('mahan'))
    
    
    
    
    
    
if __name__ == '__main__':
    main()