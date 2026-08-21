#right angle triangle
n=int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print( )    

#number pattern
n=int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print( ) 

#pyramid
n=int(input("enter the number of row: "))    
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")    
    print()