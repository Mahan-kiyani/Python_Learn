class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.scores = {'riazi': None , 'zist': None , 'fizik': None}
        
        
    def score(self, lesson, nomre):
        self.scores[lesson] = nomre
        return self.scores
    
    def avg(self):
        avarage = 0
        i = 0
        for score in self.scores.values(): 
            if type(score) is int:
                avarage += score
                i += 1
                
        print(f'avarage = {avarage / i}')
        
    
def main():
    s1 = Student('mahan', 23)
    s1.score('fizik', 20)
    s1.score('riazi', 11)
    s1.score('zist', 17)
    
    s1.avg()

if __name__ == '__main__':
    main()
                
        