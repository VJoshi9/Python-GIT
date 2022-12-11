# classesObject.py
class Laptop:
    def __init__(self)  :
        

        print("Hello World")
    
    def config(self):
        print("DELL", "i5 11th gen, 1TB HDD, 256GB SSD")

laptop1 = Laptop()
laptop2 = Laptop()
# Laptop.config(laptop1)
# Laptop.config(laptop2)
laptop1.config()
laptop2.config()









class Student:
    def __init__(self, name,rollNo):
        self.name = name
        self.rollno = rollNo
    def info(self):
        print("name is : ", self.name, "roll number is : ", self.rollno)
student1 = Student("Vinay","33")
student2 = Student("Paras","32")

student1.info()
student2.info()

print(id(student1))
print(id(student2)) 


class Person:
    def __init__(self) :
        self.name = "Vinay"
        self.number = 9
    def compare(self, other):
        if(self.number == other.number):
            return True
        else:
            return False

p1 = Person()
p2 = Person()

p2.number = "10"

if p1.compare(p2):
    print("same")
else:
    print("Different")

print(p1.number)
print(p2.number)

class Car:
    # Instance variables: The value of those variables which varies from object to object.
    def __init__(self):
        self.company = "BMW"
        self.mileage = 10

car1 = Car()
car2 = Car()

Car.wheels = 4
print(car1.mileage, car1.wheels)
print(car2.mileage, car2.wheels)



