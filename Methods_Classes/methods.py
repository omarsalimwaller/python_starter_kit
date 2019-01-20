# Methods are used to help organize code. They allow parameters to be input,
# some invisible computation, and then boom an output. Let's explore why 
# methods and classes are important.

# Lets take the Pythagorean Theorem for example

# First import math library
import math


def compute_pythag_ther(a,b):
    ''' This method computes the pythagorean theorem for two numbers'''
    
    c = math.sqrt(a*a + b*b)
    return c

print(compute_pythag_ther(7,10))


def quadratic_formula(a,b,c):
    x =[]
    x1 = (-b + math.sqrt(b*b -4*a*c))/2*a
    x2 = (-b - math.sqrt(b*b -4*a*c))/2*a
    
    x.append(x1)
    x.append(x2)
    
    return x

print(quadratic_formula(1,3,-4))
    
















































































