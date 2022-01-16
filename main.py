# this is how you leave comments in python
""" 
you can also leave comments
like this across multiple lines
neither of these will be run by the
python interpreter
"""

"""
--------- PRIMATIVE DATA TYPES -----------------
"""

"""
variables are any type of data which is represented
by a keyword which can be referenced in place of that 
data in a program

examples:
"""

#strings

"""
strings are any type of text data which is placed between two
sets of quotes that store text data
"""
my_string = "this is a string"

#numbers (integers, floats)
"""
numbers are any type of data which can have mathmatical
operations done on them, these include integers like 1, 2, 3 and so on
as well as floating point numbers like 2.5, 2.7 etc
"""
my_number = 20
my_second_number = 21
my_third_number = my_number + my_second_number

#booleans

"""
booleans are values and data types which represent the true or false nature of a statement
booleans can either be directly declared or infered from an expression
"""

my_expression_bool = 1 > 0 #True
my_expression_bool_2 = ("andrew" == "andrew") #True
my_bool = False #False

"""
--------- OTHER DATA TYPES -----------------
"""

#arrays

"""
arrays are ordered lists of elements that start at the index 0
you can think about arrays as sequentially ordered boxes that can
each hold a piece of data and be referenced by their positional index
"""

my_array = ["a","b","c","d"]
my_letter = my_array[1] #the value of this statement is b because index's start at 0 and b is the second element

#dictionary

""" a dictionary is a datatype where items can be stored and referenced by key's and values """

my_dict = {
    "name" : "andrew",
    "age": 21,
    "isMale" : True,
}

andrews_age = my_dict['age']

"""
There are a variety of other data types that are useful as you progress however with these
few you can already build complex data structures with the help of the things mentioned next
"""


"""
-------------- OPERATORS -----------------
"""

"""
operators are symbols in python that allow for data to be manipulated, some common operators include
+   is for addition
-   is for subtraction
*   is for multiplication
/   is for division
=   is for ASSIGNMENT
==  is for checking equality
>   is for greater than
<   is for less than

and resolves a True in a boolean expression if both statements are true
or  resolves a True in a boolean expression if one statement is True
not flips the result of a comparison

NOTE: most mathmatical operators allow for a combination with a = which resolves like this
x = x + 3
x += 3

"""


"""
------------ CONTROL FLOW/ STATEMENTS ---------------
"""

"""
control flow is how you either run or ignore blocks of code conditionally in a program
things like if, else, elif allow you to create blocks of code which will either be run
or ignored by the python interpreter when youre program is being executed

all python blocks are seperated by indentation which your IDE (application to write code in) will do for
you upon entering a block with a colon
"""

my_age = 21

if my_age > 20:
    print('this block will be executed')
elif my_age < 20 and my_age > 15:
    print('this block would have run if the first was not True')
else:
    print('this block will not')



"""
------------- LOOPS ----------------
"""

"""
loops are expressions which allow for a block of code to be executed many times 
and can either run conditionally or for a fixed length of time
"""

number = 10

while number < 20:
    number += 1
    print(number)

"""
that expression would start with number = 10 and run until the number was equal to 20
"""

for i in range(0,100):
    print(i)

"""
that expression would print numbers 0 - 99
"""



"""-------------- FUNCTIONS --------------"""

"""
functions are a way to organize code into reusable blocks that can take different inputs
and accomplish a task or return an output

they are defined using the def FUNCTIONNAME(): keyword and any arguments are placed into the parenthasis for reference inside the function
"""

def add_my_numbers(number_one, number_two):
    new_number = number_one + number_two
    return new_number

function_result = add_my_numbers(5,5) #function result is now equal to 10


"""
these methods can be combined in order to produce processed data and much more
"""





