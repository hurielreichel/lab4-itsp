import unittest
from Point import Point
from Rectangle import Rectangle
from Circle import Circle
import math

class TestPoint(unittest.TestCase):

    def test_get_X(self):
        test_point = Point(15, 35)
        self.assertEqual(15, test_point.getX())

    def test_get_Y(self):
        test_point = Point(15, 35)
        self.assertEqual(35, test_point.getY())

    def test_setX(self):
        test_point = Point(0, 0)
        self.assertEqual(15, test_point.setX(15))

    def test_setY(self):
        test_point = Point(0, 0)
        self.assertEqual(35, test_point.setY(35))

    def test_setPosition(self):
        test_point = Point(0, 0)
        test_point = test_point.setPosition(15, 35)
        self.assertEqual(15, test_point.getX())
        self.assertEqual(35, test_point.getY())

    def test_distance(self):
        test_point = Point(0, 1)
        self.assertEqual(1, test_point.distance(1,1))

    def test_toString(self):
        test_point = Point(15, 35)
        self.assertEqual("Point ( 15.0, 35.0 )", test_point.toString())

    def test_set(self):
        test_point = Point(0,1)
        test_point = test_point.set(1, "red", "blue")
        self.assertEqual(1, test_point.strokeWidth)
        self.assertEqual("red", test_point.strokeColour)
        self.assertEqual("blue", test_point.fillColour)
        
    def test_get(self):
        test_pt = Point(0, 1)
        test_rec = test_pt.set(1, "red", "blue")
        self.assertEqual((1, 'red', 'blue'), test_pt.get())

class TestRectangle(unittest.TestCase):

    def test_gettopLeftPoint(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        self.assertEqual(0, test_rec.gettopLeftPoint().getX())
        self.assertEqual(0, test_rec.gettopLeftPoint().getY())

    def test_getwidth(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        self.assertEqual(10, test_rec.getwidth())
        
    def test_getheight(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        self.assertEqual(20, test_rec.getheight())

    def test_settopLeftPoint(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        test_rec.settopLeftPoint(20)
        self.assertEqual(20, test_rec.gettopLeftPoint())

    def test_setwidth(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        test_rec.setwidth(30)
        self.assertEqual(30, test_rec.getwidth())

    def test_setheight(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        test_rec.setheight(30)
        self.assertEqual(30, test_rec.getheight())

    def test_area(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        self.assertEqual(200, test_rec.area())

    def test_perimeter(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        self.assertEqual(60, test_rec.perimeter())

    def test_contains(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        test_pt = Point(1,1)
        self.assertEqual(True, test_rec.contains(test_pt))

    def test_centroid(self):
        test_rec = Rectangle(Point(0,0), 10, 10)
        centroid = test_rec.centroid()
        test_pt = Point(5, 5)
        self.assertEqual(test_pt.getX(), centroid.getX())
        self.assertEqual(test_pt.getY(), centroid.getY())

    def test_toString(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        #print(test_rec.toString())
        self.assertEqual("The Rectangle [topLeftPoint = Point ( 0.0, 0.0 ), width = 10.0, height = 20.0]" , test_rec.toString() )

    def test_test_set(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        test_rec = test_rec.set(1, "red", "blue")
        self.assertEqual(1, test_rec.strokeWidth)
        self.assertEqual("red", test_rec.strokeColour)
        self.assertEqual("blue", test_rec.fillColour)

    def test_get(self):
        test_rec = Rectangle(Point(0,0), 10, 20)
        test_rec = test_rec.set(1, "red", "blue")
        self.assertEqual((1, 'red', 'blue'), test_rec.get())

class TestCircle(unittest.TestCase):

    def test_getcenterPoint(self):
        pt = Point(0,0)
        cir = Circle(Point(0,0), 10)
        self.assertEqual(pt.getX(), cir.getcenterPoint().getX())
        self.assertEqual(pt.getY(), cir.getcenterPoint().getY())

    def test_getradius(self):
        cir = Circle(Point(0,0), 10)
        self.assertEqual(10, cir.getradius())
        
    def test_setcenterPoint(self):
        pt = Point(0,0)
        cir = Circle(Point(2,2), 10)
        cir.setcenterPoint(pt)
        self.assertEqual(pt.getX(), cir.getcenterPoint().getX())
        self.assertEqual(pt.getY(), cir.getcenterPoint().getY())
        
    def test_setradius(self):
        cir = Circle(Point(0,0), 10)
        cir.setradius(5)
        self.assertEqual(5, cir.getradius())

    def test_area(self):
        cir = Circle(Point(0,0), 10)
        self.assertEqual(round(math.pi*10**2, 1), cir.area())

    def test_perimeter(self):
        cir = Circle(Point(0,0), 10)
        self.assertEqual(round(2*math.pi*10, 1), cir.perimeter())
        
    def test_contains(self):
        pt = Point(5,5)
        cir = Circle(Point(0,0), 10)
        self.assertEqual(True, cir.contains(pt))
        
    def test_toString(self):
        cir = Circle(Point(0,0), 10)
        self.assertEqual("The Circle [CenterPoint : Point ( 0.0, 0.0 ), radius : 10.0]", cir.toString())

    def test_test_set(self):
        test_cir = Circle(Point(0,0), 10)
        test_cir = test_cir.set(1, "red", "blue")
        self.assertEqual(1, test_cir.strokeWidth)
        self.assertEqual("red", test_cir.strokeColour)
        self.assertEqual("blue", test_cir.fillColour)

    def test_get(self):
        test_cir = Circle(Point(0,0), 10)
        test_cir = test_cir.set(1, "red", "blue")
        self.assertEqual((1, 'red', 'blue'), test_cir.get())

if __name__ == '__main__': 
    unittest.main()
