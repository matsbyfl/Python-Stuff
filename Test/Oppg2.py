from __future__ import print_function
import math

class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    def __eq__(self, other):
        return self.origoDist() == other.origoDist()

    def origoDist(self):
        o1 = math.sqrt( self._x**2 + self._y**2 )
        return o1
    
    def __add__(self, other):
        return Vector( self, other )

    def __str__(self):
        return "x: {0} y: {1}".format( self._x, self._y )

class Vector(object):
    def __init__(self, p1, p2):
        self._p1 = p1
        self._p2 = p2
    
    @property
    def p1(self):
        return self._p1
    
    @p1.setter
    def p1(self, value):
        self._p1 = value
    
    @property
    def p2(self, value):
        return self._p2
    
    @p2.setter
    def p2(self, value):
        self._p2 = value
    
    def __str__(self):
        return "P1: {0}  P2: {1}".format( self._p1, self._p2 )
        
        
point1 = Point( 2, 3 )
point2 = Point( 4, 8 )
point3 = Point( 4, 8 ) 
print( point2 == point3 )
#vector = Vector( "eddf", "dfdf")
print( point1 )
print( point2 )
vector = point1 + point2
print( vector )
    
    
        