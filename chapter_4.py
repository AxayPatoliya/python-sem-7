# NOTE: Python File Operations


# Where the following mode is supported for the file operations:
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will not be deleted.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.

# NOTE: reading the existing file using 'r'


with open('file_handling.txt', 'r') as f:
    print(f.read()) #this will reads the file line by line
    print(f.read(10)) #this will reads the first 10 characters only frm the file
    f.close() #it is mendatory to close the file after reading the file
    
# NOTE: appending the text to the existing file using 'a'
with open('file_handling.txt', 'a') as f:
    f.write('This is a new line added by using the Python modules for File operations.')
    f.close() #it is mendatory to close the file after writing or appending the text

# NOTE: creating a new text file and writing into it
with open('new_using_python.txt', 'w') as f:
    f.write('This is a new text file created using the Python file operator')
    f.close()


# NOTE: writing to the CSV files
import csv #we have to import the csv module in order to work with the CSV files in Python
with open('file_handling.csv', 'w') as f:
    csv_file = csv.writer(f)
    csv_file.writerow(['name','id','specialization'])
    csv_file.writerows([['dip',1,'ic'],['rajvi','2','ic'],['shubham','3','game developer'],['parthav','4','NLP expert'],['shivani','5','automation']])


# NOTE: reading the existing CSV files
with open('file_handling.csv', 'r') as f:
    csv_file = csv.reader(f)
    print(csv_file.line_num)


# NOTE: handling the single exception
# Error in Python can be of two types i.e. Syntax errors and Exceptions. Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. 

# we can handle the exception using the try and catch block
try:
    print(a) #we havent declared the variable a yet so this will throuws an NotDefined error and execution goes to the exception blovk
except:
    print('a is not defined')

# NOTE: handling the multiple exception
try:
    import panda
    prin('hey')
except ModuleNotFoundError as e:
    print('check the spelling of a module you want to import')
except NameError as e:
    print('check the syntax and correct it accordingly')
