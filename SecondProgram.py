#addition of 2 numbers - int
x=input("Whats x?")
y=input("Whats y?")

z= int(x) + int(y)

print(z)

#nested addition - float
a=int(input("a"))
b=int(input("b"))

print(a+b)

#float
c=float(input("c"))
d=float(input("d"))

print(c+d)

#round (round figure)
z= round(c+d)

# format the number with a comma
print(f"{z:,}")


#divide 
e=float(input("e"))
f=float(input("f"))
g = e/f

print(g)

#divide and rounding off the value upto 2 digits
e=float(input("e"))
f=float(input("f"))
g = round(e/f,2)

print(g)

#divide and printing the value upto 2 digits
e=float(input("e"))
f=float(input("f"))
g = e/f

print(f"{g:.2f}")



