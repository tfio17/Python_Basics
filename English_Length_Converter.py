#
#Tom Fiorelli
#
#English Length Conversion, inches as input
#
#
#Begin

#Read inches input as integer
inches = int(input("Please enter the number of inches:  "))

#Convert each with // for integer math, typecast as string for concatenation
feet = str(inches // 12)
yards = str(inches // 36)
miles = str(inches // 63360)

#Print variable values with units label
print(feet + " feet")
print(yards + " yards")
print(miles + " miles")

