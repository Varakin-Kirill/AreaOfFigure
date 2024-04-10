import math
class Shape:
    def area(self):
        pass

class Circle(Shape, ):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return math.pi * self.radius**2

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        p=(self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    
    def isRect(self):
        a=self.a**2
        b=self.b**2
        c=self.c**2
        if(a==b+c or b==a+c or c==a+b):
            return True
        else:
            return False