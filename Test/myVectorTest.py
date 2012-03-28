from mypackage import Oppg2

import unittest
import sys

class TestVector(unittest.TestCase):
    def setUp(self):
        self.v1 = Oppg2.Vector( Oppg2.Point( 4, 2), Oppg2.Point( 2, 4 ) )
        self.v2 = Oppg2.Vector( Oppg2.Point( 4, 2), Oppg2.Point( 2, 4 ) )
        self.v3 = Oppg2.Vector( Oppg2.Point( 1, 1), Oppg2.Point( 2, 4 ) )
    
    def test_setter(self):
        self.v1.p1 = Oppg2.Point( 5, 6)
        self.assertEqual( self.v1.p1, Oppg2.Point( 5, 6 ))
    
    def test_equal(self):
        self.assertEqual( self.v1, self.v2, "Inncorrect Vector returned")
    
    def test_not_equal(self):
        self.assertNotEqual( self.v1, self.v3 )


    
        
if __name__ == '__main__':
    print( "Main" )
    unittest.main()
        
        

