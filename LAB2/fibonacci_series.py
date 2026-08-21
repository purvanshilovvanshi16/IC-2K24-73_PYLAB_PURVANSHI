num=int(input("enter the num till series will print: "))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
