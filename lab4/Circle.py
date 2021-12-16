from Point import Point
from Shape import Shape
import math

class Circle(Shape):

    def __init__(self, centerPoint, radius):

        self.centerPoint = centerPoint
        self.radius = float(radius)
        
    def getcenterPoint(self):

        return(self.centerPoint)

    def getradius(self):

        return(self.radius)
        
    def setcenterPoint(self, centerPoint):

        self.centerPoint = centerPoint

        return(self.centerPoint)

    def setradius(self, radius):
    
        self.radius = radius
    	
        return(self.radius)

    def area(self):

        a = float( round(math.pi * self.getradius() ** 2, 1) ) 

        return a

    def perimeter(self):

        p = float( round(2 * math.pi * self.getradius(), 1) )

        return p

    def contains(self, point):

        if ((point.getX() - self.getcenterPoint().getX()) * (point.getX() - self.getcenterPoint().getX()) +
            (point.getY() - self.getcenterPoint().getY()) * (point.getY() - self.getcenterPoint().getY()) <= self.radius * self.radius):

            return True

        else:

            return False

    def toString(self):

        return "The Circle [CenterPoint : " + self.centerPoint.toString() + ", radius : " + str(self.radius) + "]"
