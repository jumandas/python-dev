#exception handling with loops 
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("Whats x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
    
#main()


#pass - means ignoring exception
def main():
    x = get_int("Whats x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            pass
        else:
            return x
    
main()
