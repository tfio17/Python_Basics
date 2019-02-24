#
#
#
#Tom Fiorelli
#
#Penny Program
#
#
#

print('*********')
print('The Penny Program')
print('*********')

pennies = int(input("How many pennies do you have? "))

#Determine how many quarters there are

quarters = pennies // 25
print(quarters, "Quarters")

pennies = pennies - (quarters * 25)

#Determine the dimes

dimes = pennies // 10
print(dimes, "Dimes")

pennies = pennies - (dimes * 10)

#Determine the nickels

nickels = pennies // 5
print(nickels, "Nickels")

pennies = pennies - (dimes * 5)
