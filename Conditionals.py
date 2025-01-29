#conditional statements
# > ,>= ,< ,<= ,== ,!=

#if , elif 


#if statement 

x=int(input("Whats the first number?"))
y=int(input("Whats the second number?"))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")


#elif statement 

x=int(input("Whats the first number?"))
y=int(input("Whats the second number?"))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")


#else statement 

x=int(input("Whats the first number?"))
y=int(input("Whats the second number?"))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
    

#or statement 

x=int(input("Whats the first number?"))
y=int(input("Whats the second number?"))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#another way to solve this problem
x = int(input("Whats x"))
y = int(input("Whats y"))

if x!=y:
    print("x is not equal to y")
else:
    print(" x is equal to y")
    
#and

score = int(input("Score:"))

if score >=90 and score <=100:
    print("Grade A")
elif score >=80 and score<=90:
    print("Grade B")
elif score >=70 and score <=80:
    print("Grade C")
elif score >=60 and score <=70:
    print("Grade D")
else:
    print("Grade F")


#score 
score = int(input("Score:"))

if 90 <= score <=100:
    print("Grade A")
elif 80 <= score < 90:
    print("Grade B")
elif 70 <=score <80:
    print("Grade C")
elif 60<= score <70:
    print("Grade D")
else:
    print("Grade F")
    
    
#score doing it another way

score = int(input("Score:"))

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >=60:
    print("Grade D")
else:
    print("Grade F")
    
