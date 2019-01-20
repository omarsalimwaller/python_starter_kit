"""
Primitive Data Types in Python

By: Omar Waller
Playlist: Python Starter Kit

"""

# 1. What makes a data type primitive?
    # A primitive data type is one that is built-in to the language
    # requiring no import of an external library.

#---------INTEGERS-------------
JAYZ = 1
Beyonce = 2


print(type(JAYZ))    


#--------FLOATS---------------
MeekMill = 5.8


print(type((MeekMill)))

a = JAYZ + MeekMill
print(a)

#--------COMPLEX-----------
complex_num = 3+5j

print(type(complex_num))

#-------STRINGS-----------
GOAT = "Lebron James"
print(type(GOAT))

#-------BOOLEAN----------
OmarIsTheGreatest = True

print(type(OmarIsTheGreatest))

#-------LISTS-----------
My_List = [1,2,3,4,5]

print(type(My_List))

#-------DICTIONARY-------
my_dict = {"the_key":"DJ_Khaled","J.Cole is the GOAT": True, "My_age": 45}

print(type(my_dict))



# 2. How can we convert between data types?
    # Python has built-in functions for this:

print(float(Beyonce))

print(int(MeekMill))

print((str(MeekMill)))

print(bin(Beyonce))




