#even-odd number
def main():
    x = int(input("Enter a number"))
    if isEven(x):
        print("Even")
    else:
        print("odd")



def isEven(x):
    if(x % 2 ==0):
        return True
    else:
        return False

main()