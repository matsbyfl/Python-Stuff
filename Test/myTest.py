from mypackage import Oppg2

import unittest
import sys

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Oppg2.Point(4,2)
        self.p2 = Oppg2.Point(2,4)
    
    def test_setter(self):
        self.assertEqual( self.p1, Oppg2.Point(4,2), "Points do not match")
        self.p1.x = 6
        self.assertEqual(self.p1.x, 6)
    
    def test_add(self):
        v1 = self.p1 + self.p2
        print( "V1 {0}".format(v1) )
        v2 = Oppg2.Vector( Oppg2.Point( 4, 2), Oppg2.Point( 2, 4 ))
        print( "V2 {0}".format(v2) )
        self.assertEqual( v1, v2, "Inncorrect Vector returned")


    
        
if __name__ == '__main__':
    print( "Main" )
    unittest.main()
        
        

