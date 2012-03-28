from __future__ import print_function


class Stack(list):
    
    def __init__(self):
        list.__init__(self)
        print( "initing")
    
    def pop(self):
        print( "Popping" )
        return list.pop( self )
    
    def push(self, value):
        print( "Appending {0}".format( value ))
        #list.append( self,value )
        self.append( value )
        
    def append(self, value):
        print( "Appending {0}".format( value ))
#        self.append( value )
        list.append( self,value )
    
    def printme(self):
        print( "Stack is now " )

stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
stack.push("d")
stack.append( "e" )

print( stack.pop())
print( stack.pop())

        
    