x =int (input("enter number to check: "))
sum=0
for i in range(1,x):
    if x % i ==0:
            print(i,end=" ")
            sum+=i
if sum==x:
    print(x,"\n is a perfect number")
else:
     print(x,"is not a perfect square")    

s=int(input("enter the starting value"))       
e=int(input("enter the ending value"))  
for x in range(s,e):
    sum=0     

    for i in range(1,x):
        if x % i ==0:
            sum+=i
    if sum==x:
        print(x)

     
    
    
s