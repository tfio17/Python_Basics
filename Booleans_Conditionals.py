'''

This is a comment

T

Exploring booleans and conditionals

'''

num1 = 12
num2 = 25

test = True
test2 = False


###Relational Operators:

#   >       - greater than
#   <       - less than
#   ==      - equal to
#   !=      - not equal to
#   >=      - greater than or equal to
#   <       - less than or equal to

booltest1 = 12 > 6
print(booltest1)


###Making this interactive

booltest2 = int(input("Enter a number: "))

print(booltest2, "is greater than 10: ", booltest2 >10)

#With criteria as variable
b3 = booltest2 <30

print(booltest2, "is less than 30: ",b3)

###Boolean Algebra

v1 = True
v2 = False

test1 = v1 and v2
test2 = v1 or v2

#print results

print("And:",test1)
print("Or:",test2)

#NOT

test3 = not v1

#Order of preference

#NAO
#Not - And - Or
