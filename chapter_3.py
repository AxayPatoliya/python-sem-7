# NOTE: Defining custom functions

# functions: functions can be defined as a block of code or commands that is reusable and callable whenever we require
# it takes the number of arguments and performs the operation using that argument or on the argument based on the code or command wrriten inside the function
# we can define a function using def keyword in python

# SYNTAX ->
def function_name():
    # block of code goes here
    pass

# examples of function
def addNums(a,b):
    print(a+b)
addNums(1,2)

# NOTE: variable scopes in Python
# 1)Global variables->
# Global variables are the ones that are defined and declared outside any function and are not specified to any function. They can be used by any part of the program.
s = "this is a variable named s"
def globalScope():
    print(s)
globalScope()

# 2)Local Scope ->
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def localScope():
    a = "this is a variable named a"
    print(a)
# print(a) #it will raise a NameError as a is the local scope variable so we can't access it outside the function

# 3)global keyword -> this helps us to access the local variable by making local variable global
def globalScope():
    global k 
    k = 'this is a variable named k'
    print(k)
globalScope()
print(k)

# NOTE: work with date and time
from datetime import datetime
# we used here datetime for an example but we can use datetime, time, calender as well

print(datetime.today()) #this will prints the current date and time
print(datetime.today().date()) #this will prints the current date only
print(datetime.today().time()) #this will prints the current time only
print(datetime.today().year) #this will prints the current year only
print(datetime.today().month) #this will prints the current month only
print(datetime.today().day) #this will prints the current date only(without month and year)

# NOTE: get started with dictionaries
# --> dictionaries in python are basically combination of key value pair. it may contain any datatype in key as well as value.
dict_sample = {'name':'Rajvi', 'specialization':'BE IC', 'institute':'VGEC', 'occupation':'automation engineer'}

# here name, specialization, institute and occupation are the keys. and Rajvi, BE IC, VGEC, automation engineer are the values accordingly


# printing the whole dictionary
print(dict_sample)

# iteration over the dictionaries key & values
for i in dict_sample:
    print(i + '-' + dict_sample[i])

# operations we can perform on dictionaries
# 1) adding the element
dict_sample['hobby'] = 'reading' #it will append the hobby as a key and reading as the value of it to the dictionary
print(dict_sample)

del dict_sample['occupation'] #it will remove the key occupation and its value from the dictionary
print(dict_sample)

print(dict_sample.items()) #Returns a list containing a tuple for each key value pair

print(dict_sample.keys()) #Returns a list containing the dictionary's keys

print(dict_sample.values()) #Returns a list containing the dictionary's values

dict_sample.pop('institute') #Removes the element with the specified key
print(dict_sample)


# NOTE: Programming using functions
def sayIntro(name, id, role):
    print("name of the employee - ", name)
    print("id of the employee - ", id)
    print("role of the employee - ", role)

sayIntro('Dip', '2E4F', 'Senior Developer') #it is driver code to call the function sayIntro, it will take 3 parameters as arguments and gives the output as per the commands writted inside a function


# NOTE: What are Python Modules?
# In Python, Modules are simply files with the “.py” extension containing Python code that can be imported inside another Python Program.

# In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that you want to include in your application.

# NOTE: What are External Modules?
# In Python, we can use the predefined function and classes from the python packages/modules
# example - pandas, numpy, sci-kit learn, matplotlib, seabborn