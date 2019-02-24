#This is a comment
###My first Python Program
#
# Author: Tom Fiorelli
#

print("Hello World")

'''

Everything typed here is comments,
we can use these instead of a number
sign for multiline comments.

Number sign (#) is called an octothorpe btw...

'''

print("Done w my comments")

###Lesson_One:  Arithmetic

#Define some variables
a = 34
balance = 74

first_num = 7
second_num = 17

sum = first_num + second_num
diff = first_num - second_num
product = first_num * second_num
quotient_int = first_num // second_num
quotient_float = first_num / second_num

square = first_num**2
remainder = second_num % first_num

print(sum, diff, product, quotient_int, \
      quotient_float, square, remainder)

###Lesson_Two:  Basic Numbers & Words
my_int = 7
my_float = 7.77
my_string = "Hello Everybody"

#Here python's "dynamic typing" recognizes
#the data type and class of our input

print(my_int, type(my_int))
print(my_float, type(my_float))
print(my_string, type(my_string))

