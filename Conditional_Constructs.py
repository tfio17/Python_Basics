#T

###Program to play with if statements

#Get a number from the user
num1 = int(input("Enter a Number:  "))

#If the number is greater than ten say so..
if num1 > 10:
    print("This number is greater than ten!")

    if (num1 > 20):
        print("It's bigger than 20 too!")
        
    if (num1 > 10) and (num1 < 20):
        print("This is between 10 and 20!")
        
elif (num1 ==10):
    print("This number is 10!)
          
else:
    print("This number is less than 10!")

          
print("The End")

