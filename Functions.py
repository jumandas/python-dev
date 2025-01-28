#creating own functions - def
def hello(to):
    print("hello,",to)
    

name= input("Whats your name")
hello(name)

#creating own functions - def with default value (if parameter is not passed)
# if no parameter passed it will give world only
def hellos(to="world"):
    print("hello,",to)
  
hellos()    
name= input("Whats your name")
hellos(name)



#using main method 
def main():
    name=input("whats your name")
    hello(name)
    
def hello(to="world"):
    print("hello,",to)
    
main()


#creating a square method to square a number 
def main():
    x= int(input("Whats x"))
    print("x squared is",square(x))
    
def square(n):
    #return n*n
    return pow(n,2)
    
main()

#self excerise to add 2 numbers
def main():
    x = int(input("Enter x"))
    y = int(input("Enter y"))
    print(add(x,y))

def add(x,y):
    return int(x) + int(y)
    
main()

