#object overloading
#create a class
class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __add__(self,other):
        return(self.x + other.x , self.y + other.y)
''' The __add__ method of the Point class is used to overload the + operator for two Point objects. 
    This method takes two arguments, self and other.
    The self argument refers to the object on the left side of the + operator, 
    and other refers to the object on the right side of the + operator.'''    
    
def __str__(self) -> str:
    return f"{self.x},{self, y}"
'''the str method is used to convert object to the string 
    the formatted string is represented the x & y value of this variables'''
    
p1 = Point(1,4)
p2 = Point(3,5)
#the p1 & p2 pointer object  is used to store this 
    #addition of two object
p3 =p1 + p2 #this operatin print the value of the tuple

print(p3)