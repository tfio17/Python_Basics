#
#
#
#
#
## Tom Fiorelli
## Unit2_Assignment1
#
## Program to:
#  1) print, line by line, numbers 1-100
#  2) for multiples of 3, print "Cow" instead of the number
#  3) for multiples of 7, print "Pie" instead of the number
#  4) for multiples of both 3 & 7, print "CowPie" intead of the number

for i in range(1,101,1):
    if i%3 == 0 and i%7 ==0:
        print("CowPie")
    elif i%7 ==0:
        print("Pie")
    elif i%3 == 0:
        print("Cow")
    else:
        print(i)

print("done")
