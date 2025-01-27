#hello world 
print("Hello World")

#Input with return values (variables)
name = input("Whats your name?")

#Input with return values (variables) Add all the function in the same line
name = input("Whats your name?").strip().title()

#remove whitespace from string
name = name.strip()

#Capitalize user's name (only first letter of first word)
name = name.capitalize()

#Capitalize user's fullname
name = name.title()

#use combined function
name = name.strip().title()


print("Hello, " + name)

#print on same line - other way-1
print("Hello, ", end="")
print(name)

#print on same line - other way-2
print("hello,",name,sep="")

#print on same line - other way-3
print("hello,", name)


#print with double quotes ,escape string
print('hello, "friend"')
print("hello , \"friend\"")

#special string
print(f"hello,{name}")

