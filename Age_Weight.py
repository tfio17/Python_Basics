#
#Tom Fiorelli
#
#Stores Age and Weight, guessing game
#
#
#
#Begin

#Enter fixed age and weight
Age = int(25)
Weight = int(135)

#Request age and weight guesses
Wg = int(input("Please guess the weight:  "))
Ag = int(input("Please guess the age:  "))

#set up logic
if Ag > Age and Wg > Weight:
    print("Both Higher")
    
elif Ag < Age and Wg < Weight:
    print("Both Lower")

elif Ag == Age and Wg == Weight:
    print("Bingo")

else:
    print("Game Over")
