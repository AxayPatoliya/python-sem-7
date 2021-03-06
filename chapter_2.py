# chapter - 2: Python Decision making and Loops:

# conditional statements
# if - exception will not be handled
a = 1
if a==1:
    print("value of a is 1")

# if...else - Exception will be handled
b = 3
if b==3:
    print("value of b is 3")
else:
    print("value of b is not 3")

# elif - we can check multiple condition with elif
c = 6
if c==4:
    print("value of c is 4")
elif c==5:
    print("value of c is 5")
else:
    print("value of c is neither 4 nor 5")

# Boolean expressions
print(1 == 2)
print(1 >= 2)
print(1 <= 2)
print(1 != 2)

# while loop
k = 10
while k!=0:
    print(k) #print the value of k untill it reaches to 0
    k-=1

# for loop
name = "guido van rossum"
for i in name:
    print(i)

# nested loop
name = ["one", "two", "three", "four"]
for i in name:
    for j in i:
        print(j)
    print()

# infinite loop
# a = 5
# while a==5:
#     print("value of a is 5") #this line will be printed infinite times because we didn't write any breaking condition

# break statement - if particular condition gets satisfied then loop will be terminated from there
friends = ["dip", "axay", "shubham", "study", "bonde", "shivani", "rajvi"]
for i in friends:
    print(i)
    if i == "study":
        break

# continue statement - it is used to jump one iteration when condition gets satisfied, if we want to print the numbers from 1 to 10 except 6 then...
for i in range(1,11):
    if i == 6:
        continue
    else:
        print(i)

# pass statement - it does nothing, The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute
for i in range(10):
    pass

# iterations using for and while loop
for i in range(10):
    print(i)

num = 0
while num!=10:
    print(num)
    num+=1

# manipulate lists, sets, and dictionaries
lst = [1,2,3,4,5,6,7,8,9,10]
lst[0] = "replaced" #it will change the first element of a list
print(lst)

tup = (1,2,3,4,5,6,7,8,9,10)
# tup[0] = "tuple" #it will throws an error because tuples are unmutable i.e. we can't change tuples values as we can do in lists

dic = {"name":"sam", "profession":"cloud engineer"}
dic["name"] = "martin" #this will change value of the key "name"
print(dic)