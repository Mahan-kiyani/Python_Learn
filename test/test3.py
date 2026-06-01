from pprint import pprint

class BaseClass:
    num_base = 0
    
    def __init__(self, a, **kwargs):
        self.a = a

        
    def cal_base(self):
        print('call base calls')
        self.num_base += 1
        
        
class LeftClass(BaseClass):
    num_left_base = 0
    
    def __init__(self, c, d, **kwargs):
        super().__init__(**kwargs)
        self.c = c
        self.d = d
        
    def cal_base(self):
        # BaseClass.cal_base(self)
        super().cal_base()
        print('call num left base')
        self.num_left_base += 1
    

class RightClass(BaseClass):
    num_right_base = 0
    
    def __init__(self, e, f, **kwargs):
        super().__init__(**kwargs)
        self.e = e
        self.f = f
        
    def cal_base(self):
        # BaseClass.cal_base(self)
        super().cal_base()
        print('call num right base')
        self.num_right_base += 1

class DownClass(RightClass, LeftClass):
    num_down_base = 0
    
    def __init__(self, g, **kwargs):
        super().__init__(**kwargs)
        self.g = g
        
    def cal_base(self):
        # RightClass.cal_base(self)
        # LeftClass.cal_base(self)
        super().cal_base()
        print('call num down base')
        self.num_down_base += 1
        
        
d = DownClass(a=3, c=43, d=2, e='i', f=7, g='kk')
d.cal_base()

pprint([d.a , d.c, d.d, d.e, d.f, d.g])
print(40 * '-')
pprint(DownClass.__mro__)