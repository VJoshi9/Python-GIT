class Student:
    def __init__(self, python, web, math):
        self.subject1 = python
        self.subject2 = web
        self.subject3 = math
    def avgCalculator(self):
        return(self.subject1+self.subject2+self.subject3)/3
    
    
        

student1 = Student(4, 7, 8)
student2 = Student(2, 3, 9)
print(student1.avgCalculator())
print(student2.avgCalculator())
