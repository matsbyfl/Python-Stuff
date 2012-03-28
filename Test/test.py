#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright meg
"""
from __future__ import print_function 
import time
import math
import random

__version__ = "$REV$"
__author__ = "Stu dent <stu@dent.com>"



def main():
    """module main for standalone execution"""
    print( "{0}.".format( "Hello World" ))

    words = "the quick brown fox jumped over the lazy dog"
    words_list = words.split()
    print( words_list )
    #words_list.reverse()
    
    reversed_words_lists = words_list[-1::-1] 
    print( reversed_words_lists )
    ferdig = " ".join( reversed_words_lists )
    print("Sånn: {0}".format( ferdig ) )
    print( "".join(list(reversed(words[::-1]))) )
    
x = 1 
y = 2

def foo():
    x=3
    def bar(z):
        return (x + y ) * z
    return bar


def f1():
    x = 2 
    def inner():
        print( "x={0}".format(x))
    inner()

def power( x, pwr ):
    return x ** pwr

def isPrime( number ):
    if number > 1:
        divisors = range( 2, number -1 )
        for divisor in divisors:
            if number % divisor == 0:
                return "false"
        else: 
            return "true"
    

def optimus( stop ):
    startTime = time.time()
    primes = []
    for number in range( 2, stop +1 ):
        if isPrime( number ) == "true":
            primes.append( number)
    stopTime = time.time()
    printResult( len(primes), stopTime - startTime )

def superFast( stop ):
    startTime = time.time()
    primes = [2]
    for number in range( 3, stop +1, 2 ):
        isPrime = True
        for prime in primes:
            if number % prime == 0:
                isPrime = False
                break
        if isPrime:   
            primes.append(number)
    stopTime = time.time()
    printResult( len(primes), stopTime - startTime )
    
def squirt( stop ):
    startTime = time.time()
    primes = [2]
    # Only step through odd numbers
    numbers = range( 3, stop + 1, 2 )
    for number in numbers:
        isPrime = True
        for prime in primes:
            root = int(math.sqrt(number))
            print( number, prime, root ) 
            if  root > prime:
                isPrime = False
                break
            if number % prime == 0:
                isPrime = False
                break
        if isPrime:   
            print( "Hit {0}".format( number ))
            primes.append(number)
    stopTime = time.time()
    printResult( len(primes), stopTime - startTime )

def printResult( count, delta ):
    if delta < 1:
        print( "Found {0} primes in {1:.2f}ms".format( count, delta*1000 ))
    else:
        print( "Found {0} primes in {1:.2f}s".format( count, delta ))
        
#if __name__ == "__main__":
#    main()
#    f1()
#    functor = foo()
#    print( "x = {0}".format( functor(8)))
#    print( "3 Squared {0}".format( power(3, 2)))
#    print( "3 cubed {0}".format( power(3, 3)))
#    print( "3 tessrrr {0}".format( power(3, 4)))
squirt( 100 )
superFast( 100000)
#optimus(  100000 )

print( "Ferdig")
