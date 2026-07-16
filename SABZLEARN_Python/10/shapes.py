#cspell: disable 

class Shape:
    def __init__(self, **kwargs):
        self.area = 0
        self.perimiter = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def calculate_area(self):
        pass
        
    def calculate_perimiter(self):
        pass
        
    def show(self):
        info = ''
        for key, value in self.__dict__.items():
            if value > 0:
                info += f'{key}: {value:.2f}\n'   
        print(info)       
            
    def __str__(self):
        return self.__class__.__name__


#length, width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def calculate_area(self):
        self.area = self.length * self.width       

    def calculate_perimiter(self):
        self.perimiter = 2 * (self.length + self.width)
        
        
#length 
class Square(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def calculate_area(self):
        self.area = self.length ** 2       

    def calculate_perimiter(self):
        self.perimiter = 4 * self.length
    
    def __call__(self, length):
        self.length = length
        
        
#base, height, side1, side2        
class Triangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def calculate_area(self):
        self.area = (self.base * self.height) / 2       

    def calculate_perimiter(self):
        self.perimiter = self.base + self.side1 + self.side2
        
        
        
r = Square(length=5)
r.calculate_perimiter()
r.calculate_area()
print(r)
r.show()
print('*' * 30)

r(8)
r.calculate_perimiter()
r.calculate_area()
r.show()