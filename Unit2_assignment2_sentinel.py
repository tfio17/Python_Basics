#
#
#
#
#
## Tom Fiorelli
## Unit2_Assignment1
#
## Program to:
# for given list print average of negative numbers that appear before a 999 is detected

MyList = [23,-45,6,-23,-9,77,54,-54,21,-2,8,-3,-23,45,93,-43,999,-2,3,78,90]

a = 0
n = 0

for i in MyList:
    if i == 999:
        break
    else:
        if i < 0:
            a = a + i
            n = n + 1

print(a , n)
print("The Average is:  " + str(a/n))
