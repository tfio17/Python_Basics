#
#
## Tom
#
#
## Zelle ch 5.5 pg 145
# a program to convert Unicode to text
#

def main():
    # Get the message to decode:
    message = input("Enter the message to decode:  ")

    #Loop through the message and print Unicode Values

    mess = ""

    for numStr in message.split():
        codeNum = int(numStr)
        mess = mess + chr(codeNum)

    print("\n The decoded message is: ", mess)

    print() #blank line before prompt

main()
