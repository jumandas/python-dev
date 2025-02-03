#exceptions(Error handling)
#valueError - based on datatype
#NameError - declaration of variable issue
# We can use else with exception handling
#using loops until a valid value is entered
# we are using While True to get a valid input
while True:
    try:
        x = int(input("whats x ?"))
    except ValueError:
        print("x is not an integer")
    else:
        break
    
print(f"x is {x}")

