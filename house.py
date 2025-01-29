#match (switch-case)

name= input("Whats your name?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
# using _ for else statement when we dont know 
    case _:
        print("Who")
