#
#
## Tom
#
#
## Zelle ch 5.5 pg 142
# a program to convert textual messages to a sequence of nums
# utilizing the underlying Unicode encoding

def main():
    # Get the message to encode:
    message = input("Enter the message to encode:  ")

    print("\n Here are the Unicode codes")

    #Loop through the message and print Unicode Values

    for ch in message:
        print(ord(ch), end=" ")

    print() #blank line before prompt

main()
