class Bird:
    def wings(self):
        print("Bird has two wings")
    def eyes(self):
        print("Bird has two eyes")
    def fly(self):
        print("Most of the birds can fly")
    
class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can not fly")

bird = Bird()
sparrow = Sparrow()
ostrich = Ostrich()

bird.eyes()
bird.wings()
bird.fly()
ostrich.fly()


