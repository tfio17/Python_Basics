#
#
## Tom
#
#
## Zelle ch 1.6 pg 13
# chaos
# a simple program demonstrating chaotic behavior

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1:  "))
    for i in range(10):
        x = 3.9*x*(1-x)
        print(x)
main()
