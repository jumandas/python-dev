def main():
   # print_column(3)
    #print_row(4)
    print_square(3)
    

#def print_row(n):
    #print("?" * n)
    # print("#\n" * n , end="") = prints same as above
       
#nested for-loops 
def print_square(n): 
    #for each row in square
    for i in range(n):
        #for each brick in row
        for j in range(n):
            #print brick
            print("#", end="")
        print()
        
main()