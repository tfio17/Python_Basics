#
#
#
#
#
## Tom Fiorelli
## Unit2_Quiz
#
## Program to:
#  1) create a list of natural numbers from 1-200
#  2) then iterate through list and sum multiples of 17
#  3) print the sum?

L = list(range(1,201,1))
a=0

for i in L:
    if i%17==0:
        a = a + i

print("The sum is:  ", a)
