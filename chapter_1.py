# chapter - 1: Introduction, Data Types and Operators

# installation - install it from python.org and set the path variable

# Variables and data types in python
# variables - we can assign any data type to the variable, variable name can be start with any letter as well as "_" or "__". Variable name cannot be start with any special character i.e. "*&^%$#@!()<>?|"
# NOTE: it's not good practice to declare a variable with the name of default python keyword


a = 12
b = 12.2
c = "student name"
d = [1,2,3]
e = (1,2,3)
f = {1,2,3}
g = {"name":"John Dev", "profile":"JavaScript Developer"}

# datatypes - 
# 1) numeric - integer, floar, complex numbers
# 2) dictionary
# 3) boolean 
# 4) set
# 5) Sequence type - string, list, tuple

# integer
a = 12
print(type(a))

# float
b = 12.0
print(type(b))

# complex number
c = 1 + 2j
print(type(c))

# dictionary
d = {"name":"John Dev", "profile":"JavaScript Developer"}

# boolean
yes = True
no = False
print(type(yes))
print(type(no))

# set - we can define set in 2 ways
se = {1,2,3}
se1 = set((1,2,3))
print(type(se))
print(type(se1))

# seuence type
string = "this is a string type"
lst = ["this", "is", "a", "list", "type"]
dictionary = {"type":"dictionary", "name":"dictionary"}

# computations and logical statements using python's operator
# arithmetic operators
print(1+2)
print(1-2)
print(1/2)
print(1*2)
print(1//2) #integer devision - returns integer value after devision
print(1%2) #gives us the reminder after devision

# comparison operators
num1 = 2 
num2 = 3
print(num1 == num2) #compares two numbers
print(num1 != num2) #compares two numbers
print(num1 >= num2) #compares two numbers
print(num1 <= num2) #compares two numbers

# logical operators
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# membership operators - in, not in(used to check if something is inside something or not)
name = "rajvi patel"
print("rajvi" in name)
print("raju" in name)

# Membership operators are operators used to 
# validate the membership of a value. It tests for membership in a
# sequence, such as strings, lists, or tuples.

# identity operators -
print(type("name"))
print(type(12))
print(type(12.0))
print(type([1,2,3]))
print(type({1,2,3}))
print(type((1,2,3)))

# bitwise operators
a = 10
b = 4
# Print bitwise AND operation
print("a & b =", a & b)
# Print bitwise OR operation
print("a | b =", a | b)
# Print bitwise NOT operation
print("~a =", ~a)
# print bitwise XOR operation
print("a ^ b =", a ^ b)


# list, tuple & string operations
# NOTE: list operations
list1 = [] #empty list(list with no elements inside)

list2 = [1,2,3,4,5,6,7,8,9,10] #list with the elements
print(list2)

# adding elements 1 by 1 at the end of the list using append method
list2.append(11)
list2.append(12)
list2.append(13)
list2.append(14)
print(list2)

# adding multiple elements at the end of the list using extend method
list2.extend([15,16,17,18,19,20])
print(list2)

# adding elements at fixed position using insert -> in this method we have to give 2 attributes to the method 1.position where we want to add the element 2.the element which we want to add
list2.insert(1,'added using insert method')
print(list2)

# accessing the elemetns of list using the indexes of list
print(list2[0], list2[1]) #positive indexing starts with the 0th index in python
print(list2[-1], list2[-2]) #negative index starts with the -1th index in python

# removing the elements from the list
# remove method -> in this method we have to specify the element and have to give it as a attribute to the remove method which we want to delete/remove from the list. this method will not returns any value after removeing the element
list2.remove(1) #element with the value 1 will be removed from the list
print(list2)
list2.remove(20) #element with the value 20 will be removed from the list
print(list2)

# pop method -> pop method will remove the last element of the list and it returns the popped value
list2.pop() 

# slicing of the list syntax: list_name[from, to+1]
print(list2[1:5]) #elements from the index 1 to 4 will be printed


# NOTE: tuple operations
tup = tuple('programmingisfun')
print(tup)

# Concatenation of tuple
tup1 = tuple('andmathsislove')

tup = tup + tup1
print(tup)

# slicing of tuple
print(tup[1:10]) #returns the tuple with the elements with the index from 1 to 9

# NOTE: we cant remove the lements from the tuple as we did for the lists

# NOTE: string operations
string = 'strings are always fun'
print(string)

# accessing the elements from the string
print(string[0:5]) #returns the elements from the string with the index 0 to 4

# deletation of a character in string -> we can't delete the element of the string as we did for the lists

# replacing the items of a string
print(string.replace('fun', 'enjoyable')) #it will replace the word fun by enjoyable and returns the new string(it will not affect the original string)
print(string)





