from pprint import pprint

class BaseClass:
    num_base = 0
    
    def cal_base(self):
        print('call base calls')
        self.num_base += 1
        
        
class LeftClass(BaseClass):
    num_left_base = 0
    
    def cal_base(self):
        # BaseClass.cal_base(self)
        super().cal_base()
        print('call num left base')
        self.num_left_base += 1
    

class RightClass(BaseClass):
    num_right_base = 0
    
    def cal_base(self):
        # BaseClass.cal_base(self)
        super().cal_base()
        print('call num right base')
        self.num_right_base += 1

class DownClass(RightClass, LeftClass):
    num_down_base = 0
    
    def cal_base(self):
        # RightClass.cal_base(self)
        # LeftClass.cal_base(self)
        super().cal_base()
        print('call num down base')
        self.num_down_base += 1
        
        
d = DownClass()
d.cal_base()
print(40 * '-')
pprint(DownClass.__mro__)