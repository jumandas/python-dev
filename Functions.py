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
