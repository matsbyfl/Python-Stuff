#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__  import print_function 

class FirstClass( object ):
    """ This is the firstest class ever...."""
    def __init__(self, value, secret ):
        self.value = value
        self.__hidden = secret # __ declare this fella as private
        
    @property        
    def hidden(self):
        """Return the, otherwise, hidden value"""
        "Tadaaa"
        return self.__hidden
    
    @hidden.setter
    def hidden(self, value):
        self.__hidden = value
    
#    @hidden.deleter    
#    def hidden(self):
#        print( "Neggu")
#        return
#end class def

#obj = FirstClass( 2, 4 )
#print( obj.hidden )
#obj.hidden = 33 
#print( obj.hidden )




lines = ["en\n", "to\n", "tre\n"]
stream = open("/home/student/test.txt", 'w' )
stream.writelines( lines )
stream.close()


newStream = open("/home/student/test.txt", "r" )
for line in newStream:
    print( line.strip() )


print( "Reading with with")

with open( "/home/student/test.txt" ) as mats:
    



