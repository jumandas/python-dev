#loops 

#while loop

i= 0
while i < 3:
    print("meow")
    i +=  1

print("-------------------------------------")

#for datatype
# 
for i in range(3):
    print ("meow")
    
print("-------------------------------------")

# u can use _ if you dont need that variable
for _ in range(3):
    print ("meow")
    
#print meow 3 times - one more way to do
print("meow\n" * 3 , end = "")


print("-------------------------------------")

#checking if input is true and printing the data

while True:
    n = int(input("Whats n?"))
    if n > 0:
        break
    
for _ in range(n):
    print("meow")
    