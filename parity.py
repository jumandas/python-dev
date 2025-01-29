#even-odd number
def main():
    x = int(input("Enter a number"))
    if isEven(x):
        print("Even")
    else:
        print("odd")



# def isEven(x):
#     if(x % 2 ==0):
#         return True
#     else:
#         return False
    
# to write one line if else
def isEven(x):
     if(x % 2 ==0):
        return True if x % 2 ==0 else False

# instead of if-else we can use this way also
def isEvens(n):
    return n % 2 ==0

main()