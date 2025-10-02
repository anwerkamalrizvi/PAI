from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def Area(self):
        pass
class Rectangle(Shape):
    def Area(self,len,wid):
        self.len = len
        self.wid = wid
        finalArea  = len * wid
        print(f"The Area of rectangle is: {finalArea}")
 #       pass
class Square(Shape):
    def Area(self,side):
        self.side = side * side
        print(f"Area of square is: {self.side}")

    #-def display(self):
     #   print(f"Area is: {self.side}")-
    
        
class Triangle(Shape):
    def Area(self,base,altitude):
        self.base = base
        self.altitude = altitude
        finalArea = 1/2 * base * altitude
        print(f"The area of triangle is: {finalArea}")
#        pass

Square().Area(20)
Square().Area(23)
Triangle().Area(4,5)
Rectangle().Area(54,2)
#Square().display()