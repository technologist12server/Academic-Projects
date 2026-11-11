from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Square(Shape):
    def __init__( self, side ):
        self.side = side
    def area( self ):
        return self.side * self.side
    def perimeter( self ):
        return 4 * self.side
square_obj = Square( 10)
print( "Area of Square: ", square_obj.area() )
print( "Perimeter of Square: ", square_obj.perimeter() )