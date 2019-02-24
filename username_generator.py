#
#
## Tom
#
#
## Zelle ch 5.2 pg 134
# generates usernames from user's name
#

def main():
    print("This program generates computer usernames. \n")

    # get user's first and last names
    first = input("Please enter your first name:  ")
    last =  input("Please enter your last name:  ")

    # concatenate the first initial with 7 chars of last name
    uname = first[0] + last [:7]

    # output the username
    print("Your username is:  ", uname)

main()
