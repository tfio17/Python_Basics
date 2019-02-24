#
#
#
#
## Tom
#
#
#
## Let's Play With Loops

MyList = [2,4,6,8,10,12]

for i in MyList:
    print(i, i**2)
    print('**********')

print('The End')


# The i doesn't matter!!! Try with Fred!

for fred in MyList:
    print(fred, fred**2)
    print('**********')

print('The End')

# Both of these print numbers 1-10

for i in range(1,11,1):
    print(i)

for i in range(11):
    print(i)

#count down from 100

for i in range(100,0,-1):
    print(i)

#same as first example!

for i in range(2,13,2):
    print(i, i**2)
    print('**********')




## How many of the squares under 300 are greater than 50,000????

sqlist = []
for i in range(1,301):
    print(i**2)
    sqlist.append(i**2)


c = 0
a = 0

gt50 = []

for i in sqlist:
    if i > 50000:
        c = c + 1
        a = a + i  #accumulator, c is count, a is sum, counter & accumulater


        #More "pythonic" way to do same task
        #gt50.append(i)

        #print(gt50)
        #print(len(gt50), sum(gt50))
        

# Nested for loop
for i in range(5):
    print('Outer')
    for i in range(3):
        print('Inner')



# First while loop
c = 'y'

while ( c == 'y'):
    print(' OK ')
    c = input("Enter a character:   ")
    
print("The End")



