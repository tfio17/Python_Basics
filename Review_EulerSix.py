#
#
#
#
## Tom
#
#
#
## Sum Square Difference - Project Euler
#
#
# find difference between the sum of the squares of the
# first 100 natural numbers and the square of the sum

# Step 1, find sum of squares

num = 100
limit = num + 1
sos = 0
for i in range(1,limit):
    sos = sos + i**2
print(sos)

# Step 2, find square of the sums

sqos = 0
for i in range(1,limit):
    sqos = sqos + i
sqos = sqos**2
print(sqos)

# Step 3, find the difference

print("The diff is:  " + str(sqos-sos))



